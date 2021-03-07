# -*- coding: utf-8 -*-
"""
Becky Matthews-Pease
Lab 03
Scripting for Data Analysis
"""

##Problem 1: Write a Python function to multiply all the numbers in a list.

import numpy

setOne = (8, 2, 3, -1, 7)
setTwo = (6, 9, 10, 3, 7)
setThr = (7, 8, 13, 6, 2)

resultOne = numpy.prod(setOne)
resultTwo = numpy.prod(setTwo)
resultThr = numpy.prod(setThr)

print(resultOne)
print(resultTwo)
print(resultThr)

##Output = 
        ## -336
        ## 11340
        ## 8736


##Problem 2: Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
    #Sentance 1 = I'm Literally Grasping at Straws
    #Sentence 2 = Winston, PLEASE stop licking the couch!
    
sent = input("Enter Phrase:")
upperC = 0
lowerC = 0
for x in sent:
      if(x.isupper()):
            upperC = upperC + 1
      elif(x.islower()):
            lowerC = lowerC + 1
print(upperC)
print(lowerC)

##Output = 
    ##4
    ##23
        #and
    ##7
    ##25


