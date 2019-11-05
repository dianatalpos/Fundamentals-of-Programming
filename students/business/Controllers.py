from model.Discipline import Discipline
from model.Grade import Grade
from model.Student import Student
from model.Undo import Operation, CascadeOperation
from model.StudentAvgDTO import StudentAvgDTO, StudentFailDTO
from errors.Errors import RepoError, UndoError, RedoError
from repo.Repository import Repository
from repo.Repository import Undo_Repository


class DisciplineService(object):
    
    def __init__(self,repo, validator, repo_undo):
        self.__repo = repo
        self.__validator = validator
        self.__repoUndo = repo_undo 
        
    def add_Discipline(self, id, nume):
        '''
        Function that adds a discipline in repository
        in: id, name
        pre: id is an integer> 0 , name is a string
        out: repo = repo U discipline(id, name)
        Raise RepoError if the element already exist  
        '''
        discipline = Discipline(id, nume)
        self.__validator.validateDiscipline(discipline)
        self.__repo.add(discipline)
        undo = Operation(Repository.remove, discipline, Repository.add, discipline, "discipline")
        operation = CascadeOperation()
        operation.add(undo)
        self.__repoUndo.add(operation, self.__repoUndo.get_index())
        self.__repoUndo.set_index(self.__repoUndo.get_index() + 1)
         
        
        
    def get_all_disciplines(self):
        '''
        function that returns all the disciplines from repository
        '''
        return self.__repo.getAll()
    
    
    def update_Discipline(self, id, name):
        '''
        function that update a discipline 
        in:in > 0 , name string
        out: repo = repo with the name of the discipline with id id changed in name 
        raise repo error if the discipline doesn t exist 
        '''
        discipline = Discipline (id, name)
        self.__validator.validateDiscipline(discipline)
        old_discipline = self.__repo.search(discipline.get_id())
        undo = Operation(Repository.update, old_discipline, Repository.update, discipline, "discipline")
        operation = CascadeOperation()
        operation.add(undo)
        self.__repoUndo.add(operation, self.__repoUndo.get_index())
        self.__repoUndo.set_index(self.__repoUndo.get_index() + 1)
        self.__repo.update(discipline)
        
        
    def search_Discipline_id(self,id):
        '''
        Functions that searches a discipline in the list 
        in: id
        out: discipline with all attributes if exist 
        '''
        discipline = Discipline(id, None)
        return self.__repo.search(discipline)
    
    def search_Discipline_name(self, name):
        '''
        Function that searches a discipline by name
        in: name
        out: lst - list with all disciplines that have name name or the disciplines with name partial matching with name.
        '''
        dscp = Discipline(None, name)
        self.__validator.validateDiscipline(dscp)
        disciplines = self.__repo.getAll()
        disciplines_with_name = []
        for i in range(0, len(disciplines)):
            if (name.lower() in disciplines[i].get_name().lower()) or (disciplines[i].get_name().lower() in name.lower()) :
                disciplines_with_name.append(disciplines[i])
        
        return disciplines_with_name
         
        







