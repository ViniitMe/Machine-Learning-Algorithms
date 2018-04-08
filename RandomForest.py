import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names=['sepal-length','sepal-width','petal-length','petal-width','label']
dataset=pd.read_csv(url,names=names)
df=dataset

#info of the dataset
df.shape
df.head()
df.describe()
df.isnull().any()

x=df.iloc[:,0:4]
y=df.iloc[:,4:5]
x_train,x_test,y_train,y_test=cross_validation.train_test_split(x,y,test_size=.2)

#applying classifier
clf=RandomForestClassifier(n_estimators=100)  
#note
#n_estimators signifies the no. of trees in the forest(default=10)
#criterion is the function to measure the quality of the split(default=Gini)
clf.fit(x_train,y_train)

y_pred=clf.predict(x_test)
accuracy=clf.score(x_test,y_test)
print(accuracy)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred) #same thing as clf.score
print(confusion_matrix(y_test,y_pred))
#confusion matrix will tell us the no. of prediction of every class
print(classification_report(y_test,y_pred))


#plotting the importance of the features
importances=clf.feature_importances_
plt.title('Feature Importances')
plt.xlabel('Relative Importance')
indices=np.argsort(importances)
plt.barh(range(len(indices)),importances[indices],color='b',align='center')
plt.yticks(range(len(indices)),x[indices])
plt.show()


