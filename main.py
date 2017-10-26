# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 03:50:28 2017

This is the main script of the project. It runs a couple of while loops to
create an interface for the user to navigate in. Each menu has the option
to go back or exit, if it is the main loop

At each interface it checks for filters and displays them. If only one filter
is present, it displays this and says there is no other filter

The main variables in this script are: isData, filters, data, rangeFilter
    lowerRange and upperRange

isData: Integer of 0 and 1. Decides if the "Load data" option has been
        selected, meaning data has been loaded

filters: String of bacteria, separated by commas and a space ", "
    If filters is empty, it is displayed as "//No bacteria filter//"

data: A (filtered) n*3 numpy matrix of type:
      [int, float, string]

      Where the integer is temperature, float is the growth rate and string
      is the bacteria

rangeFilter: String, either "Growth rate" or "Temperature"

lower- and upperRange: Float, the range that the rangeFilter is within


@author: Simon Moe Sørensen, moe.simon@gmail.com
"""

from functions.dataLoad import dataLoad
from functions.dataPlot import dataPlot
from functions.dataStatistics import dataStatistics
from functions.userinput import displayMenu,inputNumber,inputStr
from functions.filterData import filterData
from functions.datafileGenerator import genData

import numpy as np


#Initial variables
isData = 0
filters = "//No bacteria filter//"
upperRange = -1
lowerRange = -1
rangeFilter = "//No range filter//"

#Loop for menu

print("""
================================================
  Welcome to the Bacteria Data Analysis script

  Please choose one of the options below
================================================
      """)
print("Menu: ")

#Have the menu run until the user decides to leave
while True:
    print("")
    #Display filters
    if (filters != "//No bacteria filter//") or ((lowerRange and upperRange) != -1):
        print("""
====================================================================
Current filters:
    Bacteria: {}
    {} from {} to {}
====================================================================
                """.format(filters,rangeFilter,lowerRange,upperRange))

    menu = displayMenu(["Load data", "Filter data","Display statistics",
                        "Generate plots","Show current data","Generate datafile","Quit"])

    if menu == 1:
        print("")
        print("""Type "exit" to exit""")
        datafile = inputStr("Please enter the name of your datafile (with extension, if any): ")

        
        #Check for valid filename and exit condition
        while True:
            try:
                data = dataLoad(datafile)
                break
                
            except FileNotFoundError:
                
                if datafile == "exit":
                    break
                
                print("")
                print("File not found, please enter a valid datafile name")
                datafile = inputStr("Please enter the name of your datafile: ")
                
                
        if datafile != "exit":      
            
            #Backup of data
            dataBackup = data
    
            #Set data as loaded
            isData = 1
    
            #See if we already have filters
            #We do this in case of the user loading a new datafile, while having filters specified
            if (filters != "//No bacteria filter//") or ((lowerRange and upperRange) != -1):
    
                #See filterData.py for full comments
                #Filters of bacteria
                if filters != "//No bacteria filter//":
    
                    filtersDat = filters.split(", ")
    
                    dataDummy = [0,0,0]
    
                    for i in range(len(filtersDat)):
                        dataStack = dataBackup[dataBackup[:,2]==filtersDat[i]]
    
                        #Stack data
                        dataDummy = np.vstack((dataStack,dataDummy))
    
                    #Redefine from placeholder and remove zero
                    data = dataDummy[0:len(dataDummy)-1]
    
                #No bacteria filters
                else:
                    data = dataBackup
    
    
                #Apply range filters
                if upperRange and lowerRange != -1:
                    if rangeFilter == "Growth Rate" :
                        data = data[data[:,1]>=lowerRange]
                        data = data[data[:,1]<=upperRange]
    
                    if rangeFilter == "Temperature" :
                        data = data[data[:,0]>=lowerRange]
                        data = data[data[:,0]<=upperRange]
    
                print("Data loaded succesfully, with filters")
    
            else:
                print("")
                print("Data loaded succesfully")

    #Filter data
    elif menu == 2:

        while True:
            #Check if we have loaded data
            if isData == 0:
                print("")
                print("Please load data first")
                break

            #Display filters again
            if (filters != "//No bacteria filter//") or ((lowerRange and upperRange) != -1):
                print("""
