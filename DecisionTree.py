import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import cross_validation

url="https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data"
names=['A','B','C','D','E']
dataset=pd.read_csv(url,names=names)
df=dataset
df.shape
df.head()
df.isnull().any()
df['A'].value_counts()

x=df.iloc[:,1:5]
y=df.iloc[:,0]
x_train,x_test,y_train,y_test=cross_validation.train_test_split(x,y,test_size=.2)
clf=DecisionTreeClassifier()
clf.fit(x_train,y_train)

y_pred=clf.predict(x_test)
y_pred[0:9]
clf.score(x_test,y_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

