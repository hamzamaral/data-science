# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 01:00:06 2022

@author: HAMZA
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

data = pd.read_csv('../../../../../pokemon.csv')

asd=pd.DataFrame(data)
print(asd)


# Example of list comprehension
num1 = [1,2,3]
num2 = [i + 1 for i in num1 ]
print(num2
      
num11=[4,5,6,7,8,9]
num12=[i**2 for i in num11]
print(num12)



# Conditionals on iterable
num1 = [5,10,15]
num2 = [i**2 if i == 10 else i-5 if i < 7 else i+5 for i in num1]
print(num2)



num11=[4,5,6,7,8,9]
num12=[i**2 if i== 0 else i/2 if i<5 else i+i  for i in num11]
print(num12)


# lets return pokemon csv and make one more list comprehension example
# lets classify pokemons whether they have high or low speed. Our threshold is average speed.
threshold = sum(data.Speed)/len(data.Speed)
data["speed_level"] = ["high" if i > threshold else "low" for i in data.Speed]
data.loc[:10,["speed_level","Speed"]] # we will learn loc more detailed later



# lets return pokemon csv and make one more list comprehension example
# lets classify pokemons whether they have high or low speed. Our threshold is average speed.
threshold = sum(data.Speed)/len(data.Speed)
data["speed_level"] = ["high" if i > threshold else "low" for i in data.Speed]
data.loc[:11,["speed_level","Speed"]] # we will learn loc more detailed later


#%%

# shape gives number of rows and columns in a tuble
data.shape

# info gives data type like dataframe, number of sample or row, number of feature or column, feature types and memory usage
data.info()


print(data['Type 1'].value_counts(dropna =False))

print(data['Type 2'].value_counts())

data.describe() #ignore null entries

data.boxplot(column='Attack',by = 'Legendary')