class GradeService(object):
    
    def __init__(self, repoStudent, repoDiscipline, repoGrade, validator, repo_undo):
        self.__repoGrade = repoGrade
        self.__validator = validator
        self.__repoDiscipline = repoDiscipline
        self.__repoStudent = repoStudent 
        self.__repoUndo = repo_undo
    
    def get_all_grades(self):
        '''
        function that returns all the grades from repository
        '''
        return self.__repoGrade.getAll()
    
    def remove_Discipline(self, id):
        '''
        function that removes a discipline from the repository
        in: id > 0
        out: repo = repo\ discipline with id id 
        raise RepoError if the discipline doesn t exist 
        '''
        discipline = self.__repoDiscipline.search(id)
        self.__repoDiscipline.remove(id)
        undo = Operation(Repository.add, discipline, Repository.remove, discipline, "discipline") 
        operations = CascadeOperation()
        operations.add(undo)
        grades = self.__repoGrade.getAll()
        for grade in grades :
            if grade.get_discipline() == id :
                self.__repoGrade.remove(grade)        
                undo = Operation(Repository.add, grade, Repository.remove, grade, "grade")
                operations.add(undo)
                
        self.__repoUndo.add(operations, self.__repoUndo.get_index())
        self.__repoUndo.set_index(self.__repoUndo.get_index() + 1) 

    def add_Grade(self,grade_id, student_id, discipline_id, grade_value):
        '''
        Function that adds a grade in repository
        in:garde_id, student_id, discipline_id > 0, grade_value float
        out repo U grade 
        '''
        student = self.__repoStudent.search(student_id)
        discipline = self.__repoDiscipline.search(discipline_id)
        grade = Grade(grade_id, student, discipline, grade_value)
        self.__repoGrade.add(grade)
        undo = Operation(Repository.remove, grade, Repository.add, grade, "grade")
        operation = CascadeOperation()
        operation.add(undo)
        self.__repoUndo.add(operation, self.__repoUndo.get_index())
        self.__repoUndo.set_index(self.__repoUndo.get_index() + 1)

        #undo = Undo(self.__repoGrade.remove, grade)
        #self.__repoUndo.add([undo])
       
    def remove_Student(self, id):
        '''
        function that removes a student from the repository
        in: id > 0
        out: repo = repo\ student with id id 

        '''
        undos = []
        student = self.__repoStudent.search(id)
        self.__repoStudent.remove(id)
        
        undo = Operation(Repository.add, student, Repository.remove, student, "student")
        operations = CascadeOperation()
        operations.add(undo)
        
        grades = self.__repoGrade.getAll()
        for grade in grades :
            if grade.get_student() == id :
                
                self.__repoGrade.remove(grade)
                undo = Operation(Repository.add, grade, Repository.remove, grade, "grade")
                operations.add(undo)
                
        self.__repoUndo.add(operations, self.__repoUndo.get_index())
        self.__repoUndo.set_index(self.__repoUndo.get_index() + 1)
    
   
    def grades_at_discipline(self, id_discipline):
        '''
        Function that returns all the grades at the discipline id_discipline
        in:id_discipline
        out: lst = list with all grades at the discipline id_discipline
        
        '''
        grades = self.__repoGrade.getAll()
        grades_at_discipline = []
        for i in grades:
            if i.get_discipline() == id_discipline:
                grades_at_discipline.append(i)
        
        return grades_at_discipline
    
 
    def students_attend_discipline(self, id_discipline):
        '''
        function that make a list with all students that attend at discipline id_discipline
        '''
        grades = self.grades_at_discipline(id_discipline)
        students_average = []
        students = {}
        for grade in grades:
            student_id = grade.get_student().get_id()
            if student_id not in students :
                students[student_id] = [0,0,grade.get_student().get_name()]
            students[student_id][0] += 1
            students[student_id][1] += grade.get_grade()
        
        
        for student_id in students:
            student_avg = StudentAvgDTO(student_id, students[student_id][2], students[student_id][1]/students[student_id][0]) 
            students_average.append(student_avg)
        
        return students_average
        
    
    def sort_students_avg(self, list , condition):
        '''
        Function that returns the students with average grade sorted by avg grade
        out:list of students sorted
        '''
        if condition == "grade":
            list.sort(key = lambda x: (x.get_avg(), x.get_name()) , reverse= True)
        else:
            list.sort(key = lambda x: x.get_name() , reverse = False)
        return list 
        
    def statistics_students_at_discipline(self, id_discipline, condition):
        '''
        Function that returns the students that attend at a given discipline sorted by avg grade
        in:id_discipline
        out:list of students sorted
        '''
        list = self.students_attend_discipline(id_discipline)
        list = self.sort_students_avg(list,condition)
        return list
    
    def disciplines_average(self):
        '''
        Function that calculates the average for all discipline and return it
        '''
        disciplines = {}
        grades = self.__repoGrade.getAll()
        for grade in grades:
            discipline_id = grade.get_discipline().get_id()
            if discipline_id not in disciplines:
                disciplines[discipline_id] = [grade.get_discipline().get_name(), 0, 0]
            disciplines[discipline_id][1] += grade.get_grade()
            disciplines[discipline_id][2] += 1
        list = []
        for id in disciplines:
            disciplines_avg = StudentAvgDTO(id, disciplines[id][0], disciplines[id][1]/ disciplines[id][2])
            list.append(disciplines_avg)
        list = self.sort_students_avg(list, "grade")
        return list
        
        
    def students_failing(self):
        '''
        Function that returns all the students that are failing at one or more discipline
        '''
        disciplines = self.__repoDiscipline.getAll()
        students = {}
        for discipline in disciplines:
            students_avg = self.students_attend_discipline(discipline.get_id())
            for student in students_avg:
                if student.get_avg() < 5:
                    id = student.get_id() 
                    if id not in students:
                        students[id] = [student.get_name(), 0]
                    students[id][1] += 1
        list = []
        for student_id in students:
            std_fail = StudentFailDTO(student_id, students[student_id][0], students[student_id][1] )
            list.append(std_fail)
        return list
    
    def best_students(self):
        '''
        Function that returns a list with the best students and the aggregated average
        
        '''
        disciplines = self.__repoDiscipline.getAll()
        students = {}
        for discipline in disciplines:
            students_avg = self.students_attend_discipline(discipline.get_id())
            for student in students_avg:
                id = student.get_id()
                if id not in students:
                    students[id] = [student.get_name(), 0, 0]
                students[id][1] += student.get_avg()
                students[id][2] +=1
                    
        list = []
        for id in students :
            std_avg = StudentAvgDTO(id , students[id][0] , students[id][1]/students[id][2])
            if std_avg.get_avg() >= 5:
                list.append(std_avg)
        list = self.sort_students_avg(list, "grade")
        return list
        
    