====================================================================
Current filters:
    Bacteria: {}
    {} from {} to {}
====================================================================
                """.format(filters,rangeFilter,lowerRange,upperRange))

            print("")
            print("Please choose a filter: ")
            menu2 = displayMenu(["Bacteria type","Range","Back"])

            #Bacteria names
            sal = "Salmonella enterica"
            bac = "Bacillus cereus"
            lis = "Listeria"
            bro = "Brochothrix thermosphacta"

            strArr = [sal,bac,lis,bro]


            #User chose bacteria filter
            if menu2 == 1:

                #Print instructions
                print("""
=======================================================
Please choose a bacteria to act as a filter. If the
chosen bacteria is already a filter it will be removed.
=======================================================
                      """)

                while True:

                    #Display filters
                    if (filters != "//No bacteria filter//") or ((lowerRange and upperRange) != -1):
                        print("""
====================================================================
Current filters:
    Bacteria: {}
    {} from {} to {}
====================================================================
                """.format(filters,rangeFilter,lowerRange,upperRange))

                    #Get the bacteria to act as a filter
                    menu3 = displayMenu([sal,bac,lis,bro,"Back"])

                    #Salmonella enterica
                    if menu3 == 1:
                        filters,data = filterData(filters,sal,dataBackup)

                    #Bacillus cereus
                    if menu3 == 2:
                        filters,data = filterData(filters,bac,dataBackup)

                    #Listeria
                    if menu3 == 3:
                        filters,data = filterData(filters,lis,dataBackup)

                    #Brochothrix thermosphacta
                    if menu3 == 4:
                        filters,data = filterData(filters,bro,dataBackup)

                    #Back
                    if menu3 == 5:
                        break

                    #Filter data with ranges as well
                    if upperRange and lowerRange != -1:
                        if rangeFilter == "Growth Rate" :
                            data = data[data[:,1]>=lowerRange]
                            data = data[data[:,1]<=upperRange]

                        if rangeFilter == "Temperature" :
                            data = data[data[:,0]>=lowerRange]
                            data = data[data[:,0]<=upperRange]

                    print("")

            #User chooses range filter
            if menu2 == 2:
                #Display filters
                if (filters != "//No bacteria filter//") or ((lowerRange and upperRange) != -1):
                    print("""
====================================================================
Current filters:
    Bacteria: {}
    {} from {} to {}
====================================================================
                """.format(filters,rangeFilter,lowerRange,upperRange))

                print("""
                      =======================================================
                      Please specify whether you want to range-filter
                      Growth Rate or Temperature
                      =======================================================
                      """)

                menu3 = displayMenu(["Growth Rate","Temperature","Clear range filter"])

                if menu3 == 1:
                    rangeFilter = "Growth Rate"

                elif menu3 == 2:
                    rangeFilter = "Temperature"



                #If user decides to go into a range filter, run the code
                if menu3 in [1,2]:

                    #Get the ranges specified by the user
                    #Also makes sure, that they fulfil the conditions
                    while True:
                        if rangeFilter == "Growth Rate":
                            range1 = inputNumber("Please enter the lower range: ")
                            range2 = inputNumber("Please enter the upper range: ")

                            if (range1 or range2) < 0:
                                print("")
                                print("Growth Rate can only be a positive number, please try again.")

                            else:
                                break

                        if rangeFilter == "Temperature":
                            range1 = inputNumber("Please enter the lower range: ")
                            range2 = inputNumber("Please enter the upper range: ")

                            if (range1 or range2) > 60:
                                print("Temperature can only be between 10 and 60, please try again.")

                            elif (range1 or range2) < 10:
                                print("Temperature can only be between 10 and 60, please try again.")

                            else:
                                break



                    #Check if range is in wrong order
                    if range1>range2:
                        print("""
                        Detected a lower range that is higher than the upper range.
                        Switching ranges...
                        """)

                    #Define ranges, no matter the order
                    upperRange = max(range1,range2)
                    lowerRange = min(range1,range2)

                    #Filter the data with range
                    if upperRange and lowerRange != -1:
                        if rangeFilter == "Growth Rate":
                            data = data[data[:,1]>=lowerRange]
                            data = data[data[:,1]<=upperRange]

                        if rangeFilter == "Temperature":
                            data = data[data[:,0]>=lowerRange]
                            data = data[data[:,0]<=upperRange]



                #Clear ranges
                if menu3 == 3:
                    rangeFilter = "//No range filter//"
                    lowerRange = -1
                    upperRange = -1

                    #Check if we have filters of bacteria
                    #See filterData.py for full comments
                    if filters != "//No bacteria filter//":

                        filtersDat = filters.split(", ")

                        dataDummy = [0,0,0]

                        for i in range(len(filtersDat)):
                            dataStack = dataBackup[dataBackup[:,2]==filtersDat[i]]

                            #Stack data
                            dataDummy = np.vstack((dataStack,dataDummy))

                        #Redefine from placeholder and remove zero
                        data = dataDummy[0:len(dataDummy)-1]

                    #No filters
                    else:
                        data = dataBackup

                    print("")
                    print("Range-filter has been cleared")

            if menu2 == 3:
                break

    #Display statistics
    elif menu == 3:
        #Initial variable
        stat = "Statistic"
        result = "result"
        while True:
            #Check if we have loaded data
            if isData == 0:
                print("")
                print("Please load data first")
                break

            #Display filters
            if (filters != "//No bacteria filter//") or ((lowerRange and upperRange) != -1):
                print("""
