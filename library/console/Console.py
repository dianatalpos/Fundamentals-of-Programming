from errors.Errors import RepoError, ValidError

class Console(object):

    
    def __init__(self, serv_book, serv_client, serv_rental):
        self.__serv_book = serv_book
        self.__serv_client = serv_client
        self.__serv_rental = serv_rental
        self.__commands = {"addbook" : self.__ui_add_book, 'removebook' : self.__ui_remove_book, "updateBookName" : self.__ui_update_book_name,
                           "updateBookDescription" : self.__ui_update_book_description, "addClient": self.__ui_add_client }
    
    def __menu(self):
        print("Commands:")
        print("\t addbook")
        print("\t removebook")
        print("\t updateBookName")
        print("\t updateBookDescription")
        print("\t addClient")
    
    def __ui_add_client(self):
        id = input("Give id: ")
        try:
            id = int(id)
        except ValueError as ve :
            print("The id must be an integer!")
        name = input("Give the name: ")
        
        self.__serv_client.add_client(id, name)
        
        
    def __ui_remove_client(self):
        id = input

    def __ui_update_book_description(self):
        id  = input("Give id: ")
        desc = input("Give description: ")
        
        try:
            id = int(id)
        except ValueError as ve:
            print("The id must be an integer!")
        
        title = None
        author = None
        
        self.__serv_book.update_book(id, title, desc, author)

    def __ui_add_book(self):
        
        ident = input("Give id: ")
        ident = ident.strip()
        title = input("Give title: ")
        description = input("Give description: ")
        author =  input("Give author: ") 
        
        
        try:
            ident = int(ident)
        except ValueError as ve:
            print("The id must be an integer!")
            
        self.__serv_book.add_book(ident, title, description, author)
    
    def __ui_remove_book(self):
        ident = input("Give id: ")
        try:
            ident = int(ident)
        except ValueError as ve:
            print("The id must be an integer!")
        self.__serv_book.remove_book(ident)    
                  
    def __ui_update_book_name(self):
        id = input("Give id: ")
        name = input("Give the new name: ")
        try:
            ident = int(id)
        except ValueError as ve:
            print("The id must be an integer!")
        description = None
        author = None
        
        self.__serv_book.update_book(ident, name, description, author)
        
    
    def run(self):
        
        while True:
            self.__menu()
            x = input("Give a command!\n")
            param = x.split(" ")
            
            if param[0] in self.__commands:
                try:
                    self.__commands[param[0]]()
                except ValidError as ve:
                    print(ve)
                except RepoError as re:
                    print(re)
            elif x == "exit":
                return
            else:
                print("Ivalid command!")
    


