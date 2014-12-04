# -*- coding: utf-8 -*-
"""
Created on Mon Dec 01 16:37:42 2014

@author: Israel
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plotCharts(dataframe):
    '''Plots a historgram for each series of the dataframe passed'''
    
    for p in dataframe.columns:
        label = "%04d" % (p,)
        plt.figure(p)
        plt.hist(np.array(dataframe[p]),100,range=[-1,1])
        plt.title(str(p)+" Positions")
        plt.xlabel('Daily Return')
        plt.plot()
        plt.savefig('histogram_'+label+'_pos.pdf')

