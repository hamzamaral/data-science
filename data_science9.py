# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 01:49:39 2022

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

data_new = data.head()    # I only take 5 rows into new data
data_new


melted = pd.melt(frame=data_new,id_vars = 'Name', value_vars= ['Attack','Defense'])
melted

melted.pivot(index = 'Name', columns = 'variable',values='value')

data1 = data.head()
data2= data.tail()
conc_data_row = pd.concat([data1,data2],axis =0,ignore_index =True) # axis = 0 : adds dataframes in row
conc_data_row


data1 = data['Attack'].head()
data2= data['Defense'].head()
conc_data_col = pd.concat([data1,data2],axis =1) # axis = 1 : adds dataframes in column
conc_data_col


data.dtypes

# lets convert object(str) to categorical and int to float.
data['Type 1'] = data['Type 1'].astype('category')
data['Speed'] = data['Speed'].astype('float')

# As you can see Type 1 is converted from object to categorical
# And Speed ,s converted from int to float
data.dtypes

data.info()


data["Type 2"].value_counts(dropna =False)


data1=data   # also we will use data to fill missing value so I assign it to data1 variable
data1["Type 2"].dropna(inplace = True)

assert 1==1 # return nothing because it is true


assert  data['Type 2'].notnull().all() # returns nothing because we drop nan values


data["Type 2"].fillna('empty',inplace = True)

assert  data['Type 2'].notnull().all() # returns nothing because we do not have nan values

data = pd.read_csv('../../../../../pokemon.csv')


















