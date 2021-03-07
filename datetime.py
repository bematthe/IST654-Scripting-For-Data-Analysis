# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:10:58 2020

@author: becky
"""
import calendar
import datetime
#Current Date and Time
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#Current Year
print("Current year: ", datetime.date.today().strftime("%Y"))

#Current Month of Year
print("Month of year: ", datetime.date.today().strftime("%B"))

#Current Week Number
import datetime
datetime.date(2020, 10, 28).isocalendar()[1]


4	print("Current year: ", datetime.date.today().strftime("%Y"))



#Namr of Day of the Week
import datetime 
import calendar 
  
def findDay(date): 
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[born]) 

date = '28 10 2020'
print(findDay(date)) 


Approach #2 : Using strftime() method

The strftime() method takes one or more format codes as an argument and returns a formatted string based on it. Here we will pass the directive “%A” in the method which provides Full weekday name for the given date.
filter_none
edit
play_arrow
brightness_4
# Python program to Find day of  
# the week for a given date 
import datetime  
from datetime import date 
import calendar 
  
def findDay(date): 
    day, month, year = (int(i) for i in date.split(' '))     
    born = datetime.date(year, month, day) 
    return born.strftime("%A") 
  
# Driver program 
date = '03 02 2019'
print(findDay(date)) 
Output:


 
Approach #3 : By finding day number
In this approach, we find the day number using calender module and then find the correspoding week day.
filter_none
edit
play_arrow
brightness_4
# Python program to Find day of  
# the week for a given date 
import calendar 
def findDay(date): 
    day, month, year = (int(i) for i in date.split(' '))     
    dayNumber = calendar.weekday(year, month, day) 
    days =["Monday", "Tuesday", "Wednesday", "Thursday", 
                         "Friday", "Saturday", "Sunday"] 
    return (days[dayNumber]) 
# Driver program 
date = '03 02 2019'
print(findDay(date)) 
Output:


    