====================================================================
Current filters:
    Bacteria: {}
    {} from {} to {}
====================================================================
                """.format(filters,rangeFilter,lowerRange,upperRange))

            print("""
===============================================================================
Please choose a statistic to display

{}  =  {}
===============================================================================
              """.format(stat,result))

            #Display a menu of statistics that the user can choose from
            menu2 = displayMenu(['Mean Temperature','Mean Growth rate','Std Temperature','Std Growth rate','Rows','Mean Cold Growth rate','Mean Hot Growth rate','Back'])
            print("")
            if menu2 == 1:
                result = dataStatistics(data,"Mean Temperature")
                stat = "Mean Temperature"

            elif menu2 == 2:
                result = dataStatistics(data,'Mean Growth rate')
                stat = 'Mean Growth rate'

            elif menu2 == 3:
                result = dataStatistics(data,'Std Temperature')
                stat = 'Std Temperature'

            elif menu2 == 4:
                result = dataStatistics(data,'Std Growth rate')
                stat = 'Std Growth rate'

            elif menu2 == 5:
                result = dataStatistics(data,'Rows')
                stat = 'Rows'

            elif menu2 == 6:
                result = dataStatistics(data,'Mean Cold Growth rate')
                stat = 'Mean Cold Growth rate'

            elif menu2 == 7:
                result = dataStatistics(data,'Mean Hot Growth rate')
                stat = 'Mean Hot Growth rate'

            elif menu2 == 8:
                break

    #Run dataPlot function
    elif menu == 4:
        while True:
            #Check if we have loaded data
            if isData == 0:
                print("")
                print("Please load data first")
                break

            #plot data with dataPlot function
            dataPlot(data)

            break


    #Show data, if user wants to see the data
    elif menu == 5:
        while True:
            #Check if we have loaded data
            if isData == 0:
                print("")
                print("Please load data first")
                break

            #Display filters
            if (filters != "//No bacteria filter//") or ((lowerRange and upperRange) != -1):
                print("""
====================================================================
Current filters:
    Bacteria: {}
    {} from {} to {}
====================================================================
                """.format(filters,rangeFilter,lowerRange,upperRange))

            print("")

            #Make sure to print everything, np.inf = numpy.infinity
            np.set_printoptions(threshold=np.inf)
            print(data)

            #Set print options back to normal
            np.set_printoptions(threshold=1000)

            break

    #Generate datafile
    elif menu == 6:

        #Run the datafile-generation script. Only for test-purposes
        genData()
        print("")
        print("""File with name "datafile" has now been generated""")

    elif menu == 7:
        break
