'''
Created on Feb 5, 2019

@author: Andrea
'''

from ui.Console import Console
from business.Controller import Service
from repo.Repository import Repository
from valid.Validator import Validator

repo_sentences = Repository()
validator = Validator()

serv_game = Service(repo_sentences, validator)

console = Console(serv_game)
console.run()