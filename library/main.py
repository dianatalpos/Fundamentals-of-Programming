'''
Created on Feb 3, 2019

@author: Andrea
'''

from console.Console import Console
from business.Service import BookService, ClientService, RentalService
from repo.Repository import RentalRepository, ClientRepository, BookRepository
from valid.Validation import BookValidator, ClientValidator, RentalValidator

files_name = {"book" : 'C:\\Andrea\\eclipse-python\\library\\Books', "client" : 'C:\\Andrea\\eclipse-python\\library\\Clients', "rental" : 'C:\\Andrea\\eclipse-python\\library\\Rentals'}

validator_book = BookValidator()
validator_client = ClientValidator()
validator_rental = RentalValidator()

repo_rentals = RentalRepository(files_name["rental"])
repo_clients = ClientRepository(files_name["client"])
repo_books = BookRepository(files_name["book"])

serv_rental = RentalService(repo_rentals, validator_rental)
serv_client = ClientService(repo_clients, validator_client)
serv_book = BookService(repo_books, validator_book) 

c = Console(serv_book, serv_client, serv_rental)

c.run()
