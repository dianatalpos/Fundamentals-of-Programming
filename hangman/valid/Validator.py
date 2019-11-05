from errors.Errors import ValidError


class Validator(object):
    
    
    def __init__(self):
        pass
    
    

    def valid_sentence(self, sentence):
        
        errors = ''
        words = sentence.split()
        
        if len(words) < 1:
            errors += "The sentence must have at least 1 word!\n"
        ok = 0 
        for word in words:
            if len(word) < 3:
                ok = 1
        if ok == 1:
            errors+= "All the words must have at least 3 letters!\n"
        if len(errors) > 0:
            raise ValidError(errors)     


