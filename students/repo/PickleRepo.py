from repo.Repository import Repository
import pickle
from errors.Errors import *

class PickleRepoDisciplines(object):
    def __init__(self,filename):
        self.__filename = filename
        Repository.__init__(self)
        self.__readAll()

    def add(self, discipline):
        Repository.add(self, discipline)
        self.__saveToPickle()

    def remove(self, discipline):
        Repository.remove(self, discipline)
        self.__saveToPickle()

    def update(self, discipline):
        Repository.update(self, discipline)
        self.__saveToPickle()
    
    def getAll(self):
        return Repository.getAll(self)
    
    def search(self, discipline):
        discipline = Repository.search(self, discipline)
        return discipline
    

    def __saveToPickle(self):
        try:
            pickle.dump(self._elems,open(self.__filename,"wb"))
        except FileNotFoundError as fe:
            print("Inexisting file!")
    def __readAll(self):
        try:
            self._elems = pickle.load(open(self.__filename,"rb"))
        except EOFError:
            self._elems = []
        except FileNotFoundError as fe:
            print("Inexisting file!")


class PickleRepoStudents(object):
    
    def __init__(self,filename):
        self.__filename = filename
        Repository.__init__(self)
        self.__readAll()

    def add(self, student):
        Repository.add(self, student)
        self.__saveToPickle()

    def remove(self, student):
        Repository.remove(self, student)
        self.__saveToPickle()

    def update(self, student):
        Repository.update(self, student)
        self.__saveToPickle()
    
    def getAll(self):
        return Repository.getAll(self)
    
    def search(self, student):
        student = Repository.search(self, student)
        return student
    

    def __saveToPickle(self):
        try:
            pickle.dump(self._elems,open(self.__filename,"wb"))
        except FileNotFoundError as fe:
            print("Inexisting file!")
    def __readAll(self):
        try:
            self._elems = pickle.load(open(self.__filename,"rb"))
        except EOFError:
            self._elems = []
        except FileNotFoundError as fe:
            print("Inexisting file!")



class PickleRepoGrades(object):
    
    
    def __init__(self, filename, repo_students, repo_disciplines):
        self.__filename = filename
        self.__repo_students = repo_students
        self.__repo_disciplines = repo_disciplines
        Repository.__init__(self)
        self.__readAll()
    
    def add(self, grade):
        Repository.add(self, grade)
        self.__saveToPickle()

    def remove(self, grade):
        Repository.remove(self, grade)
        self.__saveToPickle()

    def update(self, grade):
        Repository.update(self, grade)
        self.__saveToPickle()
    
    def getAll(self):
        return Repository.getAll(self)
    
    def search(self, grade):
        grade = Repository.search(self, grade)
        return grade
    

    def __saveToPickle(self):
        try:
            pickle.dump(self._elems,open(self.__filename,"wb"))
        except FileNotFoundError as fe:
            print("Inexisting file!")
    def __readAll(self):
        try:
            self._elems = pickle.load(open(self.__filename,"rb"))
        except EOFError:
            self._elems = []
        except FileNotFoundError as fe:
            print("Inexisting file!")





