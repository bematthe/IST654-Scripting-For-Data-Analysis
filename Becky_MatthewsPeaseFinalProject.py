# -*- coding: utf-8 -*-
##Becky Matthews-Pease
##IST 652: Scripting for Data Analysis
#Homework 01
 
##################Libraries#####################################
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

###############Import Data######################################
data = pd.read_csv("C:\\Users\\becky\\Desktop\\choc.csv")

###############Exploring the Data###############################
type(data)  #pandas.core.frame.DataFrame
print(data.columns) #Index(['I.D', 'Company', 'Bar Name', 'Year', 'CocoaPercent', 'CompanyLocation','CompanyContinent', 'Rating', 'Bean\nType', 'Style','BeanMainContinent', 'BeanSecondContinent', 'BeanThirdContinent','BeanOrigin', 'BeanSecondCountry', 'BeanThirdCountry', 'Rating2','Description'], dtype='object')
total_rows = data.count
print(total_rows) #[1795 rows x 6 columns]>

#Get Unique Values from each column
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
for col in data:
    print(data['BeanType'].value_counts())
for col in data:
    print(data['BeanOrigin'].value_counts())
for col in data:
    print(data['BeanMainContinent'].value_counts()) 
for col in data:
    print(data['CoLocation'].value_counts())
for col in data:
    print(data['CoContinent'].value_counts())      
for col in data:
    print(data['Year'].value_counts())    
for col in data:
    print(data['Rating'].value_counts())     
    
##############Histograms########################################
#Histogram of Ratings
x = data["Rating"]
plt.hist(x, bins = 13, color = "orchid")
plt.title("Distribution of Ratings")
plt.show()

#Histogram of Cocoa Content
x = data['CocoaPerc']
plt.xticks(rotation='vertical')
plt.hist(x, bins = 10, color = "palevioletred")
plt.title("Distribution of Cocoa Percentage")
plt.show()

#Histogram of Types of Beans
x = data["BeanType"]
plt.xticks(rotation='vertical')
plt.hist(x, bins = 21, color = "dodgerblue")
plt.title("Distribution of Bean Types")
plt.show()

#Histogram of General Bean Types
x = data["BeanTypeSum"]
plt.hist(x, bins = 9, color = "m")
plt.xticks(rotation='vertical')
plt.title("Distribution of General Bean Type")
plt.show()

#Histogram of HQs-Country
x = data["CoLocation"]
plt.xticks(rotation='vertical')
plt.hist(x, bins = 10, color = "cadetblue") 
plt.title("Distribution of Company Location (Country)")
plt.show()

#Histogram of Bean Origins-Country
x = data["BeanOrigin"]
plt.xticks(rotation='vertical')
plt.hist(x, bins = 20, color = "darkcyan") 
plt.title("Distribution of Bean Origin (Country)")
plt.show()

#Histogram of Bean Origins-Continent
x = data["BeanMainContinent"]
plt.xticks(rotation='vertical')
plt.hist(x, bins = 6, color = "darkcyan") 
plt.title("Distribution of Bean Origin (Continent)")
plt.show()

#Rating Distribution By Year
x = data["Rating"]
y = data["Year"]
plt.hist2d(x, y, bins=10, cmap='Blues')
cb = plt.colorbar()
plt.title("Distribution of Ratings By Year")
cb.set_label('counts in bin')

##############Averages##########################################
#Averages
origin = data.groupby('BeanOrigin')['Rating'].mean()
originC = data.groupby('BeanMainContinent')['Rating'].mean()
bType = data.groupby('BeanType')['Rating'].mean()
bTypeSum = data.groupby('BeanTypeSum')['Rating'].mean()
colocation = data.groupby('CoLocation')['Rating'].mean() 
coContinent = data.groupby('CoContinent')['Rating'].mean() 
bYear = data.groupby('Year')['Rating'].mean() 
cPerc = data.groupby('CocoaPerc')['Rating'].mean() 
print(origin)
print(originC)
print(bType)
print(bTypeSum)
print(colocation)
print(coContinent)
print(bYear)
print(cPerc)

#Average Rating by Bean Continent Origin
beanSource = ("NotDisclosed", "Africa", "Asia", "NorthAmerica", "Oceania", "SouthAmerica")
averageRating = (2.945652, 3.163488, 3.163793, 3.203467, 3.245000, 3.191988)
plt.ylim(2.8, 3.3)
plt.bar(beanSource,averageRating, color = "violet")
plt.ylabel('Rating')
plt.title('Average Ratings by Bean Origin')
plt.xticks(rotation='vertical')
plt.show()
#Average Rating by Company Continental Location
companyLocation = ("Africa", "Asia", "Europe", "NorthAmerica", "Oceania", "SouthAmerica")
averageRating = (3.008333, 3.160714, 3.217655, 3.183131, 3.286517, 3.097682)
plt.ylim(3.0, 3.3)
plt.bar(companyLocation,averageRating, color = "palevioletred")
plt.ylabel('Rating')
plt.title('Average Ratings by Company Location')
plt.xticks(rotation='vertical')
plt.show()

