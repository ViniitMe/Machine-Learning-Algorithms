import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
style.use('ggplot')
from sklearn import datasets
from sklearn.decomposition import PCA
dataset=datasets.load_iris()
x=dataset.data

clf=PCA(n_components=2)
clf.fit(x)
x_new=clf.transform(x)
clf.components_

