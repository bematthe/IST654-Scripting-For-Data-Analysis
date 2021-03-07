# -*- coding: utf-8 -*-
##Becky Matthews-Pease
##IST 652: Scripting for Data Analysis
#Homework 01
 

import os
import csv
import pandas as pd
import numpy as np 
import sklearn
import pydotplus
from graphviz import Digraph
from pydotplus import graph_from_dot_data
import seaborn as sns
import math
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import statsmodels.api as sm

##############Import Data######################################
data = pd.read_csv("C:\\Users\\becky\\Desktop\\flavors_of_cacao2.csv")

##############Exploring the Data###############################
type(data)  #pandas.core.frame.DataFrame
print(data.columns) #Index(['Year', 'CocoaPerc', 'CoLocation', 'Rating', 'BeanType', 'BeanOrigin'], dtype='object')
total_rows = data.count
print(total_rows) #[1795 rows x 6 columns]>

for col in data:
    print (col, data[col].nunique())
for col in data:
    print (col, data[col].count())
for col in data:
    print (col, data[col].unique())

#Ratings
cRatings = data["Rating"].unique()
cRatings.sort()
print(cRatings)
#Ratings Stats
data["Rating"].describe()

#Counts of Variables
data['BeanType'].value_counts()
data['BeanOrigin'].value_counts()
data['CoLocation'].value_counts()
data['Year'].value_counts()

