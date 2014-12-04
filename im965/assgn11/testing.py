# -*- coding: utf-8 -*-
"""
Created on Mon Dec 01 19:39:48 2014

@author: Israel
"""

from myexceptions import *
from invest import *
import unittest
import pandas


#test invest function
class TestInvest(unittest.TestCase):
    def setUp(self):
        self.itema =invest([1,10],10)
    def test_shape(self):
        self.assertEqual(len(self.itema.index), 10)  

#test CumReturns
class TestCumReturns(unittest.TestCase):
    def setUp(self):
        self.itema = calcCumRet(50)
    def test_returns(self):
        self.assertEqual(type(self.itema), numpy.float64) 


if __name__ == '__main__':
    unittest.main()
