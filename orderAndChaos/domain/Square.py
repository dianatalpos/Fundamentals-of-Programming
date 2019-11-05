class Square(object):
    
    
    def __init__(self, row, column):
        self.__row = row
        self.__column = column

    def get_row(self):
        return self.__row


    def get_column(self):
        return self.__column

    row = property(get_row, None, None, None)
    column = property(get_column, None, None, None)
    
    
     


