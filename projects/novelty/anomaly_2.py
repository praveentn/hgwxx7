# load the libraries
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, recall_score, precision_score

import seaborn as sns
sns.set(style="darkgrid")

# load the data 
df = pd.read_csv("creditCard.csv")
df.head()

# Classify as 1 or -1 
df['Class'] = df['Class'].map(lambda x: -1 if x=="'1'" else 1)

fig, ax = plt.subplots(figsize=(8,6))
_ = sns.countplot(x='Class', data=df, ax=ax)
_ = plt.yscale('log')

df = df.drop(['Time'], axis=1)

# split into training an test
X_train, X_test = train_test_split(df, test_size=0.25, random_state=23)

# X,y train
y_train = X_train['Class']

# train using the normal transactions
X_train = X_train[X_train.Class == 1].drop(['Class'], axis=1)

# X,y test
y_test = X_test['Class']
X_test = X_test.drop(['Class'], axis=1).values

print("Train dataset: \n{}".format(pd.value_counts(y_train)))
print("Test dataset: \n{}".format(pd.value_counts(y_test)))

oc_svm = svm.OneClassSVM(nu=0.0007, kernel="rbf", gamma=0.04)

%%time
oc_svm.fit(X_train)

%%time
y_pred = oc_svm.predict(X_test)


LABELS = [1, -1]
conf_matrix = confusion_matrix(y_test, y_pred, labels=LABELS)

fig, ax = plt.subplots(figsize=(10,8))
_ = sns.heatmap(conf_matrix, xticklabels=LABELS, yticklabels=LABELS, 
               annot=True, ax=ax)
_ = ax.set_xlabel('Predicted Class')
_ = ax.set_ylabel('True Class')

# Normalizer confusion matrix
cm = conf_matrix.astype('float') / conf_matrix.sum(axis=1)[:, np.newaxis]
fig, ax = plt.subplots(figsize=(10,8))
_ = sns.heatmap(cm, xticklabels=LABELS, yticklabels=LABELS, 
               annot=True, ax=ax)
_ = ax.set_xlabel('Predicted Class')
_ = ax.set_ylabel('True Class')

print("Precision = {}".format(precision_score(y_test, y_pred, pos_label=-1)))
print("Recall = {}".format(recall_score(y_test, y_pred, pos_label=-1)))