class StudentService(object):
    
    def __init__(self, repo, validator, repo_undo):
        self.__repo = repo
        self.__validator = validator
        self.__repoUndo = repo_undo
        
    def add_Student(self, id, nume):
        '''
        Function that adds a student in repository
        in: id, name
        pre: id is an integer> 0 , name is a string
        out: repo = repo U student(id, name)
        Raise RepoError if the element already exist  
        '''
        student = Student(id, nume)
        #undo = Undo(self.__repo.remove, student)
        #self.__repoUndo.add([undo])
        self.__validator.validateStudent(student)
        self.__repo.add(student)
        undo = Operation(Repository.remove, student, Repository.add, student, "student")
        operation = CascadeOperation()
        operation.add(undo)
        self.__repoUndo.add(operation, self.__repoUndo.get_index())
        self.__repoUndo.set_index(self.__repoUndo.get_index() + 1)

        
    def get_all_students(self):
        '''
        function that returns all the students from repository
        '''
        return self.__repo.getAll()
    

    def update_Student(self, id, name):
        '''
        function that update a student
        in:in > 0 , name string
        out: repo = repo with the name of the student with id id changed in name 
        raise repo error if the student doesn t exist 
        '''
        std = self.__repo.search(id)
        #undo = Undo(self.__repo.update, std)
        #self.__repoUndo.add([undo])

        student = Student(id, name)
        self.__validator.validateStudent(student)
        self.__repo.update(student)
        
        undo = Operation(Repository.update, std, Repository.add, student, "student")
        operation = CascadeOperation()
        operation.add(undo)
        self.__repoUndo.add(operation, self.__repoUndo.get_index())
        self.__repoUndo.set_index(self.__repoUndo.get_index() + 1)


    def search_Student_id(self,id):
        '''
        Functions that searches a student in the list 
        in: id
        out: student with all attributes if exist 
        '''
        student = Student(id, None)
        return self.__repo.search(student)
         
            
    def search_Student_name(self, name):
        '''
        Function that searches a student by name
        in: name
        out: lst - list with all students that have name name or the students with name partial matching with name.
        '''
        std = Student(None, name)
        self.__validator.validateStudent(std)
        students = self.__repo.getAll()
        students_with_name = []
        for i in range(0, len(students)):
            if (name.lower() in students[i].get_name().lower()) or (students[i].get_name().lower() in name.lower()) :
                students_with_name.append(students[i])
        
        return students_with_name
     

class UndoService(object):
    
    
    def __init__(self, undo_repo, repo_students, repo_disciplines, repo_grades):
        self.__repo_students = repo_students
        self.__repo_disciplines = repo_disciplines
        self.__repo_grades = repo_grades
        self.__undo_repo = undo_repo
        
        
    def perform_undo(self):
        '''
        undos = self.__repo_undo.getAll()
        if len(undos) != 0:
            redo = []
            list = undos[len(undos) - 1][0]
            list_redo = undos[len(undos) - 1][1]
            for i in range (0, len(list)):
                undo_fct = list[i].get_undo_function()
                undo_elem = list[i].get_undo_elem()
                undo_fct(undo_elem)
                redo.append(list_redo[i])
                
            self.__repo_undo.remove(undos[len(undos)-1])
            self.__repo_redo.add(redo)
        else:
            raise UndoError("Can't perform any undo! You must perform an action before! ")
        '''
        if self.__undo_repo.get_index() > 0:
            list = self.__undo_repo.getAll()
            list = list[self.__undo_repo.get_index() - 1].getAll()
            for operation in list:
                undo_function = operation.get_undo_function()
                elem = operation.get_undo_elem()
                entity = operation.get_entity()
                if entity == "discipline" :
                    undo_function(self.__repo_disciplines, elem)
                elif entity == "student":
                    undo_function(self.__repo_students, elem)
                elif entity == "grade":
                    undo_function(self.__repo_grades, elem)
        
                self.__undo_repo.set_index(self.__undo_repo.get_index() - 1)
        
        else:
            raise UndoError("Can't perform any undo! You must perform an action before! ")
        
        
       
       
              
    def perform_redo(self):
        '''
        undos = self.__repo_undo.getAll()
        redos = self.__repo_redo.getAll()
        if len(redos) != 0:
            undo = []
            list = redos[len(redos)-1]
            for redo in list:
                redo_fct = redo.get_undo_function()
                redo_elem = redo.get_undo_elem()
                redo_fct(redo_elem)
            self.__repo_redo.remove(redos[len(redos)-1])
        else:
            raise RedoError("Can't perform any redo! You must perform an undo before!")
        '''
        if self.__undo_repo.get_index() < len(self.__undo_repo.getAll()):
            list = self.__undo_repo.getAll()
            list = list[self.__undo_repo.get_index()].getAll()
            for operation in list:
                redo_function = operation.get_redo_function()
                elem = operation.get_redo_elem()
                entity = operation.get_entity()
                if entity == "discipline" :
                    redo_function(self.__repo_disciplines, elem)
                elif entity == "student":
                    redo_function(self.__repo_students, elem)
                elif entity == "grade":
                    redo_function(self.__repo_grades, elem)
    
                self.__undo_repo.set_index(self.__undo_repo.get_index() + 1)
        else:
            raise RedoError("Can't perform any redo! You must perform an undo before!")
        
        