##############Histograms#######################################
#Histogram of Ratings
x = data["Rating"]
plt.hist(x, bins = 13)
plt.show()
#Histogram of Cocoa Content
x = data['CocoaPerc']
plt.hist(x, bins = 10)
plt.show()
#Histogram of Types of Beans
x = data["BeanType"]
plt.hist(x, bins = 21) 
plt.show()
#Histogram of Bean Origins
x = data["BeanOrigin"]
plt.hist(x, bins = 7) 
plt.show()
#Histogram of HQs
x = data["CoLocation"]
plt.hist(x, bins = 7) 
plt.show()
#Rating Distribution By Year
x = data["Rating"]
y = data["Year"]
plt.hist2d(x, y, bins=10, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')


x = data["Rating"]
y = data["Year"]
plt.hist2d(x, y, bins=10, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')

##############Averages###########################################
#Averages
origin = data.groupby('BeanOrigin')['Rating'].mean() 
bType = data.groupby('BeanType')['Rating'].mean() 
location = data.groupby('CoLocation')['Rating'].mean() 
bYear = data.groupby('Year')['Rating'].mean() 
cPerc = data.groupby('CocoaPerc')['Rating'].mean() 
print(origin)
print(bType)
print(location)
print(bYear)
print(cPerc)

#Average Rating by Bean Origin
beanSource = (0, 1, 2, 3, 4, 5)
averageRating = (3.188034, 3.235915, 2.925000, 3.194037, 3.194037, 3.181566)
plt.ylim(2.8, 3.3)
plt.bar(beanSource,averageRating)
plt.ylabel('Rating')
plt.title('Average Ratings by Bean Origin')
plt.show()
#Average Rating by Company Location
companyLocation = (0, 1, 2, 3, 4, 5, 6)
averageRating = (3.040000, 3.210526, 3.349057, 3.214038, 3.191176, 3.172810, 3.119128)
plt.ylim(3.0, 3.5)
plt.bar(companyLocation,averageRating)
plt.ylabel('Rating')
plt.title('Average Ratings by Company Location')
plt.show()

#############Linear Regression################################
model_lin = sm.OLS.from_formula("Rating ~ CocoaPerc + Year + CoLocation + BeanType + BeanOrigin", data=data)
result_lin = model_lin.fit()
result_lin.summary()

model_lin = sm.OLS.from_formula("BeanOrigin ~ Rating", data=data)
result_lin = model_lin.fit()
result_lin.summary()


########Coca Content of bars with beans from most highly ranked source and lowest ranked source###########
###What are the Cocoa Content Percentages for Bars made from Beans Sourced from Asia?######
source = data[data.BeanOrigin == 1]
Content = source['CocoaPerc']
np.array(Content)
ContentList = Content.unique()
type(ContentList)
ContentList.sort()
print(ContentList)

####What are the Cocoa Content Percentages for Bars made from Beans Sourced from Australia?####
source = data[data.BeanOrigin == 2]
Content = source['CocoaPerc']
np.array(Content)
ContentList = Content.unique()
type(ContentList)
ContentList.sort()
print(ContentList)

##########Output Files######################
###Write file to Excel containing unique values of dataset:
rows = [ ['Year', '2014', '2008', '2010', '2016', '2011', '2007', '2012', '2013', '2009', '2015', '2017', '2006'],  ['CocoaPerc', '0.72', '1.', '0.8', '0.74', '0.75', '0.7', '0.67', '0.63', '0.73', '0.68', '0.76', '0.64', '0.77', '0.78', '0.79',  '0.61',  '0.65',  '0.85',  '0.6',   '0.62',  '0.88',  '0.83',  '0.66',  '0.71',  '0.55',  '0.9', '0.58', '0.56', '0.99',  '0.84',  '0.69',  '0.89',  '0.82',  '0.81',  '0.91',  '0.57',  '0.86',  '0.87',  '0.42',  '0.46',  '0.53', '0.5'],  ['CoLocation', '0', '1', '2', '3', '4', '5', '6',],  ['Rating', '2.5', '1.', '3.', '3.75', '4.', '2.75', '3.5','3.25', '2.25', '2.', '1.5',  '1.75', '5.'],  ['BeanType', '0', '12', '20', '4', '7', '16', '2', '6', '8', '9', '10', '14', '17', '19',  '1',  '3', '11', '13', '18',  '5', '15'],  ['BeanOrigin', '5', '0', '3', '1', '2', '4]']]  
# name of csv file  
filename = "BeckyMatthewsPeaseOutput1.csv" 
# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
    # writing the data rows  
    csvwriter.writerows(rows) 
    
###Write file to Excel containing averages: 
fields = ['Averages for Chocoate Rating Variables']  
rows = ['BeanOrigin', '0', '3.068868', '1', '3.500000', '2', '3.472222', '3', '3.583333', '4', '3.241541', '5', '3.500000', '6', '1.750000', '7', '3.231760', '8', '3.250000', '9', '3.450000', '10', '3.375000', '11', '3.583333', '12', '3.091615', '13', '3.750000', '14', '2.976190', '15', '3.375000', '16', '3.241379', '17', '3.531250', '18', '3.291667', '19', '3.092105', '20', '3.217778'],  ['BeanType', '0', '3.040000', '1', '3.210526', '2', '3.349057', '3', '3.214038', '4', '3.191176', '5', '3.172810', '6', '3.119128'],  ['Year', '2006', '3.125000', '2007', '3.162338', '2008', '2.994624', '2009', '3.073171', '2010', '3.148649', '2011', '3.256061', '2012', '3.178205', '2013', '3.197011', '2014', '3.189271', '2015', '3.246491', '2016', '3.226027', '2017', '3.312500'],  ['CocoaPerc', '0.42', '2.750000', '0.46', '2.750000', '0.50', '3.750000', '0.53', '2.000000', '0.55', '2.859375', '0.56', '3.250000', '0.57', '2.750000', '0.58', '3.125000', '0.60', '3.005814', '0.61', '3.000000', '0.62', '2.964286', '0.63', '3.604167', '0.64', '3.191176', '0.65', '3.169872', '0.66', '3.380435', '0.67', '3.351852','0.68', '3.287234','0.69', '3.500000','0.70', '3.276042', '0.71', '3.088710', '0.72 ', '3.190476', '0.73 ', '3.136364', '0.74', '3.230769', '0.75 ', '3.177928', '0.76 ', '2.945652', '0.77', '3.060606', '0.78', '3.338235','0.79', '3.000000','0.80', '3.027778', '0.81', '2.850000', '0.82', '3.058824','0.83', '2.937500', '0.84', '2.812500', '0.85', '2.986111', '0.86', '3.250000', '0.87', '3.250000', '0.88', '3.218750', '0.89', '2.625000', '0.90', '2.968750', '0.91', '2.166667', '0.99', '2.625000', '1.00', '2.250000']
filename = "BeckyMatthewsPeaseOutput2.csv" 
with open(filename, 'w') as csvfile:    
    csvwriter = csv.writer(csvfile)   
    csvwriter.writerow(fields)   
    csvwriter.writerows(rows)     
    