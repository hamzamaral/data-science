# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 17:51:41 2022

@author: HAMZA
"""
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

data = pd.read_csv('../../../../../pokemon.csv')

asd=pd.DataFrame(data)
print(asd)
#WHILE and FOR LOOPS

# Stay in loop if condition( i is not equal 5) is true
i = 0
while i != 5 :
    print('i is: ',i)
    i +=1
print(i,' is equal to 5')

# Stay in loop if condition( i is not equal 5) is true
lis = [1,2,3,4,5]
for i in lis:
    print('i is: ',i)
print('')

# Enumerate index and value of list
# index : value = 0:1, 1:2, 2:3, 3:4, 4:5
for index, value in enumerate(lis):
    print(index," : ",value)
print('')   

# For dictionaries
# We can use for loop to achive key and value of dictionary. We learnt key and value at dictionary part.
dictionary = {'spain':'madrid','france':'paris'}
for key,value in dictionary.items():
    print(key," : ",value)
print('')

# For pandas we can achieve index and value
for index,value in data[['Attack']][0:2].iterrows():
    print(index," : ",value)

#%%

#PYTHON DATA SCIENCE TOOLBOX
# example of what we learn above
def tuple_ex():
    """ return defined t tuple"""
    t = (1,2,3)
    return t
a,b,c = tuple_ex()
print(a,b,c)

# guess prints what
x = 2
def f():
    x = 3
    return x
print(x)      # x = 2 global scope
print(f())    # x = 3 local scope



# What if there is no local scope
x = 5
def f():
    y = 2*x        # there is no local scope x
    return y
print(f())         # it uses global scope x  
# First local scope searched, then global scope searched, if two of them cannot be found lastly built in scope searched.



# How can we learn what is built in scope
import builtins
dir(builtins)

#nested function
def square():
    """ return square of value """
    def add():
        """ add two local variable """
        x = 2
        y = 3
        z = x + y
        return z
    return add()**2
print(square())  

def f(x,y=2,m=4):
    k=x+y+m
    
    return k

print(f(7))


# default arguments
def f(a, b = 1, c = 2):
    y = a + b + c
    return y
print(f(5))
# what if we want to change default arguments
print(f(5,4,3))


# flexible arguments *args
def f(*args):
    
    for i in args:
        print(i)
f(1)
f(4)

f(1,2,3,4)

# flexible arguments **kwargs that is dictionary
def f(**kwargs):
    """ print key and value of dictionary"""
    for key, value in kwargs.items():               # If you do not understand this part turn for loop part and look at dictionary in for loop
         print(key, " ", value)
f(country = 'spain', capital = 'madrid', population = 123456)

def f(*args):
    print(args)
    for l in args:
        print(l)
        

f(5,4,7)


def fg(**arh):
    for value,key in arh.items():
         print( value," ", key)
            
            
fg(country = 'spain', capital = 'madrid', population = 123456)

