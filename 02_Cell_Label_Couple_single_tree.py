#This is the code for the generation of Decision Trees:
#-one for all values of the target feature
#-one for the couple of values 0_2
#-one for the couple of values 2_3
#-one for the couple of values 3_4

#Importing packages
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

#Importing data
#Drop the 'Unnamed:0' and 'cell_type' features
df = pd.read_csv('whole_dataset_count_matrix.csv')

features_to_drop = ['Unnamed: 0', 'cell_type']
df = df.drop(features_to_drop, axis=1)

#Creating dictionary for plotting the trees and extracting feature importances
couples_of_values = {"all_values": {"df": df,
                                    "dt": DecisionTreeClassifier(max_depth=8, criterion='gini', random_state=1),
                                    "figureTitle": 'Decision Tree Leiden',
                                    "figureFileName": 'Decision_Tree_Leiden.pdf',
                                    "featImpFileName": 'Feature_importances_Decision_Tree_Leiden.csv'
                                    },
                     "values_0_2": {"df": df[df['leiden'].isin([0, 2])],
                                    "dt": DecisionTreeClassifier(max_depth=3, criterion='gini', random_state=1),
                                    "figureTitle": 'Decision Tree Leiden 0_2',
                                    "figureFileName": 'Decision_Tree_Leiden_0_2.pdf',
                                    "featImpFileName": 'Feature_importances_Decision_Tree_0_2.csv'
                                    },
                     "values_2_3": {"df": df[df['leiden'].isin([2, 3])],
                                    "dt": DecisionTreeClassifier(max_depth=2, criterion='gini', random_state=1),
                                    "figureTitle": 'Decision Tree Leiden 2_3',
                                    "figureFileName": 'Decision_Tree_Leiden_2_3.pdf',
                                    "featImpFileName": 'Feature_importances_Decision_Tree_2_3.csv'
                                    },
                     "values_3_4": {"df": df[df['leiden'].isin([3, 4])],
                                    "dt": DecisionTreeClassifier(max_depth=2, criterion='gini', random_state=1),
                                    "figureTitle": 'Decision Tree Leiden 3_4',
                                    "figureFileName": 'Decision_Tree_Leiden_3_4.pdf',
                                    "featImpFileName": 'Feature_importances_Decision_Tree_3_4.csv'
                                    }
                     }

#Transforming 'leiden' values from integer to string
#Splitting features into X and y variables:
#- X stores descriptive features
#- y stores class feature 'Label_leiden'
#Creating training set and test set
#Training the models
#Creating tree structures
#Extracting feature importances
for element, model in couples_of_values.items():
    df = model["df"]
    print(df['leiden'].dtype)
    df['leiden'] = df['leiden'].astype(str)
    print(df['leiden'].dtype)

    class_labels = sorted(df['leiden'].unique())
    class_count = df['leiden'].value_counts()
    print(class_labels, "\n")
    print(class_count, "\n")

    print(df['leiden'].unique())
    column_names = list(df.columns)
    num_of_columns = len(column_names)
    descriptive_features_names = column_names[0: num_of_columns - 1]
    class_attribute_name = column_names[-1]

    X = df[descriptive_features_names]
    y = df[class_attribute_name]
    # Transform y to Dataframe
    y = pd.DataFrame(y, columns=['leiden'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=1, stratify=y)

    dt = model["dt"]
    dt.fit(X_train, y_train)
    y_pred = dt.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(accuracy)

    plt.figure(figsize=(20, 10))
    plot_tree(dt, filled=True, feature_names=X.columns, class_names=class_labels, rounded=True)
    title = model["figureTitle"]
    plt.title(title)
    plt.tight_layout()
    name_file = model["figureFileName"]
    plt.savefig(name_file)
    plt.show()

    feat_imp = dt.feature_importances_
    feature_importances = pd.DataFrame({'Feature': X_train.columns, 'Importance': feat_imp}).sort_values(by='Importance', ascending=False)
    feat_imp_file_name = model["featImpFileName"]
    feature_importances.to_csv(feat_imp_file_name, index=False)


