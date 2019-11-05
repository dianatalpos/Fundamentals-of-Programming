'''
Created on Feb 3, 2019

@author: Andrea
'''
import unittest

from domain.Entities import Book, Client, Rental
from business.Service import BookService, ClientService, RentalService
from repo.Repository import RentalRepository, ClientRepository, BookRepository



class Tests(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    

    '''
    tests for books repository
    
    '''
    def test_repo_book(self):
        
        book = Book(5, "cdv", "dvfdv", "Dfd")
        file = "C:\\Andrea\\eclipse-python\\library\\test_books"
        repo =BookRepository(file)
        self.assertEqual(len(repo.getAll()), 0)
        
        repo.add(book)
        list = repo.getAll()
        self.assertEqual(len(list), 1)
        self.assertEqual(list[0], book)

        try:        
            repo.add(book)
            self.assertFalse(1)
        except:
            self.assertTrue(1)
        
        book = Book(1, "alfa","ion","fhdsuj")
        repo.add(book)
        
        book1 = Book(5, None, None, None)
        repo.remove(book1)
        
        list = repo.getAll()
        self.assertEqual(len(list), 1)
        self.assertEqual(list[0],book) 