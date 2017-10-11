# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 02:35:15 2017

This function plots the filtered or non-filtered data into a
bar plot and a line plot with multiple lines, with legends

INPUT:
    data: Same numpy matrix type as in main.py
    
OUTPUT:
    bar and line-plot
    
    CAUTION: if generated datafile is used, the line-plot will not be
        representative of the real-world data.
        
USAGE:
    dataPlot(data)

@author: Simon Moe Sørensen, moe.simon@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt

def dataPlot(data):
    #Initial values
    sal = "Salmonella enterica"
    bac = "Bacillus cereus"
    lis = "Listeria"
    bro = "Brochothrix thermosphacta"
    
    #Plot 1
    
    x = np.arange(0,4,1)
    #Count occurences
    salSize = np.size(data[data==sal])
    lisSize = np.size(data[data==lis])
    bacSize = np.size(data[data==bac])
    broSize = np.size(data[data==bro])
    
    xticks = ("Salmonella enterica","Bacillus cereus","Listeria","Brochothrix thermosphacta")
    plt.xticks(x,xticks,rotation=35)
    y = (salSize,bacSize,lisSize,broSize)
    
    plt.bar(x,y)
    plt.title("Number of bacteria")
    plt.xlabel("Type of bacteria")
    plt.ylabel("Amount of bacteria")
    plt.show()
    
    #clear
    plt.clf()
    
    #Plot 2
    
    dataBackup = np.copy(data)
    
    #Graph for Salmonella enterica
    
    #Get rows where it is equal to string
    data = dataBackup[dataBackup[:,2]==sal]
    
    if len(data) > 0:

        #Sort temperature (x) axis
        data = data[np.lexsort((data[:, 0], ))]        
        
        #Make graph
        xsal = data[:,0]
        ysal = data[:,1]
        
        #If plot or line
        if np.size(xsal)>1:
            plt.plot(xsal,ysal,ls="-",c="r",label=sal)
        else:
            plt.plot(xsal,ysal,marker=".",c="r",label=sal,ms=15)
        
        plt.legend()
    
    #Graph for Listeria
    
    #Get rows where it is equal to string
    data = dataBackup[dataBackup[:,2]==lis]

    if len(data) > 0:
        
        #Sort temperature (x) axis
        data = data[np.lexsort((data[:, 0], ))]
        
        #Make graph
        xlis = data[:,0]
        ylis = data[:,1]
        
        #If plot or line
        if np.size(xlis)>1:
            plt.plot(xlis,ylis,ls="-",c="g",label=lis)
        else:
            plt.plot(xlis,ylis,marker=".",c="g",label=lis,ms=15)
            
        plt.legend()
    
    #Graph for Bacillus cereus
    
    #Get rows where it is equal to string
    data = dataBackup[dataBackup[:,2]==bac]
    
    if len(data) > 0:
        
        #Sort temperature (x) axis
        data = data[np.lexsort((data[:, 0], ))]
        
        #Make graph
        xbac = data[:,0]
        ybac = data[:,1]
        
        #If plot or line
        if np.size(xbac)>1:
            plt.plot(xbac,ybac,ls="-",c="b",label=bac)
        else:
            plt.plot(xbac,ybac,marker=".",c="b",label=bac,ms=15)
        
        plt.legend()
    
    #Graph for Brochothrix thermosphacta
    
    #Get rows where it is equal to string
    data = dataBackup[dataBackup[:,2]==bro]
    
    if len(data) > 0:
        
        #Sort temperature (x) axis
        data = data[np.lexsort((data[:, 0], ))]        
        
        #Make graph
        xbro = data[:,0]
        ybro = data[:,1]
        
        #If plot or line
        if np.size(xbro)>1:
            plt.plot(xbro,ybro,ls="-",c="y",label=bro)
        else:
            plt.plot(xbro,ybro,marker=".",c="y",label=bro,ms=15)
            
        plt.legend(loc=2)
    
    #Set plot limits
    plt.xlim([10,60])
    plt.ylim(ymin=0)
    plt.grid()
    plt.title("Growth rate by temperature")
    plt.ylabel("Growth rate")
    plt.xlabel("Temperature")
    plt.show()
    