#Average Rating by Summary Bean Type
beanSumType = ("Amazon", "Blends", "Criollo", "Forastero", "Hybrid", "Nacional", "Trinitario", "Other", "Undisclosed")
averageRating = (3.231579, 3.159889, 3.204698, 3.096053, 3.174689, 3.274306, 3.223529, 3.183790, 3.225000)
plt.ylim(3.0, 3.3)
plt.bar(beanSumType,averageRating, color = "chocolate")
plt.ylabel('Rating')
plt.title('Average Ratings by Bean Type')
plt.xticks(rotation='vertical')
plt.show()

#Average Rating by Continental Bean Source v. Company Continental Location
barWidth = 0.40
bars1 = [2.945652, 3.163488, 3.163793, 0.0, 3.203467, 3.245000, 3.191988]
bars2 = [0.0, 3.008333, 3.160714, 3.217655, 3.183131, 3.286517, 3.097682]
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
# Make the plot
plt.bar(r1, bars1, color='lightsalmon', width=barWidth, edgecolor='white', label='Company Location')
plt.bar(r2, bars2, color='orchid', width=barWidth, edgecolor='white', label='Bean Origin')
plt.ylim(2.9, 3.3)
# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ["Undisclosed", "Africa", "Asia", "Europe", "NorthAmerica", "Oceania", "SouthAmerica"])
plt.xticks(rotation='vertical')
plt.title('Average Ratings by Company Location v. Bean Origin')
# Create legend & Show graphic
plt.legend()
plt.show()

###############BoxPlots#########################################
OriginX = sns.boxplot(x = "BeanOrigin", y = "Rating", data = data)
OriginX.set_xticklabels(OriginX.get_xticklabels(),rotation=90)
print(OriginX)

OriginCx = sns.boxplot(x="BeanMainContinent", y="Rating", data=data, palette="Set3")
OriginCx.set_xticklabels(OriginCx.get_xticklabels(),rotation=30)
print(OriginCx)

bTypeX = sns.boxplot(x="BeanType", y="Rating", data=data)
bTypeX.set_xticklabels(bTypeX.get_xticklabels(),rotation=90)
print(bTypeX)

bTypeSumX = sns.boxplot(x="BeanTypeSum", y="Rating", data=data)
bTypeSumX.set_xticklabels(bTypeSumX.get_xticklabels(),rotation=40)
print(bTypeSumX)

colocationX = sns.boxplot(x="CoLocation", y="Rating", data=data)
colocationX.set_xticklabels(colocationX.get_xticklabels(),rotation=90)
print(colocationX)

coContinent = sns.boxplot(x="CoContinent", y="Rating", data=data)
coContinent.set_xticklabels(coContinent.get_xticklabels(),rotation=40)
print(coContinent)

bYear = sns.boxplot(x="Year", y="Rating", data=data)
bYear.set_xticklabels(bYear.get_xticklabels(),rotation=40)
print(bYear)

cPerc = sns.boxplot(x="CocoaPerc", y="Rating", data=data)
cPerc.set_xticklabels(cPerc.get_xticklabels(),rotation=90)
print(cPerc)

##############Scatterplots###################################### 
#Rating v Cocoa Percentage
sns.catplot(x="CocoaPerc", y="Rating", data=data)
#Rating by Bean Origin (Country)
sns.catplot(x="BeanOrigin", y="Rating", data=data)
frst.set_xticklabels(rotation=90)
#Rating by Bean Origin (Continent)
sns.catplot(x="BeanMainContinent", y="Rating", data=data)
s.set_xticklabels(rotation=90)
#Rating by Bean Origin (Continent)
sns.catplot(x="BeanMainContinent", y="Rating", kind="boxen",
            data=data.sort_values("BeanTypeSum"))
#Rating by Company Country
g = sns.catplot(x="CoLocation", y="Rating", data=data)
g.set_xticklabels(rotation=90)
#Rating by Company Country
sns.catplot(x="CoLocation", y="Rating", kind="boxen",
            data=data.sort_values("BeanTypeSum"))
