import pandas as pd
import numpy as np
import string

#loading dataset
url="/home/vinit/Desktop/test.csv"
data=pd.read_csv(url)

#dataset information
data.head()
data.describe()
data.shape

#dataset containing 2015 posts
df=data.iloc[0:9020,:]
df.to_csv("/home/vinit/Desktop/2015.csv")
url="/home/vinit/Desktop/2015.csv"
df=pd.read_csv(url)
df.shape

#dataset processing
list(df)
del(df['Profile Picture URL'])
del(df['Link'])
df.shape

#counting types of posts in 2015
df['Type'].value_counts()

#Finding reposts in 2015
lower=df['Caption'].str.lower()
lower.head()
repost=lower.str.contains("repost")
repost.head()   #true false type
repost.isnull().any()
repost=repost.fillna(False)  #filling null with False
lower=lower.fillna(0)
text=lower[repost]   #reposts
text.head()

#Reposts analysis
text.shape      #no. of reposts
df['Type'][repost].value_counts()  #no. of posts types
df['Username'][repost].value_counts()

#Location of people from where reposts are done
df['Username'][repost].value_counts()  #people and the no. of reposts by them
latitude=df['Latitude'][repost].value_counts()
longitude=df['Longitude'][repost].value_counts()
location=df['Location Name'][repost].value_counts()

#finding original posts and analysis
text2=lower[-repost]
df['Type'][-repost].value_counts()  #no. of posts types
df['Username'][-repost].value_counts()


#Location of people from where original posts are done
latitude_orig=df['Latitude'][-repost].value_counts()
longitude_orig=df['Longitude'][-repost].value_counts()
location_orig=df['Location Name'][-repost].value_counts()