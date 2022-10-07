# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 18:29:49 2022

@author: HAMZA
"""
"""pip install pip
pip install seaborn"""
"""
Content: 

1. [Load and Check Data](#1)
1. [Variable Description](#2)
    * [Univariate Variable Analysis](#3)
        * [Categorical Variable](#4)
        * [Numerical Variable](#5)
1. [Basic Data Analysis](#6)
1. [Outlier Detection](#7)
1. [Missing Value](#8)
    * [Find Missing Value](#9)
    * [Fill Missing Value](#10)
1. [Visualization](#11)
    * [Correlation Between Sibsp -- Parch -- Age -- Fare -- Survived](#12)
    * [SibSp -- Survived](#13)
    * [Parch -- Survived](#14)
    * [Pclass -- Survived](#15)
    * [Age -- Survived](#16)
    * [Pclass -- Survived -- Age](#17)
    * [Embarked -- Sex -- Pclass -- Survived](#18)
    * [Embarked -- Sex -- Fare -- Survived](#19)
    * [Fill Missing: Age Feature](#20)
1. [Feature Engineering](#21)
    * [Name -- Title](#22)
    * [Family Size](#23)
    * [Embarked](#24)
    * [Ticket](#25)
    * [Pclass](#26)
    * [Sex](#27)
    * [Drop Passenger ID and Cabin](#28)
1. [Modeling](#29)
    * [Train - Test Split](#30)
    * [Simple Logistic Regression](#31)
    * [Hyperparameter Tuning -- Grid Search -- Cross Validation](#32) 
    * [Ensemble Modeling](#33)
    * [Prediction and Submission](#34)
                                  
                                  
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")

import seaborn as sns

from collections import Counter

import warnings
warnings.filterwarnings("ignore")



train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
test_PassengerId = pd.read_csv('gender_submission.csv')

train_df.head()
train_df.columns
train_df.describe()

"""
    VARIABLE DESCRIPTION
PassengerId: unique id number to each passenger
Survived: passenger survive(1) or died(0)
Pclass: passenger class
Name: name
Sex: gender of passenger
Age: age of passenger
SibSp: number of siblings/spouses
Parch: number of parents/children
Ticket: ticket number
Fare: amount of money spent on ticket
Cabin: cabin category
Embarked: port where passenger embarked (C = Cherbourg, Q = Queenstown, S = Southampton)
"""

"""
float64(2): Fare ve Age
int64(5): Pclass, sibsp, parch, passengerId and survived
object(5): Cabin, embarked, ticket, name and sex

"""


"""   
          UNIVARIATE VARIABLE ANALYSIS
Categorical Variable: Survived, Sex, Pclass, Embarked, Cabin, Name, Ticket, Sibsp and Parch
Numerical Variable: Fare, age and passengerId

"""


#    CATEGORICAL VARIABLE

def bar_plot(variable):
    """
        input: variable ex: "Sex"
        output: bar plot & value count
    """
    # get feature
    var = train_df[variable]
    # count number of categorical variable(value/sample)
    varValue = var.value_counts()
    
    # visualize
    plt.figure(figsize = (12,3)) # specify size
    plt.bar(varValue.index, varValue)
    plt.xticks(varValue.index, varValue.index.values)
    plt.ylabel("Frequency")
    plt.title(variable)
    plt.show()
    print("{}: \n {}".format(variable,varValue))
    
    
    
category1 = ["Survived","Sex","Pclass","Embarked","SibSp", "Parch"]
for c in category1:
    bar_plot(c)

category2 = ["Cabin", "Name", "Ticket"]
for c in category2:
    print("{} \n".format(train_df[c].value_counts()))


#               NUMERICAL VARIABLE

def plot_hist(variable):
    plt.figure(figsize = (12,3))
    plt.hist(train_df[variable], bins = 150)
    plt.xlabel(variable)
    plt.ylabel("Frequency")
    plt.title("{} distribution with hist".format(variable))
    plt.show()


numericVar = ["Fare", "Age","PassengerId"]
for n in numericVar:
    plot_hist(n)


"""
#                BASIC DATA ANALYSIS
Pclass - Survived
Sex - Survived
SibSp - Survived
Parch - Survived
"""

train_df[["Pclass","Survived"]].groupby(["Pclass"], as_index = False).mean().sort_values(by="Survived",ascending = False)
#ascending=false -> means sort in descending order -> azalan sıra
# sort_values(by="Survived",ascending = False) survived e göre sırala

#train_df[["pclass","survived"]].groupby(["pclass"],as_index =False).mean.sort_values(by="survived",ascending=False)

train_df[["Sex","Survived"]].groupby(["Sex"], as_index = False).mean().sort_values(by="Survived",ascending = False)
#  as_index = False  -> 
train_df[["SibSp","Survived"]].groupby(["SibSp"], as_index = False).mean().sort_values(by="Survived",ascending = False)

#                   OUTLIER DETECTION


def detect_outliers(df,features):
    outlier_indices = []
    
    for c in features:
        # 1st quartile
        Q1 = np.percentile(df[c],25)
        # 3rd quartile
        Q3 = np.percentile(df[c],75)
        # IQR
        IQR = Q3 - Q1
        # Outlier step
        outlier_step = IQR * 1.5
        # detect outlier and their indeces
        outlier_list_col = df[(df[c] < Q1 - outlier_step) | (df[c] > Q3 + outlier_step)].index
        # store indeces
        outlier_indices.extend(outlier_list_col)

    outlier_indices = Counter(outlier_indices)# counter eleman sayısını bulmamıza  yarar
    multiple_outliers = list(i for i, v in outlier_indices.items() if v > 2)
    
    return multiple_outliers

train_df.loc[detect_outliers(train_df,["Age","SibSp","Parch","Fare"])]
"""
#            MISSING VALUE¶
Find Missing Value
Fill Missing Value
"""

train_df_len = len(train_df)
train_df = pd.concat([train_df,test_df],axis = 0).reset_index(drop = True)

train_df.head()

#             FIND MISSING VALUE

train_df.columns[train_df.isnull().any()]
train_df.isnull().sum()

Counter(train_df.isnull())

"""
                     FILL MISSING VALUE
Embarked has 2 missing value
Fare has only 1

"""
train_df[train_df["Embarked"].isnull()]


train_df.boxplot(column="Fare",by = "Embarked")
plt.show()




train_df["Embarked"] = train_df["Embarked"].fillna("C")
train_df[train_df["Embarked"].isnull()]


train_df[train_df["Fare"].isnull()]
train_df["Fare"] = train_df["Fare"].fillna(np.mean(train_df[train_df["Pclass"] == 3]["Fare"]))

train_df[train_df["Fare"].isnull()]


#%%
#            Visualization

#Correlation Between Sibsp -- Parch -- Age -- Fare -- Survived
list1 = ["SibSp", "Parch", "Age", "Fare", "Survived"]
sns.heatmap(train_df[list1].corr(), annot = True, fmt = ".2f")#annot true coralasyon uzerindeki sayıları göstermeyi sağklar
plt.show()
#Fare feature seems to have correlation with survived feature (0.26)

#SibSp -- Survived
g = sns.factorplot(x = "SibSp", y = "Survived", data = train_df, kind = "bar", size = 6)
g.set_ylabels("Survived Probability")
plt.show()

#Parch -- Survived

k= sns.factorplot(x="parch",y="survived",size=6,data=train_df,kind="Scatter")
k.set_ylabels("survied probability")
plt.show()
#siyah cizgi standar sapmayı gösterin 3 için ortalama 0.6 iken aldığı değerler m 0.2 ila 1 arasında değişir 
#Pclass -- Survived

h=sns.factorplot(x="Pclass",y="Survived",data=train_df,kind="bar",size=6)
h.set_ylabels("survied probability")
plt.show()

#Age -- Survived

g = sns.FacetGrid(train_df, col = "Survived")
g.map(sns.distplot, "Age", bins = 25)
plt.show()

#Pclass -- Survived -- Age

m=sns.FacetGrid(train_df, col = "Survived", row = "Pclass", size = 2)
m.map(sns.hist,"Age",bins=25)
g.add_legend()
plt.show()














