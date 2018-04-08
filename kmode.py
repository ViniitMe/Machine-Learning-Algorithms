import pandas as pd
import numpy as np
url="https://archive.ics.uci.edu/ml/machine-learning-databases/soybean/soybean-small.data"
dataset=pd.read_csv(url)
#dataset.head()
df=dataset.iloc[:,0:35]
df.shape
from kmodes.kmodes import KModes
km=KModes(n_clusters=4,init='Huang',n_init=5,verbose=1)
clusters=km.fit_predict(df)
print(km.cluster_centroids_)
print(km.labels_)
a=km.labels_
x=dataset.iloc[:,35]

