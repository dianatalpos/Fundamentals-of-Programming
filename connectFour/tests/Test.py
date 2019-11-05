'''
Created on Jan 8, 2019

@author: Andrea
'''

from domain.Entities import Board
import unittest

class BoardTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def test_is_won(self):
        b = Board()
        b.move(1,'red')
        b.move(2,'red')
        b.move(3,'red')
        b.move(4,'red')
        self.assertTrue(b.is_won())
        b = Board()
        b.move(1,'red')
        b.move(1,'red')
        b.move(1,'red')
        self.assertFalse(b.is_won()) 
        
        