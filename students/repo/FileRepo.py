
from repo.Repository import Repository
from model.Student import Student
from model.Discipline import Discipline
from model.Grade import Grade

class FileRepoStudents(object):
    
    def __init__(self,filename):
        Repository.__init__(self)
        self.__filename = filename
        self.__readAllFromFile()
    
    def __readAllFromFile(self):
        try:
            with open(self.__filename, "r") as f:
                
                lines = f.readlines()
                for line in lines:
                    if line != "":
                        words = line.strip().split(",")
                        ident = int(words[0].strip())
                        name = words[1].strip()
                        student = Student(ident,name)
                        self._elems.append(student)
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)
    
    def __writeAllToFile(self):
        try:
            with open(self.__filename,"w") as f:
                for elem in self._elems:
                    f.write(str(elem)+"\n")
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)


    def add (self, student):
        Repository.add(self, student)
        self.__writeAllToFile()
        
    def remove(self, student):
        Repository.remove(self, student)
        self.__writeAllToFile()
    
    def update(self, student):
        Repository.update(self, student)
        self.__writeAllToFile()
        
    def search(self, student):
        student = Repository.search(self, student)
        return student
    
    def getAll(self):
        return Repository.getAll(self)
        
class FileRepoDiscipline(object):
    def __init__(self,filename):
        Repository.__init__(self)
        self.__filename = filename
        self.__readAllFromFile()
    
    def __readAllFromFile(self):
        try:
            with open(self.__filename, "r") as f:
                
                lines = f.readlines()
                for line in lines:
                    if line != "":
                        words = line.strip().split(",")
                        ident = int(words[0].strip())
                        name = words[1].strip()
                        discipline = Discipline(ident,name)
                        self._elems.append(discipline)
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)
    
    def __writeAllToFile(self):
        try:
            with open(self.__filename,"w") as f:
                for elem in self._elems:
                    f.write(str(elem)+"\n")
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)


    def add (self, discipline):
        Repository.add(self, discipline)
        self.__writeAllToFile()
        
    def remove(self, discipline):
        Repository.remove(self, discipline)
        self.__writeAllToFile()
    
    def update(self, discipline):
        Repository.update(self, discipline)
        self.__writeAllToFile()
        
    def search(self, discipline):
        discipline = Repository.search(self, discipline)
        return discipline
    
    def getAll(self):
        return Repository.getAll(self)


class FileRepoGrades(object):
    def __init__(self,filename, repo_students, repo_disciplines):
        Repository.__init__(self)
        self.__filename = filename
        self.__repo_students = repo_students
        self.__repo_disciplines = repo_disciplines
        self.__readAllFromFile()
    
    def __readAllFromFile(self):
        try:
            with open(self.__filename, "r") as f:
                
                lines = f.readlines()
                for line in lines:
                    if line != "":
                        words = line.strip().split(",")
                        ident = int(words[0].strip())
                        id_student = int(words[1].strip())
                        id_discipline = int(words[2].strip())
                        student = self.__repo_students.search(id_student)
                        discipline = self.__repo_disciplines.search(id_discipline)
                        value = float(words[3].strip())
                        grade = Grade(ident,student, discipline, value)
                        self._elems.append(discipline)
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)
    
    def __writeAllToFile(self):
        try:
            with open(self.__filename,"w") as f:
                for elem in self._elems:
                    id_grade =  elem.get_grade_id()
                    id_student = elem.get_student().get_id()
                    id_discipline = elem.get_discipline().get_id()
                    string = str(id_grade) + ", "+ str(id_student)+ ", " + str(id_discipline) + ", "+ str(elem.get_grade()) 
                    f.write(string)
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)


    def add (self, discipline):
        Repository.add(self, discipline)
        self.__writeAllToFile()
        
    def remove(self, discipline):
        Repository.remove(self, discipline)
        self.__writeAllToFile()
    
    def update(self, discipline):
        Repository.update(self, discipline)
        self.__writeAllToFile()
        
    def search(self, discipline):
        discipline = Repository.search(self, discipline)
        return discipline
    
    def getAll(self):
        return Repository.getAll(self)


