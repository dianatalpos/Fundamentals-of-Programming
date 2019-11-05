class Book(object):
    
    
    def __init__(self, ident, title, description, author):
        self.__id = ident
        self.__title = title
        self.__description = description
        self.__author = author

    def get_id(self):
        return self.__id


    def get_title(self):
        return self.__title


    def get_description(self):
        return self.__description


    def get_author(self):
        return self.__author


    def set_title(self, value):
        self.__title = value


    def set_description(self, value):
        self.__description = value


    def set_author(self, value):
        self.__author = value

    def __str__(self):
        return str(self.get_id()) + ', ' + self.get_title() + ', ' + self.get_description() + ', ' + self.get_author()

    def __eq__(self, book):
        return self.get_id() == book.get_id() 
        
        
        
    id = property(get_id, None, None, None)
    title = property(get_title, set_title, None, None)
    description = property(get_description, set_description, None, None)
    author = property(get_author, set_author, None, None)
    
    



class Client(object):
    
    
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id


    def get_name(self):
        return self.__name


    def set_name(self, value):
        self.__name = value

    def __str__(self):
        return str(self.get_id()) + self.get_name()
    
    def __eq__(self, client):
        return client.get_id() == self.get_id()
    

    id = property(get_id, None, None, None)
    name = property(get_name, set_name, None, None)
        
    
    
    



class Rental(object):
    pass


