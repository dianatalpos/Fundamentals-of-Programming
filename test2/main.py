'''
Created on Dec 19, 2018

@author: Andrea
'''

from repo.Repository import Repository, RepositoryFile
from business.Service import Service_ski
from ui.Console import Console
from tests.Test import Test
    
repo_ski = RepositoryFile("C:\\Andrea\\eclipse-python\\test2\\repo\\ski_jumps.txt")

service_ski = Service_ski(repo_ski)

console = Console(service_ski)

console.run()