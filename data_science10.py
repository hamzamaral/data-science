# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 17:50:55 2022

@author: HAMZA
"""


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('../../../../../pokemon.csv')

asd=pd.DataFrame(data)
print(asd)

data_new = data.head()    # I only take 5 rows into new data
data_new


# data frames from dictionary
country = ["Spain","France"]
population = ["11","12"]
list_label = ["country","population"]
list_col = [country,population]
zipped = list(zip(list_label,list_col))
data_dict = dict(zipped)
df = pd.DataFrame(data_dict)
df

df["capital"] = ["madrid","paris"]
df

data1 = data.loc[:,["Attack","Defense","Speed"]]
data1.plot()

data1.plot(subplots = True)
plt.show()

data1.plot(kind = "scatter",x="Attack",y = "Defense")
plt.show()


data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True)


fig, axes = plt.subplots(nrows=2,ncols=1)
data1.plot(kind = "hist",y = "Defense",density =True ,bins = 50,range= (0,250),ax = axes[0])
data1.plot(kind = "hist",y = "Defense",density =True ,bins = 50,range= (0,250),ax = axes[1],cumulative = True)
plt.savefig('graph.png')
plt


time_list = ["1992-03-08","1992-04-12"]
print(type(time_list[1])) # As you can see date is string
 
datetime_object = pd.to_datetime(time_list)
print(type(datetime_object))


import warnings
warnings.filterwarnings("ignore")
# In order to practice lets take head of pokemon data and add it a time list
data2 = data.head()
date_list = ["1992-01-10","1992-02-10","1992-03-10","1993-03-15","1993-03-16"]
datetime_object = pd.to_datetime(date_list)
data2["date"] = datetime_object

data2= data2.set_index("date")
data2 

time_list = ["1992-03-08","1992-04-12"]
print(type(time_list[1])) # As you can see date is string
# however we want it to be datetime object
datetime_object = pd.to_datetime(time_list)
print(type(datetime_object))


# Now we can select according to our date index
print(data2.loc["1993-03-16"])
print(data2.loc["1992-03-10":"1993-03-16"])


data2.resample("A").mean()

data2.resample("M").mean()

data2.resample("M").first().interpolate("linear")

data2.resample("M").mean().interpolate("linear")


data=data.set_index("#")

data["HP"][1]
data.HP[1]

data.loc[1,"HP"]

data[["HP","Attack"]]


print(type(data["HP"]))     # series
print(type(data[["HP"]]))   # data frames

data.loc[1:10,"HP":"Defense"]

data.loc[10:1:-1,"HP":"Defense"]

data.loc[1:10,"Speed":] 


boolean = data.HP > 200
data[boolean]

first_filter = data.HP > 150
second_filter = data.Speed > 35
data[first_filter & second_filter]

data.HP[data.Speed<15]

def div(n):
    return n/2
data.HP.apply(div)

data.HP.apply(lambda n : n/2)

data["total_power"] = data.Attack + data.Defense
data.head()
# our index name is this:
print(data.index.name)
# lets change it
data.index.name = "index_name"
data.head()

# Overwrite index
# if we want to modify index we need to change all of them.
data.head()
# first copy of our data to data3 then change index 
data3 = data.copy()
# lets make index start from 100. It is not remarkable change but it is just example
data3.index = range(100,900,1)
data3.head()

data = pd.read_csv('../../../../../pokemon.csv')
data.head()


data1 = data.set_index(["Type 1","Type 2"]) 
data1.head(100)


dic = {"treatment":["A","A","B","B"],"gender":["F","M","F","M"],"response":[10,45,5,9],"age":[15,4,72,65]}
df = pd.DataFrame(dic)
df

df.pivot(index="treatment",columns = "gender",values="response")
df.show()

df1 = df.set_index(["treatment","gender"])
df1
# lets unstack it

# level determines indexes
df1.unstack(level=0)

df1.unstack(level=1)

df2 = df1.swaplevel(0,1)

df
 
pd.melt(df,id_vars="treatment",value_vars=["age","response"])
df2

df

df.groupby("treatment").mean()   # mean is aggregation / reduction method

df.groupby("treatment").age.max() 

df.groupby("treatment")[["age","response"]].min() 

df.info()































