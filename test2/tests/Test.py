import unittest
from model.Ski_jump import Ski_jump
from business.Service import Service_ski
from repo.Repository import Repository, RepositoryFile

class Test(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test_repo(self):
        repo = Repository()
        
        self.assertEqual(len(repo.getAll()), 0)
        
        jump = Ski_jump("gicu", 32.46, 10, -3)
    
        repo.add(jump)
        self.assertEqual(jump, repo.getAll()[0])

    