# -*- coding: utf-8 -*-
"""
##Becky Matthews-Pease
##IST 652: Scripting for Data Analysis
##Lab 02, Week 04
"""

##Dictionaries:
stock = {"banana":6,"apple":0,"orange":32,"pear":15}
prices = {"banana":4,"apple":2,"orange":1.5,"pear":3}


##Part A:
stock["orange"]
##Output = 32
stock["cherry"] = 14
print(stock)
##Output = {'banana': 6, 'apple': 0, 'orange': 32, 'pear': 15, 'cherry': 14}


##Part B:
for item in stock:
    print(stock)
##Output = {'banana': 6, 'apple': 0, 'orange': 32, 'pear': 15, 'cherry': 14}
    
    
##Part C:
groceries = ['apple', 'banana', 'pear']

instock = 0
for fruit in stock:
    if fruit in groceries:
        instock += stock[fruit]
print(instock)
##Output = 21


##Part D:
inventory = lambda dct_1, dct_2: {key: int(dct_2[key]) * int(dct_1[key]) for key in dct_2}
inventory(stock, prices)
#Output = {'banana': 24, 'apple': 0, 'orange': 32, 'pear': 45}


