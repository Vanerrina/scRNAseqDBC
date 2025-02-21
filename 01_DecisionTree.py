#This is the code for the Decision Tree model,
#trained and tested on 5 folds generated through Cross Validation.
#The code also provides the Confusion Matrix for the aforementioned model

#Importing packages
import pandas as pd
import warnings
from sklearn.model_selection import cross_val_predict, cross_validate
from sklearn.model_selection import StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
import numpy as np

warnings.filterwarnings('ignore')

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

#Decision Tree model
dt = DecisionTreeClassifier(max_depth=8, criterion='gini', random_state=1)

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
    'Classifier': 'Logistic Regression',
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

#Confusion matrices:
# - Relative values
# - Absolute values
cm_rel = confusion_matrix(y, cv_pred, normalize='true')
cm_relative = ConfusionMatrixDisplay(confusion_matrix=cm_rel, display_labels=class_labels)
cm_relative.plot(cmap='Blues')
#plt.xticks(rotation=65)
plt.title('Decision Tree confusion matrix with relative values')
plt.tight_layout()
plt.savefig('Decision_Tree_confusionM_Leiden_relative_values.pdf')
plt.show()

cm_abs = confusion_matrix(y, cv_pred, normalize=None)
cm_absolute = ConfusionMatrixDisplay(confusion_matrix=cm_abs, display_labels=class_labels)
cm_absolute.plot(cmap='Blues')
#plt.xticks(rotation=65)
plt.title('Decision Tree confusion matrix with absolute values')
plt.tight_layout()
plt.savefig('Decision_Tree_confusionM_Leiden_absolute_values.pdf')
plt.show()

