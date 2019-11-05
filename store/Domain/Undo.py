'''
Created on Feb 17, 2019

@author: Andrea
'''
class Undo():
    
    def __init__(self, function, elem, redo_function, redo_elem):
        self.__undo_function = function 
        self.__undo_elem = elem
        self.__redo_function = redo_function
        self.__redo_elem = redo_elem
        
    def get_redo_function(self):
        return self.__redo_function
    
    def get_redo_elem(self):
        return self.__redo_elem
    
    def get_undo_elem(self):
        return self.__undo_elem
    
    def get_undo_function(self):
        return self.__undo_function
    
class CascadeOperation(object):
    
    def __init__(self):
        self.__operations = [] 
    
    def getAll(self):
        return self.__operations
    
    def add(self, operation):
        self.__operations.append(operation)   