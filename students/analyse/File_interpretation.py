from repo.Repository import Repository, Undo_Repository
from repo.FileRepo import FileRepoStudents, FileRepoDiscipline, FileRepoGrades
from repo.PickleRepo import PickleRepoStudents, PickleRepoDisciplines, PickleRepoGrades
from valid.Validation import StudentValidator, DisciplineValidator, GradeValidator
from business.Controllers import StudentService, DisciplineService, GradeService, UndoService
from ui.Console import Console
from tests.Test import Test

class File_mode(object):

    def __init__(self):
        self.__filename = "C:\\Andrea\\eclipse-python\\newlab5-7\\analyse\\settings.properties.txt"
        self.__settings = self.__readFromFile()
    
    def __get_mode(self, line):
        line = line.strip()
        words = line.split(" ")
        if len(words) == 3:
            return words[2] 
        else:
            return ""
    
    def __readFromFile(self):
        
        settings = {}
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line= line.strip()
                if line != "":
                    words = line.split("=")
                    settings[words[0].strip()] = words[1].strip()
        
        return settings
            
    def app_generator(self):
        if self.__settings["mode"]=="inmemory":
            repo_students = Repository()
            repo_disciplines = Repository()
            repo_grades = Repository()
            

        elif self.__settings["mode"]=="binary":
            repo_students = PickleRepoStudents(self.__settings["file_students"])
            repo_disciplines = PickleRepoDisciplines(self.__settings["file_disciplines"])
            repo_grades = PickleRepoGrades(self.__settings["file_grades"], repo_students, repo_disciplines)
            
        elif  self.__settings["mode"]=="text":
            repo_students = FileRepoStudents(self.__settings["file_students"])
            repo_disciplines = FileRepoDiscipline(self.__settings["file_disciplines"])
            repo_grades = FileRepoGrades(self.__settings["file_grades"], repo_students, repo_disciplines)
        
        validator_student = StudentValidator()
        validator_discipline = DisciplineValidator()
        validator_grade = GradeValidator() 
        
        repo_undo = Undo_Repository()

        service_student = StudentService (repo_students, validator_student, repo_undo)
        service_discipline = DisciplineService(repo_disciplines, validator_discipline, repo_undo)
        service_grade = GradeService(repo_students, repo_disciplines, repo_grades, validator_grade, repo_undo)
        service_undo = UndoService(repo_undo, repo_students, repo_disciplines, repo_grades)


        console = Console (service_student, service_discipline, service_grade, service_undo) 
        
        if self.__settings["mode"]=="inmemory":
            console.initial_list()
        
        t = Test()
        t.run_test()

        return console
        