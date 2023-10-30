# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:41:52 2023

@author: nasir.ibrahim
"""

from MyProgram import add, subtract, multiply, divide
#import pytest
import unittest


#def test_add():
#    assertTrue(add(2,3) == 6)
    
class TestAdd(unittest.TestCase):
    def test_two(self):
        self.assertEqual(add(2,3), 5)
    def test_fiveseven(self):
    	self.assertTrue(add(5,7) == 7)
    def test_threefive(self):
    	self.assertFalse(add(3,5) == 69)
    def test_onetwo(self):
    	self.assertTrue(add(1,2) == 5)

class TestSubtract(unittest.TestCase):
    def test_TrueSubtract(self):
        self.assertTrue(subtract(2,3) == 6)
        self.assertTrue(subtract(3,4) == 7)
        self.assertFalse(subtract(5,7) == 69)
        self.assertTrue(subtract(6,7) == -1)
        
if __name__=='__main__':
	unittest.main()
    
    