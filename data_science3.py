# -*- coding: utf-8 -*-
"""
Created on Wed Jun 7 08:37:20 2022

@author: HAMZA
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

data = pd.read_csv('../../../../../pokemon.csv')

asd=pd.DataFrame(data)
print(asd)

asd["Defense"]
asd.Speed.mean()


data.Speed.plot(kind = 'line', color = 'g',label = 'Speed',linewidth=1,alpha = 0.5,grid = True,linestyle = ':')
data.Defense.plot(color = 'r',label = 'Defense',linewidth=1, alpha = 1,grid = True,linestyle = '-.')
plt.legend(loc='upper right')     # legend = puts label into plot
plt.xlabel('x axis')              # label = name of label
plt.ylabel('y axis')
plt.title('Line Plot')            # title = title of plot
plt.show()


data.Speed.plot(kind ='line', color='g' , grid=True, label="speed",alpha=0.7,linewidth=1)
data.Defense.plot(kind='line', color='red',grid=True, label="DEfence",alpha=1,lineWidth=1)
plt.show()

plt.scatter(data.Speed,data.Generation)



# Scatter Plot 
# x = attack, y = defense
data.plot(kind='scatter', x='Attack', y='Defense',alpha = 0.5,color = 'red')
plt.xlabel('Attack')              # label = name of label
plt.ylabel('Defence')
plt.title('Attack Defense Scatter Plot')            # title = title of plot


data.Speed.plot(kind = 'hist',bins = 50,figsize = (12,12))
plt.show()


# clf() = cleans it up again you can start a fresh
data.Speed.plot(kind = 'hist',bins = 50)
plt.clf()
# We cannot see plot due to clf()