from repo.Repository import Repository


class Service_ski(object):
    
    def __init__(self, repo):
        self.__repo = repo

    
    def best_jumpers(self):
        '''
        Function that sort the list of elements in the reverse order and return the first 3 elements
        
        in -
        out: list of 3 elements with the best ski jumpers
        '''
        list = self.__repo.getAll()
        
        list.sort(key = lambda x: x.get_distance() , reverse = True)

        return list[0:3]
    
    def jumps(self):
        '''
        Function that sort the jumps by the distance and returns the list
        '''
        
        list = self.__repo.getAll()
        
        list.sort(key = lambda x: x.get_distance() , reverse = False)
        
        return list
    
    
    def jump_file(self):
        
        
        filename ="C:\\Andrea\\eclipse-python\\test2\\jumps.txt"
        with open(filename, "w") as f:
            list = self.jumps()
            contor = 0
            for jump in list:
                value = jump.get_distance()/50 
                for i in range(0,int(value)):
                    f.write("*")
                f.write(jump.get_name())
            