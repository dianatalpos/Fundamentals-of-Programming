

class Console(object):
    
    
    def __init__(self, service_ski):
        self.__service_ski = service_ski
    
    def menu(self):
        print("1. Best 3 jumpers")
        print("2. Jumps in file")
    
    def ui_best(self):
        list = self.__service_ski.best_jumpers()
        for elem in list:
            print(elem)
    
    def ui_jump_file(self):
        self.__service_ski.jump_file()
    
    
    def run(self):
        self.menu()
        while True:
            x = input("Give a command(1 or 2): ")
            if x == "1":
                self.ui_best()
            elif x == "2":
                self.ui_jump_file()
            elif x =="exit":
                return
            else:
                print("Invalid command!")


