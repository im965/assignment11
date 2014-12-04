# -*- coding: utf-8 -*-
"""
Created on Mon Dec 01 16:27:15 2014

@author: Israel
"""
from pandas import DataFrame

def printSummary(dataframe,filename):
    '''This functions prints the columns-wise mean and standard deviation of the 
       passed dataframe to the filename specified as a txt file'''
       
    means=DataFrame(dataframe.mean(),columns=["Mean by Position"])
    stddev=DataFrame(dataframe.std(),columns=["Std Dev by Position"])
    
    # write summary stats totxt
    f = open(filename+'.txt','w')
    f.write(str(means))
    f.write('\n')
    f.write('\n')
    f.write(str(stddev))
    f.flush()
    f.close()