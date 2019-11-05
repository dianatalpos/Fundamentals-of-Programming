from repo.Repository import RentalRepository, ClientRepository, BookRepository
from domain.Entities import Book, Client, Rental


class BookService(object):

    
    def __init__(self, repo_books, validator_book):
        self.__repo_books = repo_books
        self.__validator_book = validator_book
    
    
    def add_book(self, id, title, description, author):
        
        book = Book(id, title, description, author)
        self.__validator_book.book_validation(book)
        self.__repo_books.add(book)
        
    def remove_book(self,id):
        book = Book(id, None, None, None)
        self.__validator_book.book_validation(book)
        self.__repo_books.remove(book)
        
    def update_book(self, id, title, description, author):
        book = Book(id, title, description, author )
        self.__validator_book.book_validation(book)
        self.__repo_books.update(book)


class ClientService(object):
    
    
    def __init__(self, repo_clients, validator_client):
        self.__repo_clients = repo_clients
        self.__validator_client = validator_client
    
    



class RentalService(object):
    
    
    def __init__(self, repo_rentals, validator_rental):
        self.__repo_rentals = repo_rentals
        self.__validator_rental = validator_rental
    
    



