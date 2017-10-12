# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 23:13:59 2017

This function loads data from a datafile into an n*3 numpy matrix
If some requirements are not met in the datafile it skips that line
and outputs where the error was

INPUT:
    filename: String, name of datafile

OUTPUT:
    data: A filtered n*3 numpy matrix of type:
          [float, float, string]

          Where the first float is temperature, second float is the growth rate
          and string is the bacteria name

USAGE:
    data = dataLoad(filename)

@author: Simon Moe Sørensen, moe.simon@gmail.com
"""
import csv
from functions.userinput import inputStr


def dataLoad(filename):
    #Initial variables

    bacName1 = "Salmonella enterica"
    bacName2 = "Bacillus cereus"
    bacName3 = "Listeria"
    bacName4 = "Brochothrix thermosphacta"

    #Loading the collumns with row-values
    datafile = []

    while True:
        try:
            #Check if the user wants to exit
            if filename == "exit":
                break

            with open(filename, newline='') as inputfile:
                for row in csv.reader(inputfile):
                    datafile.append(row)
            break
        except FileNotFoundError:
            print("")
            print("File not found, please enter a valid datafile name")
            filename = inputStr("Please enter the name of your datafile: ")

            continue

    import numpy as np

    data = np.array([[0,0,0]])

    for i in range(len(datafile)):
        #Clean up the row and create list of strings
        rowStr = str(datafile[i])
        rowStr = rowStr.replace("']","")
        rowStr = rowStr.replace("['","")
        rowStr = rowStr.split()

        #Checks if the row has 3 collumns
        if len(rowStr)<3:
            print("Erroneous line, ValueError at line",i+1,"skipping...")
            continue

        #Check if row is within the specified conditions
        while True:
            try:
                #Temp
                if not 10<float(rowStr[0])<60:
                    print("Erroneous line, ValueError at line",i+1,"skipping...")
                    skip = True
                    break

                #Growth
                elif not float(rowStr[1])>0:
                    print("Erroneous line, ValueError at line",i+1,"skipping...")
                    skip = True
                    break

                #Bacteria
                elif not 0<int(rowStr[2])<=4:
                    print("Erroneous line, ValueError at line",i+1,"skipping...")
                    skip = True
                    break

                skip = False
                break
            except ValueError:
                print("Erroneous line, ValueError at line",i+1,"skipping...")
                skip = True
                break

        #Skip if Error
        if skip == True:
            skip = False
            continue

        #Initial values
        temp = float(rowStr[0])
        growth = float(rowStr[1])
        bacInt = int(rowStr[2])

        #Assigning bacteria names
        if bacInt == 1:
            bacStr = bacName1

        elif bacInt ==2:
            bacStr = bacName2

        elif bacInt ==3:
            bacStr = bacName3

        elif bacInt ==4:
            bacStr = bacName4

        #Create arrray of the row values
        row = np.array([temp,growth,bacStr],dtype=object)

        #Stack in an n*3 matrix
        data = np.vstack((data,row))

    #Remove initial values
    data = np.delete(data,0,0)

    return data
