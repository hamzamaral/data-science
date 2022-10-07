# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 01:04:32 2022

@author: HAMZA
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

data = pd.read_csv('../../../../../pokemon.csv')

asd=pd.DataFrame(data)
print(asd)

data_new = data.head()    # I only take 5 rows into new data
data_new

melted1=pd.melt(frame=data_new,id_vars='Name',value_vars=["Attack",'Defense'])
melted1

melted1.pivot(index='Name',columns='variable', values='value')
