import pandas as pd
import numpy as np

df1=pd.read_csv("/home/vinit/Downloads/2017-11-01.csv")
df2=pd.read_csv("/home/vinit/Downloads/2017-11-02.csv")
df3=pd.read_csv("/home/vinit/Downloads/2017-11-03.csv")

#Joining datasets
l=[df1,df2,df3]
df=pd.concat(l)

#Dataset information
print(df.shape)
print( df.describe())
print(df.head())
df.isnull().any()

import string
lower=df['text'].str.lower()
lower.head()

#finding references to Donald Trump
ref=lower.str.contains("donald|trump|president|john miller")
print(ref.head())
donald=lower[ref]
print(donald.head())

#Ordering accounts by the frequency of tweets abt donald
freq=df['user_id'][ref].value_counts()
print(freq.head())
total_unique_accounts=df['user_id'].value_counts().count()
total_unique_tweeting_abt_trump=freq.count()

#finding +ve tweets abt donald trump
positive=donald.str.contains("good|very good|nice")
positive=donald[positive]

percent=(float(positive.count())/float(donald.count()))*100
print(percent)

