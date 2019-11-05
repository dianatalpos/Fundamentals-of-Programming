
from model.Student import Student
from model.Discipline import Discipline
from model.Grade import Grade
from valid.Validation import StudentValidator, DisciplineValidator, GradeValidator
from errors.Errors import ValidError, RepoError
from repo.Repository import Repository, Undo_Repository
from business.Controllers import StudentService, GradeService , DisciplineService,UndoService
import unittest

class Test():
    
    def __init__(self):
        self.__studentid = 23
        self.__studentname = "Popescu"
        self.__student = Student(self.__studentid, self.__studentname)
        self.__badstudentid = -15
        self.__badstudentname = ""
        self.__badstudent = Student(self.__badstudentid, self.__badstudentname) 
        self.__validstudent = StudentValidator()
       
        self.__disciplineid = 15
        self.__disciplinename = "Math"
        self.__discipline = Discipline(self.__disciplineid, self.__disciplinename)
        self.__baddisciplineid = -7
        self.__baddisciplinename = ""
        self.__baddiscipline = Discipline(self.__baddisciplineid, self.__baddisciplinename)
        self.__validdiscipline = DisciplineValidator()
        
        self.__gradeid = 1
        self.__gradevalue = 9
        self.__grade = Grade(self.__gradeid, self.__student, self.__discipline, self.__gradevalue)
        self.__validgrade = GradeValidator()
        self.__badgradeid = -1
        self.__badgradevalue = 12
        self.__badgrade = Grade(self.__badgradeid, self.__badstudent, self.__baddiscipline, self.__badgradevalue)
        self.__repoUndo = Undo_Repository
        
        self.__repoStudents = Repository()
        self.__repoGrades = Repository()
        self.__serviceStudents = StudentService(self.__repoStudents, self.__validstudent, self.__repoUndo)
        self.__repoDiscipline = Repository()
        self.__serviceDiscipline = DisciplineService(self.__repoDiscipline, self.__validdiscipline, self.__repoUndo)
        self.__serviceGrade = GradeService( self.__repoStudents, self.__repoDiscipline, self.__repoGrades, self.__validgrade, self.__repoUndo)
        self.__service_undo = UndoService(self.__repoUndo, self.__repoStudents, self.__repoDiscipline, self.__repoGrades)
    
    
    def test_model_student(self):
        assert Student.get_id(self.__student) == self.__studentid
    
    def test_model_discipline(self):
        assert Discipline.get_id(self.__discipline) == self.__disciplineid
        
    def test_model_grade(self):
        assert Grade.get_grade_id(self.__grade) == self.__gradeid
        
    def test_valid_student(self):
        try:
            self.__validstudent.validateStudent(self.__student)
            assert True
        except:
            assert False
        
        try:
            self.__validstudent.validateStudent( self.__badstudent)
            assert False
        except ValidError as ve:
            assert str(ve) == "Invalid id!\nEmpty name!\n"

    def test_valid_discipline(self):
        try:
            self.__validdiscipline.validateDiscipline(self.__discipline)
            assert True
        except:
            assert False
        
        try:
            self.__validstudent.validateStudent( self.__baddiscipline)
            assert False
        except ValidError as ve:
            assert str(ve) == "Invalid id!\nEmpty name!\n"
    
    def test_valid_grade(self):
        try:
            self.__validgrade.validateGrade(self.__grade)
            assert True
        except:
            assert False
        
        try:
            self.__validgrade.validateGrade(self.__badgrade)
            assert False
        except ValidError as ve:
            assert str(ve) == "Invalid grade id!\nInvalid value for grade!\n"
    
    
    def test_repo(self):
        assert len(self.__repoStudents) == 0
        
        self.__repoStudents.add(self.__student)
        assert len(self.__repoStudents) == 1
        try:
            self.__repoStudents.add(self.__student)
            assert False
        except RepoError as re:
            assert str(re) == "Existing element!\n"
        
        student_to_search = Student(self.__studentid, None)
        assert self.__repoStudents.search(student_to_search) == self.__student
        try:
            self.__repoStudents.search(self.__badstudent)
            assert False
        except RepoError as re:
            assert str(re) == "Inexisting element!\n"
            
        student_to_update = Student(self.__studentid, "Nelu")
        self.__repoStudents.update(student_to_update)
        students = self.__repoStudents.getAll()
        assert students == [student_to_update]
        assert self.__repoStudents.search(student_to_search) == student_to_update
        try:
            self.__repoStudents.update(self.__badstudent)
            assert False
        except RepoError as re:
            assert str(re) == "Inexisting element!\n"
             
        student_to_remove = Student(self.__studentid, None)
        self.__repoStudents.remove(student_to_remove) 
        students = self.__repoStudents.getAll()
        assert students == []
        try:
            self.__repoStudents.remove(self.__badstudent)
            assert False
        except RepoError as re:
            assert str(re) == "Inexisting element!\n"
        
            
    def test_business(self):
        
        assert self.__serviceStudents.get_all_students() == []
        self.__serviceStudents.add_Student(self.__studentid, self.__studentname)
        students = self.__serviceStudents.get_all_students()
        assert students == [self.__student]
        try:
            self.__serviceStudents.add_Student(self.__studentid, self.__studentname)
            assert False
            students = self.__serviceStudents.get_all_students()
        except RepoError as re:
            assert str(re) == "Existing element!\n"
        assert students == [self.__student]
        self.__serviceGrade.remove_Student(self.__student.get_id())
        students = self.__serviceStudents.get_all_students()
        assert students == []
        try:
            self.__serviceGrade.remove_Student(self.__student.get_id())
            assert False
            students = self.__serviceStudents.get_all_students()
        except RepoError as re:
            assert str(re) == "Inexisting element!\n"
        
        self.__serviceStudents.add_Student(self.__studentid, self.__studentname)
        students = self.__serviceStudents.get_all_students()
        newSt = Student(self.__studentid, "Gicu")
        self.__serviceStudents.update_Student(self.__studentid, newSt.get_name())
        students = self.__serviceStudents.get_all_students()
        assert students == [newSt]
        
        
        std = self.__serviceStudents.search_Student_id(self.__studentid)
        assert std.get_name() == newSt.get_name()
        
        try:
            std = self.__serviceStudents.search_Student_id(5)
            assert False
        except RepoError as re:
            assert True
        
        
        self.__serviceStudents.add_Student(1, "Gicu")
        self.__serviceStudents.add_Student(2, "gIcU")
        self.__serviceStudents.add_Student(3, "Gicurescu")
        
        std1 = Student(1,"Gicu")
        std2 = Student(2, "gIcU")
        std3 = Student(3, "Gicurescu")
        std_search_name = self.__serviceStudents.search_Student_name("gicu")
        
        assert std_search_name == [newSt, std1, std2, std3]

        self.__serviceDiscipline.add_Discipline(self.__discipline.get_id(), self.__discipline.get_name())
        disciplines = self.__serviceDiscipline.get_all_disciplines()
        assert disciplines == [self.__discipline]
        
        
        self.__serviceGrade.add_Grade(self.__grade.get_grade_id(), self.__grade.get_student(),self.__grade.get_discipline(), self.__grade.get_grade())
        grades = self.__serviceGrade.get_all_grades()
        assert grades == [self.__grade]
        try:
            self.__serviceGrade.add_Grade(self.__grade.get_grade_id(), self.__grade.get_student(),self.__grade.get_discipline(), self.__grade.get_grade())
            grades = self.__serviceGrade.get_all_grades()
            assert False
        except RepoError as re:
            assert str(re) == "Existing element!\n"
      
        
    
    def run_test (self):
        pass
        '''
        assert 5/2 == 2.5 
        self.test_model_student()
        self.test_model_discipline()
        self.test_model_grade()
        self.test_valid_student()
        self.test_valid_discipline()
        self.test_valid_grade()
        self.test_repo()
        self.test_business()
        '''


