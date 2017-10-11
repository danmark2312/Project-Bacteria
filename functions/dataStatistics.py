# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 02:18:33 2017

This function calculates one of the following statistics of the data

Mean Temperature
Mean Growth rate
Std Temperature
Std Growth rate
Rows
Mean Cold Growth rate
Mean Hot Growth rate

INPUT: 
    data: Same as in main.py
    statistic: String, equal to one of the above
    
OUTPUT:
    result: Float, the result of the specified statistic

USAGE:
    result = dataStatistics(data,statistic)
    

@author: Simon Moe Sørensen, moe.simon@gmail.com
"""
import numpy as np

def dataStatistics(data,statistic):
    
    #Define initial strings
    strings=["Mean Temperature","Mean Growth rate","Std Temperature","Std Growth rate","Rows","Mean Cold Growth rate","Mean Hot Growth rate"]
    
    #Compute statistic by checking the input value
    if len(data) == 0:
        print("Data array is 0, check filters")
        
    elif strings[0]==statistic:
        result = np.mean(data[:,0])
    
    elif strings[1]==statistic:
        result = np.mean(data[:,1])
    
    elif strings[2]==statistic:
        result = np.std(data[:,1])
        
    elif strings[3]==statistic:
        result = np.std(data[:,0])
    
    elif strings[4]==statistic:
        result = np.size(data,axis=0)
        
    elif strings[5]==statistic:
        data = data[data[:,0]<20]
        if len(data!=0):
            result = np.std(data[:,1])
        else:
            result = "No data under 20 Degrees Celsius"
    
    elif strings[6]==statistic:
        data = data[data[:,0]>50]
        if len(data!=0):
            result = np.std(data[:,1])
        else:
            result = "No data over 50 Degrees Celsius"
    
    else:
        result = "Invalid statistic, please try again"
    
    return result