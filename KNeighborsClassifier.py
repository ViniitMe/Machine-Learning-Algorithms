#K nearest neighbors classification type problem
import pandas as pd
import numpy as np
from sklearn import preprocessing,cross_validation,neighbors
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

url = "C://Users/User/Desktop/breast-cancer-wisconsin.data.txt"
features=['samp_code_no','clump_thick','unif_cell_size','unif_cell_shape','marg_adh','sin_ep_cell_size','bare_nuclie','bland_chrom','norm_nuclei','mitosis','label']
dataset=pd.read_csv(url,names=features)

dataset.replace('?', -99999, inplace=True) 
dataset.drop(['samp_code_no'],1,inplace=True)
#print(dataset.shape)
#print(dataset.head())
#print(dataset.describe())


x=np.array(dataset.drop(['label'],1))
y=np.array(dataset['label'])

x_train,x_test,y_train,y_test=cross_validation.train_test_split(x,y,test_size=0.2)
clf=neighbors.KNeighborsClassifier()
clf.fit(x_train,y_train)
accuracy=clf.score(x_test,y_test)
print(accuracy)

new_example=np.array([1,1,1,1,9,1,5,7,4])
new_example=new_example.reshape(1,-1)    #when we have 2 samples(i.e training ex)then it would be(2,-1)...so better to use (len(new_example),-1)
prediction=clf.predict(new_example)
print(prediction)
