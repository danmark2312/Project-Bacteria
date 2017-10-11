#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 09:13:07 2017

This function filters the data with respect to the defined filters.
It can remove and add filters depending on their presence in the filters-
variable.

INPUT:
    filters: String, separated by commas and a space ", "
    bacteria: String, The bacteria which needs to be added or removed
    dataBackup: n*3 numpy matrix, the raw datafile

OUTPUT:
    filters: String, separated by commas and a space ", "
    data: A filtered n*3 numpy matrix of type:
          [int, float, string]
          
          Where the integer is temperature, float is the growth rate and string
          is the bacteria
    
USAGE:
    filters = filterData(filters,bacteria,dataBackup)[0]
    data = filterData(filters,bacteria,dataBackup)[1]
    
    Or
    
    filters,data = filterData(filters,bacteria,dataBackup)

@author: Simon Moe Sørensen, moe.simon@gmail.com
"""
import numpy as np

def filterData(filters,bacteria,dataBackup):    
    
    #Check if bacteria is not a filter
    if not bacteria in filters:
        filters = ", ".join((bacteria,filters))
        
        #Check for no filter message and remove it 
        if filters[len(filters)-22:len(filters)] == "//No bacteria filter//":
            filters = filters[:len(filters)-24]
        
        #Separate filter-data into list of strings
        filtersDat = filters.split(", ")
        
        #Filtering code
        #Initial variable
        dataDummy = [0,0,0]
        
        #Loop that runs through the core-data (dataBackup)
        #and filters the data from "filtersDat" an i amount of times,
        #depending on how many filters there are in filtersDat
        #It stacks the different results into one "data" variable
        for i in range(len(filtersDat)):
            dataStack = dataBackup[dataBackup[:,2]==filtersDat[i]]
            
            dataDummy = np.vstack((dataStack,dataDummy))
        
        #Remove placeholder / dummy
        data = dataDummy[0:len(dataDummy)-1]
        
        
        print("")
        print(bacteria,"has now been added as a filter")
        
    #Else, bacteria must be in the filter
    else:
        #Remove filter from string of filters
        
        #See if the bacteria is after a comma
        #i.e filters: Bacillus cereus, Salmonella enterica
        #Where salmonella is after a comma
        if filters[filters.index(bacteria)-2] == ",":
            pos1 = filters.index(bacteria)-2
        
        #Else it must be in the beginning of the string, therefore the
        #bacteria starts at position 0
        else:
            pos1 = 0
        
        #Redefine filters from beginning to the start of the bacteria
        #there is to be removed. And then skip, from the start of
        #the bacteria, to the end of the bacteria + 2, because
        #we want to remove the following comma and space as well
        filters = filters[:pos1] + filters[(pos1+2+len(bacteria)):]
        
        #Reassign data with or without filter
        
        #Without filter
        if filters == "":
            data = dataBackup
            filters = "//No bacteria filter//"
            
        #With filter
        else:
            #Filter data
            filtersDat = filters.split(", ")
            
            #Filtering code
            #Initial variable
            dataDummy = [0,0,0]
            
            for i in range(len(filtersDat)):
                dataStack = dataBackup[dataBackup[:,2]==filtersDat[i]]
                
                #Stack data
                dataDummy = np.vstack((dataStack,dataDummy))
            
            #Redefine from placeholder and remove zero
            data = dataDummy[0:len(dataDummy)-1]
        
        print("")
        print(bacteria,"has now been removed as a filter")
        
    return filters,data