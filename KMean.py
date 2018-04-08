import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing

url="C://Users/User/Downloads/titanic.xls"
dataset=pd.read_excel(url)
#print(dataset.head())
#print(dataset.shape)
df=dataset.drop(['name','ticket'],1)
df.fillna('a',inplace=True)
inc=LabelEncoder()
enc.fit(df['sex'])
df['sex']=enc.transform(df['sex'])
enc.fit(df['home.dest'])
df['home.dest']=enc.transform(df['home.dest'])
enc.fit(df['cabin'])
df['cabin']=enc.transform(df['cabin'])
enc.fit(df['embarked'])
df['embarked']=enc.transform(df['embarked'])
df.replace('a',0,inplace=True)
print(df.head())
print(df.shape)

x=np.array(df.drop(['survived'],1))
y=np.array(df['survived'])
#print(x)
print(len(x))
#print(y)


clf=KMeans(n_clusters=2)
clf.fit(x)
correct=0
for i in range (len(x)):
    predict_me=np.array(x[i])
    predict_me=predict_me.reshape(-1,len(predict_me))
    prediction=clf.predict(predict_me)
    if prediction[0]==y[i]:
         correct=correct+1
   
print(correct/len(x))
