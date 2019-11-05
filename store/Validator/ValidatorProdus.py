'''
Created on Feb 16, 2019

@author: Andrea
'''
from Errors.Error import ValidError
class ValidatorProdus():
    
    def ValidatorProdus(self, object):
        errors=""
        if int(object.get_id()) <= 0:
            errors+="Id-ul trebuie sa fie un numar pozitiv"
        if str(object.get_denumire()) == "":
            errors+="Denumirea nu poate sa fie vida"
        if int(object.get_pret()) <= 0:
            errors+="Pretul trebuie sa fie un numar pozitiv"
        
        if len(errors) >0:
            raise ValidError(errors)