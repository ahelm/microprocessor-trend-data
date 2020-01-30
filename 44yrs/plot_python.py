#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:14:25 2020

@author: leonardo

python script to plot the data coming from ...

"""

import glob
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from functools import reduce

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
    
def listFileNameData(fileNameOS,columnName):
    """
    This function lists the file names in the project folder.
    It accept as input the name of the column you want to store
    """   
    a = {}
    index = 0
    #fileName
    for filename in glob.glob(fileNameOS):
        #print(os.path.splitext(filename)[0])
        key = os.path.splitext(filename)[0]
        #print(key)
        a[key] = index
        fileData = pd.read_csv(filename, skipinitialspace=True)
        a[key] = fileData[columnName]
        index += 1
    return a

def returnListValues(fileNameOS, columnName):
    """
    This function lists the file names in the project folder.
    It accept as input the name of the column you want to store
    """   
    a = []
    index = 0
    for filename in glob.glob(fileNameOS):
        fileData = pd.read_csv(filename, skipinitialspace=True)
        a = fileData[columnName]
        index += 1
    return a

def createListKey(seriePanda):
    dataList = []
    for key, value in seriePanda.items():
        # print(key)
        # print(value)
        dataList.append(key)
    return dataList

def createListValues(seriePanda):
    dataList = []
    for key, value in seriePanda.items():
        # print(key)
        # print(value)
        dataList.append(value)
    return dataList


if __name__ == "__main__":
    
    print("reading the data from the files into Panda's series")
    years_n_core_serie = returnListValues('cores.csv', 'year')
    n_cores_serie = returnListValues('cores.csv', 'n_cores')
    
    years_frequency_serie = returnListValues('frequency.csv', 'year')
    frequency_serie = returnListValues('frequency.csv', 'frequency')
    
    years_transistors_serie = returnListValues('transistors.csv', 'year')
    transistors_serie = returnListValues('transistors.csv', 'transistors')
    
    years_watts_serie = returnListValues('watts.csv', 'year')
    watts_serie = returnListValues('watts.csv', 'watts')
    
    years_thread_perf_serie = returnListValues('specint.csv', 'year')
    thread_perf_serie = returnListValues('specint.csv', 'specint')
    
    print("converting Panda Series --> lists")
    years_n_core_list = createListValues(years_n_core_serie)
    n_cores_list = createListValues(n_cores_serie)
    
    years_frequency_list = createListValues(years_frequency_serie)
    frequency_list = createListValues(frequency_serie)
    
    years_transistors_list = createListValues(years_transistors_serie)
    transistors_list = createListValues(transistors_serie)
    
    years_watts_list = createListValues(years_watts_serie)
    watts_list = createListValues(watts_serie)
    
    years_thread_perf_list = createListValues(years_thread_perf_serie)
    thread_perf_list = createListValues(thread_perf_serie)
    
    print("plotting")
    figObject1 = plt.figure();
    ax1 = figObject1.add_subplot(111)
    plt.plot( years_n_core_list, n_cores_list, '^', markersize=3, label='Number of Logical Cores')
    plt.plot( years_frequency_list, frequency_list, 's', markersize=3, label='Frequency (MHz)')
    plt.plot( years_transistors_list, transistors_list, 'd', markersize=3, label='Transistors (thousands)')
    plt.plot( years_watts_list, watts_list, 'v', markersize=3, label='Power (Watts)')
    plt.plot( years_thread_perf_list, thread_perf_list, '>', markersize=3, label='Single Thread Perf')
    plt.title("Microprocessor Trend Data")
    ax1.set_yscale('log')
    ax1.set_xlabel('Year')
    ax1.legend()
    plt.savefig("microprocessor_trend.svg", format="svg")
    