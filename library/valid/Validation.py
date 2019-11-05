
from errors.Errors import ValidError
from domain.Entities import Book, Client, Rental

class BookValidator(object):
    
    
    def __init__(self):
        pass
    
    
    def book_validation(self, book):
        errors = ""
        if book.get_id() < 0:
            errors += "Invalid id!\n"
            
        if book.get_title() == "":
            errors += "Invalid title!\n"
        
        if book.get_description() == "" :
            errors += "Invalid description!\n"
            
        if book.get_author() == "":
            errors += "Invalid author!\n"
        
        if len(errors)>0:
            raise ValidError(errors) 



class ClientValidator(object):
    
    
    def __init__(self):
        pass
    
    def client_validation(self, client):
        
        errors = ""
        
        if client.get_id() < 0 :
            errors += "Invalid id!\n"
        if client.get_name == "":
            errors += "Invalid name!\n"
            
        if len(errors) > 0:
            raise ValidError(errors)
    



class RentalValidator(object):
    
    
    def __init__(self):
        pass
    
    



