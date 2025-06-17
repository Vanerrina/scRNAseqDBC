#This is the code for the Decision Tree model,
#trained and tested on 5 folds generated through Cross Validation.
#The code also provides the Confusion Matrix and the ROC Curve for the aforementioned model

#Importing packages
import pandas as pd
import warnings
from sklearn.model_selection import GridSearchCV, cross_val_predict, cross_validate
from sklearn.model_selection import StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report, \
    roc_curve, auc
from sklearn.preprocessing import LabelBinarizer
import numpy as np
from itertools import cycle

warnings.filterwarnings('ignore')

rcParams['font.family'] = 'Arial'

#ROC Curve Function
def plot_multiclass_roc_crossval(classifier, X, y, cv):
    lb = LabelBinarizer()
    y_binarized = lb.fit_transform(y)

    y_true_binarized = []
    y_predicted = []

    for train_idx, test_idx in cv.split(X, y):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

        classifier.fit(X_train, y_train)
        y_pred = classifier.predict_proba(X_test)
        y_predicted.append(y_pred)
        y_true_binarized.append(lb.transform(y_test))

    y_true_binarized = np.vstack(y_true_binarized)
    y_predicted = np.vstack(y_predicted)

    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    n_classes = y_binarized.shape[1]

    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_true_binarized[:, i], y_predicted[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    fpr["micro"], tpr["micro"], _ = roc_curve(y_true_binarized.ravel(), y_predicted.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
    print("Micro-average AUC: {:.4f}".format(roc_auc["micro"]))

    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(n_classes):
        mean_tpr += np.interp(all_fpr, fpr[i], tpr[i])
    mean_tpr /= n_classes

    fpr["macro"] = all_fpr
    tpr["macro"] = mean_tpr
    roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])

    roc_curve_figure = plt.figure(figsize=(12, 8))
    lw = 3

    colors = cycle(["aqua", "darkorange", "cornflowerblue", "green", "red", "purple"])
    for i, color in zip(range(n_classes), colors):
        plt.plot(fpr[i], tpr[i], color=color, lw=lw,
                 label="Cluster {0} (AUC = {1:0.2f})".format(i, roc_auc[i]), )

    plt.plot([0, 1], [0, 1], "k--", lw=lw)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel("False Positive Rate", fontsize=30, labelpad=10)
    plt.ylabel("True Positive Rate", fontsize=30, labelpad=10)
    plt.tick_params(axis='both', which='major', labelsize=18)
    plt.legend(loc="lower right",
               frameon=True,
               fancybox=True,
               framealpha=1,
               edgecolor='black',
               facecolor='white',
               fontsize=20
               )
    plt.tight_layout()
    plt.show()
    return roc_curve_figure

#Importing data
#Drop the 'Unnamed:0' and 'cell_type' features
#Transforming 'Leiden' values from integer to string
df = pd.read_csv('whole_dataset_count_matrix.csv')

print(df.info())
print(df['Unnamed: 0'].nunique())

features_to_drop = ['Unnamed: 0', 'cell_type']
df = df.drop(features_to_drop, axis=1)

print(df['leiden'].dtype, "\n")
df['leiden'] = df['leiden'].astype(str)
print(df['leiden'].dtype, "\n")

class_labels = sorted(df['leiden'].unique())
class_count = df['leiden'].value_counts()
print(class_labels, "\n")
print(class_count, "\n")

#Splitting features into X and y variables:
#- X stores descriptive features
#- y stores class feature 'leiden'
column_names = list(df.columns)
num_of_columns = len(column_names)
descriptive_features_names = column_names[0: num_of_columns-1]
class_attribute_name = column_names[-1]

X = df[descriptive_features_names]
y = df[class_attribute_name]
#Transform y to Dataframe
y = pd.DataFrame(y, columns=['leiden'])

#GridSearchCV
dt_model = DecisionTreeClassifier(random_state=1)
dt_model_parameters = [
    {'max_depth' : [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 'criterion' : ['gini', 'entropy', 'log_loss']}
]
dt_grid_search = GridSearchCV(estimator=dt_model, param_grid=dt_model_parameters, scoring='accuracy',
                              return_train_score=True, n_jobs=-1)
dt_grid_search.fit(X, y)
print("Best parameters:", dt_grid_search.best_params_)

#Decision Tree model
dt = DecisionTreeClassifier(max_depth=9, criterion='gini', random_state=1)

#Cross Validation
results = []

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)
cv_pred = cross_val_predict(dt, X, y, cv=skf)
cv_scores = cross_validate(dt, X, y, cv=skf,
                           scoring=['accuracy', 'precision_macro', 'recall_macro', 'f1_macro'])

#Metrics results
mean_accuracy = np.mean(cv_scores['test_accuracy'])
mean_precision = np.mean(cv_scores['test_precision_macro'])
mean_recall = np.mean(cv_scores['test_recall_macro'])
mean_f1 = np.mean(cv_scores['test_f1_macro'])

results.append({
    'Classifier': 'Decision Tree',
    'Mean Accuracy': mean_accuracy,
    'Mean Precision': mean_precision,
    'Mean Recall': mean_recall,
    'Mean F1': mean_f1,
    'Fold Accuracy': cv_scores['test_accuracy'],
    'Fold Precision': cv_scores['test_precision_macro'],
    'Fold Recall': cv_scores['test_recall_macro'],
    'Fold F1': cv_scores['test_f1_macro']})

results = pd.DataFrame(results)
results.to_csv("Classification_Results_DecisionTree.csv", index=False)

#Classification report
class_report = classification_report(y, cv_pred, target_names=class_labels)
with open('Decision_Tree_Classification_report.txt', 'w') as fout:
    fout.write(class_report)

#Confusion matrix
labels = ['Cluster 0', 'Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5']
cm_rel = confusion_matrix(y, cv_pred, normalize='true')
cm_relative = ConfusionMatrixDisplay(confusion_matrix=cm_rel, display_labels=labels)
fig, ax = plt.subplots(figsize=(16, 10))
cm = cm_relative.plot(cmap='Blues', ax=ax)
cm.im_.set_clim(0, 1)
cbar = cm.figure_.axes[-1]
cbar.tick_params(labelsize=28)
ax.tick_params(axis='both', labelsize=28)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
ax.set_xlabel('Predicted label', fontsize=30, labelpad=15)
ax.set_ylabel('True label', fontsize=30, labelpad=15)
for row in cm.text_:
    for text in row:
        text_value = text.get_text()
        if text_value.replace('.', '', 1).isdigit():
            formatted_value = "{:.2f}".format(float(text_value))
            text.set_text(formatted_value)
            text.set_fontsize(25)
            text.set_fontweight('bold')
plt.tight_layout()
plt.savefig('Confusion_matrix.pdf')
plt.show()

#ROC Curve
roc_curve_fig = plot_multiclass_roc_crossval(dt, X, y, skf)
roc_curve_fig.savefig("Roc_Curve.pdf")