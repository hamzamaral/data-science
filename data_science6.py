# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 19:57:46 2022

@author: HAMZA
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

data = pd.read_csv('../../../../../pokemon.csv')

asd=pd.DataFrame(data)
print(asd)

# lambda function
square = lambda x: x**2     # where x is name of argument
print(square(4))
tot = lambda x,y,z: x+y+z   # where x,y,z are names of arguments
print(tot(1,2,3))

kare= lambda x:x**2
print(kare(5))

art = lambda x,y,z:x+y+x

print(tot(4,2,3))

number_list = [1,2,3]
y = map(lambda x:x**2,number_list)
print(list(y))

number= [1,2,3,4]
k=map(lambda x:x**2,number)
print(list(k))
print(k)

# iteration example
name = "ronaldo"
it = iter(name)
print(next(it))    # print next iteration
print(*it)         # print remaining iteration


isim='merhaba dünya'
it =  iter(isim)
print(it)

print(next(it))
print(*it)
print(it)


# zip example
list1 = [1,2,3,4]
list2 = [5,6,7,8]
z = zip(list1,list2)
print(z)
z_list = list(z)
print(z_list)


mhm =[1,2,3]
hl=[4,5,6]

kvt=zip(mhm,hl)
print(kvt)

kvt2=list(kvt)

print(kvt2)



un_zip = zip(*z_list)
un_list1,un_list2 = list(un_zip) # unzip returns tuple
print(un_list1)
print(un_list2)
print(type(un_list2))

n_zipp=zip(*kvt2)
n_list1,n_list2 =list(n_zipp)
print(n_list1)
print(n_list2)


