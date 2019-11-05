from errors.Errors import RepoError
from domain.Entities import Book, Client, Rental



class BookRepository(object):
    
    
    def __init__(self, file_name):
        self.__elems = []
        self.__file_name = file_name
        self.__readAllFromFile()
    
    def __readAllFromFile(self):
        try:    
            with open(self.__file_name, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line != "":
                        words = line.strip().split(",")
                        id = int(words[0].strip())
                        title = words[1].strip()
                        description = words[2].strip()
                        author = words[3].strip()
                        book = Book(id, title, description, author)
                        self.__elems.append(book)
        except FileNotFoundError as fe:
            print("Inexistent file " + self.__file_name)
        
    def __writeAllToFile(self):
        try:
            with open(self.__file_name, "w") as f:
                for elem in self.__elems:
                    f.write(str(elem)+ "\n")
                
        except FileNotFoundError as fe:
            print("Inexistent file " + self.__file_name)        
            
            
    def add(self, book):
        '''
        Add a book to the list
        '''
        if book in self.__elems:
            raise RepoError("Existing book!")
        
        self.__elems.append(book)
        self.__writeAllToFile()
        
    def remove(self, book):
        '''
        Remove a book from the list
        '''
        
        if book not in self.__elems:
            raise RepoError("Inexistent book!")
        
        self.__elems.remove(book)
        self.__writeAllToFile()
        
    def update(self, book):
        '''
        Update a book from the list
        '''
        
        if book not in self.__elems:
            raise RepoError("Inexistent book!")
        for i in range(len(self.__elems)):
            if self.__elems[i] == book:
                if book.get_title() != None:
                    self.__elems[i].set_title(book.get_title())
                if book.get_description() != None:    
                    self.__elems[i].set_description(book.get_description())
                if book.get_author() != None:
                    self.__elems[i].set_author(book.get_author())
                self.__writeAllToFile()
                return
    def getAll(self):
        return self.__elems
        

class ClientRepository(object):
    
    
    def __init__(self, file_name):
        self.__elems = []
        self.__file_name = file_name
        self.__readAllFromFile()
        
    def __readAllFromFile(self):
        try:    
            with open(self.__file_name, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line != "":
                        words = line.strip().split(",")
                        id = int(words[0].strip())
                        name = words[1].strip()
                        client = Client(id, name)
                        self.__elems.append(client)
        except FileNotFoundError as fe:
            print("Inexistent file " + self.__file_name)
        
    def __writeAllToFile(self):
        try:
            with open(self.__file_name, "w") as f:
                for elem in self.__elems:
                    f.write(str(elem)+ "\n")
                
        except FileNotFoundError as fe:
            print("Inexistent file " + self.__file_name)        
            
            
    def add(self, client):
        '''
        Add a client to the list
        '''
        if book in self.__elems:
            raise RepoError("Existing book!")
        
        self.__elems.append(client)
        self.__writeAllToFile()
        
    def remove(self, client):
        '''
        Remove a client from the list
        '''
        
        if client not in self.__elems:
            raise RepoError("Inexistent book!")
        
        self.__elems.remove(client)
        self.__writeAllToFile()
        
    def update(self, client):
        '''
        Update a client from the list
        '''
        
        if client not in self.__elems:
            raise RepoError("Inexistent book!")
        for i in range(len(self.__elems)):
            if self.__elems[i] == client:
                self.__elems[i] = client
                self.__writeAllToFile()
                return

    def getAll(self):
        return self.__elems
    



class RentalRepository(object):
    
    
    def __init__(self, file_name):
        self.__file_name = file_name
        
    
    



