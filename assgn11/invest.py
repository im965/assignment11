# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 15:52:39 2014

@author: Israel
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from myexceptions import *
from summary import *
from plots import *

def calcCumRet(bet):
    ''' Returns the cumulative value of 'bet' investments of value 1000/'bet' 
        in an instrument that returns double 51% and zero 49%  of the time'''
        
    return ((np.random.random((1,bet))>0.49).sum(axis=1)*2.0*(1000/bet))[0]

    
def invest(positions,num_trials):
    '''Returns a dataframe with percentage returns of the form [trial(i),position(j)], 
    where entry[i,j] represents the i'th independent trial of buying 'j' investments 
    of value 1000/'j' in an instrument the returns double 51% and zero 49%  of the time.'''
    
    #Calculations (Simulation)
    position_value = 1000/np.array(positions)
    cumu_ret = DataFrame(columns=positions,index=np.arange(1,num_trials+1))
    
    for i in position_value:
        col=1000/i
        cumu_ret[col] = col
        cumu_ret[col] = cumu_ret[col].map(calcCumRet)    
    daily_ret = (cumu_ret/1000)-1
    return daily_ret
    
def investInput():
    ''' This program interacts with the user to obtain input that will be passed to the invest function.
    \n  It ensure that the user input is valid and then passes argument, returns a dataframe of returns
    \n  Additionally, a results.txt file with summary stats and plots of the distribution of returns are saved to the cd.'''
    
    print "You will now be asked to enter input to the invest function. \nPlease see docstring for input details. \nEnter end to stop program."
    
    #intialize input to empty/None    
    positionsClean = None    
    postionsCheck = 0
    positionsInput= None
    trialsClean = None
    trialsCheck = 0 
    trialsInput = None
    end='end'
    
    
    while positionsClean==None  and positionsInput!='end':
        try:
            rawPositionsInput = raw_input("Please enter a list of positions \n")
            positionsInput = eval(rawPositionsInput)
        
     
            #Exception Handling (positions argument)
            if type(positionsInput)!=list:
                raise NotListError
            if all([(type(x)==int or type(x)==float) for x in positionsInput])==False:
                raise NotNumError
            if all([x % 1==0.0 for x in positionsInput])==False:
                raise NotIntError
            if all([(0<x<=1000) for x in positionsInput])==False:
                raise InvalidPosError
            
        except (NotListError, NotNumError, NotIntError, InvalidPosError) as e:
            print e
        except (NameError) as e:
            print "Please enter a valid input for positions, to quit enter 'end' \n"
        except (KeyboardInterrupt, EOFError, SyntaxError) as e:
            print "Caught a keyboard interrupt or EOF or SyntaxError, to quit enter 'end' \n"
            
        else:
            positionsCheck = 1
            positionsClean = positionsInput
    
    if positionsInput=='end':
        print "You have quit before entering in all arguments"+"\n........Goodbye!"
            
            
    while trialsClean==None and positionsInput!='end' and trialsInput!='end':
        try:
            rawTrialsInput = raw_input("Please enter the number of trials \n")
            trialsInput = eval(rawTrialsInput)
        
     
            #Excption Handling (num_trials argument)    
            if (type(trialsInput)!=int and type(trialsInput)!=float):
                raise TrialNotNumError
            if 0>=(trialsInput):
                raise TrialNegError
            
        except (TrialNotNumError, TrialNegError, NotIntError, InvalidPosError) as e:
            print e
        except (NameError) as e:
            print "Please enter a valid input for trials, to quit enter 'end' \n"
        except (KeyboardInterrupt, EOFError, SyntaxError) as e:
            print "Caught a keyboard interrupt or EOF or SyntaxError, to quit enter 'end' \n"
            
        else:
            trialsCheck = 1
            trialsClean = trialsInput
            
            
    if trialsInput=='end':
        print "You have quit before entering in all arguments"+"\n........Goodbye!"
    
    ### If made it this far, input is valid
    if trialsInput!='end' and positionsInput!='end' and trialsClean!=None and positionsClean!=None:
        results = invest(positionsClean,trialsClean)
        printSummary(results,'results')
        print '\n Summary statistics have been printed to results.txt \n'
        plotCharts(results)
        print '\n Histograms with the distribution of returns for each positions have been saved \n'
        return results
        
    
    
        
    
