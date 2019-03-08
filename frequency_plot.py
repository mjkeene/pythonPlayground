#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 18:55:17 2019

@author: Michael Keene
"""
import matplotlib.pyplot as plt

def freq(string):
    """
    A function that displays the frequency of each character in a given string
    in a dictionary and bar chart.
    """
    
    myDict = {}
    for i in string:
        myDict.setdefault(i, 0)
        myDict[i] += 1
    print(myDict)
    
    plt.bar(myDict.keys(), myDict.values())
    plt.show()
freq('MichaelKeene')
