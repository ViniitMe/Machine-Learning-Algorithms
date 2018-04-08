import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
dataset=quandl.get('WIKI/GOOGL')
#print(dataset.head())             #we are loading stock
df=dataset[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
#print(dataset.head())
#print(df.head())
forecast_col='Adj. Close'
df.fillna(-99999,inplace=True)
forecast_out=int (math.ceil(0.01*len(df)))
df['label']=df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
#print(df.head())x=np.array(df.drop(['label'],1))#x-independent variable(features)excluding label ; y-dependent variable i.e. label
x=np.array(df.drop(['label'],1))
y=np.array(df['label'])

x=preprocessing.scale(x)
x_train,x_test,y_train,y_test=cross_validation.train_test_split(x,y,test_size=0.2)   #test set is 20% ,train set is 80%

clf=LinearRegression()        # calling classifier from sklearn
clf.fit(x_train,y_train)      #training the train dataset using classifier(fit.....for train)
accuracy=clf.score(x_test,y_test)      #testing(score....for test)
print(accuracy)
