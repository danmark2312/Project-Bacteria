# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:32:06 2017

Purely for test-purposes. Generates a datafile of the specified type for the
project.

Input:
    None

Output:
    A generated datafile in the folder of the script
    
USAGE:
    genData()

@author: Simon Moe Sørensen, moe.simon@gmail.com
"""

from functions.userinput import inputNumber
import random

def genData():

    print("=================================================================================")
    print("This script generates a file with erroneous lines for the project exercise")
    print("=================================================================================")
    print("")
    
    l = int(inputNumber("Enter the amount of lines you want: "))
    
    #create file
    f = open("datafile","w")
    
    #Initial variable
    j=1
    
    #Write l, amount of lines
    for i in range(l):
        temp = random.randint(10,59) #Error of total 1 out of 50
        growth = round(random.uniform(-0.005,1.8),3) #Error of 0.005 out of 1.805
        bacteria = random.randint(1,4) #Error of 0 out of 4
        
        #Every 25'th line we get an invalid bacteria, 0     
        if i-1 == 25*j:
            bacteria = 0
            j = j+1
        
        #Write into a line
        f.write("{} {} {}".format(temp,growth,bacteria))
        f.write("\n")
        