class TestRepository(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def getAll(self):
        repo = Repository()
        
        self.assertEqual( len(repo.getAll()), 0)
    
    def testAdd(self):
        repo = Repository()
        
        student = Student(1, "Gicu")
        repo.add(student)
        self.assertEqual(repo.getAll(), [student])
    
    def testRemove(self):
        repo = Repository()
        
        student1 = Student(1, "Gicu")
        student2 = Student(2, "alfred")
        student3 = Student(3, "djevgc")
        
        repo.add(student1)
        repo.add(student2)
        repo.add(student3)
        
        repo.remove(student2)
        self.assertEqual(repo.getAll(), [student1, student3])
        
    def testUpdate(self):
        
        repo = Repository()
        
        student1 = Student(1, "Gicu")
        student2 = Student(2, "alfred")
        student3 = Student(3, "djevgc")
        
        repo.add(student1)
        repo.add(student2)
        repo.add(student3)
        
        std = Student(2, "nana")
        repo.update(std)
        
        elem = repo.getAll()[1]
        self.assertEqual(elem, std)
    
    def testSearch(self):
        repo = Repository()
        
        student1 = Student(1, "Gicu")
        student2 = Student(2, "alfred")
        student3 = Student(3, "djevgc")
        
        repo.add(student1)
        repo.add(student2)
        repo.add(student3)
        
        std = Student(2, None)
        
        std = repo.search(std)
        elems =  repo.getAll()
        
        self.assertEqual(elems[1], std)
        
        
class TestControllers(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def testDisciplineService(self):
        repo = Repository()
        valid = DisciplineValidator()
        undo = Undo_Repository()
        
        disc1 = Discipline(1,"Math")
        disc2 = Discipline(2,"physics")
        dsc = Discipline(1, "Asc")
        
        serv = DisciplineService(repo, valid, undo)
        
        serv.add_Discipline(1, "Math")
        
        self.assertEqual(serv.get_all_disciplines(), [disc1] )
        
        serv.add_Discipline(2, "physics")
        
        self.assertEqual(serv.get_all_disciplines(), [disc1,disc2])
        
        serv.update_Discipline(1, "Asc")
        
        self.assertEqual(serv.get_all_disciplines()[0], dsc)
        
        disc = serv.search_Discipline_id(2)
        
        self.assertEqual(disc, disc2)
        
        disc = serv.search_Discipline_name("Asc")
        
        self.assertEqual(disc, [disc1])
        