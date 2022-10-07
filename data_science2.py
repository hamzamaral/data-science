# -*- coding: utf-8 -*-
"""
Created on Wed Jun 5 05:25:55 2022

@author: HAMZA
"""
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

data = pd.read_csv('../../../../../pokemon.csv')
data.head()

data.describe()

data.dtypes

data.info()

data.corr()

data.head(10)

asd=pd.DataFrame(data)
print(asd)

asd["Defense"]
asd.Speed.mean()

f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()