#Rating by Specific Bean Type
h = sns.catplot(x="BeanType", y="Rating", data=data)
h.set_xticklabels(rotation=90)
#Rating by General Bean Type
i = sns.catplot(x="BeanTypeSum", y="Rating", data=data)
i.set_xticklabels(rotation=90)

#Bar Rating By Cocoa Percentage and Bean Continent Origin
# Use the 'hue' argument to provide a factor variable
trio = sns.lmplot( x="CocoaPerc", y="Rating", data=data, fit_reg=False, hue="BeanMainContinent", legend=False)
# Move the legend to an empty part of the plot
plt.legend(loc='lower right')
sns.plt.show()

##############Linear Regression#################################
datan = pd.read_csv("C:\\Users\\becky\\Desktop\\chocn.csv")
model_lin = sm.OLS.from_formula("Rating ~ CocoaPerc + Year + CoLocation + CoContinent + BeanContinent + BeanType + BeanTypeSum + BeanOrigin", data=datan)
result_lin = model_lin.fit()
result_lin.summary()

model_lin = sm.OLS.from_formula("Rating ~ CocoaPerc + CoContinent + BeanContinent + BeanTypeSum", data=datan)
result_lin = model_lin.fit()
result_lin.summary()

model_lin = sm.OLS.from_formula("BeanTypeSum ~ Rating", data=datan)
result_lin = model_lin.fit()
result_lin.summary()
#.262
model_lin = sm.OLS.from_formula("BeanOrigin ~ Rating", data=datan)
result_lin = model_lin.fit()
result_lin.summary()
#.389
model_lin = sm.OLS.from_formula("BeanContinent ~ Rating", data=datan)
result_lin = model_lin.fit()
result_lin.summary()
#.354
model_lin = sm.OLS.from_formula("CoLocation ~ Rating", data=datan)
result_lin = model_lin.fit()
result_lin.summary()
#.323 
model_lin = sm.OLS.from_formula("CoContinent ~ Rating", data=datan)
result_lin = model_lin.fit()
result_lin.summary()
#.378


########Coca Content of bars with beans from most highly ranked source and lowest ranked source###########
###What are the Cocoa Content Percentages for Bars made from Beans Sourced from Africa?######
source = data[data.BeanMainContinent == "Africa"]
Content = source['CocoaPerc']
np.array(Content)
ContentList = Content.unique()
ContentList.sort()
print(ContentList)

####What are the Cocoa Content Percentages for Bars made from Beans Sourced from Oceania?####
source = data[data.BeanMainContinent == "Oceania"]
Content = source['CocoaPerc']
np.array(Content)
ContentList = Content.unique()
ContentList.sort()
print(ContentList)


################Bars Sourced Locally############################
###What companies are located in the same country from which their beans are sourced?######
def find_value_column(row):
    return row.CoLocation in row.BeanOrigin
data[data.apply(find_value_column, axis=1)][['CoLocation', 'BeanOrigin']]
newdata = data[data.apply(find_value_column, axis=1)][['CoLocation', 'BeanOrigin', 'Rating']]

#Mean and Median of Local Company/Source
origin = newdata.groupby('BeanOrigin')['Rating'].median()
print(origin)
newdata["Rating"].describe()
newdata["Rating"].median()

#Averages of 'locally sourced' bars by continent
AfricaAve = newdata[data.BeanMainContinent == "Africa"].mean()
AsiaAve = newdata[data.BeanMainContinent == "Asia"].mean()
NAmericaAve = newdata[data.BeanMainContinent == "North America"].mean()
SAmericaAve = newdata[data.BeanMainContinent == "South America"].mean()
OceaniaAve = newdata[data.BeanMainContinent == "Oceania"].mean()

##############Africa and Oceania#################################
###Creates data frame only including entries with a bean source from Oceania
Oceania = data[data.BeanMainContinent == "Oceania"]

#Returns Average Rating by bean type for Oceania sourced beans
Oceania.groupby('BeanType')['Rating'].mean()
Oceania.groupby('BeanTypeSum')['Rating'].mean()


###Creates data frame only including entries with a bean source from Africa
Africa = data[data.BeanMainContinent == "Africa"]

#Returns Average Rating by bean type for Oceania sourced beans
Africa.groupby('BeanType')['Rating'].mean()
Africa.groupby('BeanTypeSum')['Rating'].mean()


##############Output Files######################################
###Write file to Excel containing averages:  
origin.to_csv('AveRatingsByBeanOriginCountry.csv')  
bType.to_csv('AveragebyBeanType.csv')    
colocation.to_csv('AveragebyCompanyLocation.csv')  
cPerc.to_csv('AveragebyCocoaPercentage.csv')    





