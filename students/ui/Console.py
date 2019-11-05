
from errors.Errors import RepoError, ValidError, UndoError, RedoError


class Console(object):
    
    def __init__(self, servStudent, servDiscipline, servGrade, servUndo):
        self.__service_student = servStudent
        self.__service_discipline = servDiscipline
        self.__service_grade = servGrade
        self.__service_undo = servUndo

    def __menu(self):
        print("1. Add a student: 'add student id name'")
        print("2. Print all students: 'print students'")
        print("3. Update a student: 'update student id new_name'")
        print("4. Remove a student: 'remove student id'")
        print("5. Add a discipline: 'add discipline id name'")
        print("6. Print all disciplines: 'print disciplines' ")
        print("7. Update a discipline: 'update discipline id new_name'")
        print("8. Remove a discipline: 'remove discipline id'")
        print("9. Give a grade to a student at a discipline: 'give grade grade_id student_id discipline_id grade_value'")
        print("10. Print grades")
        print("11. Search student by id/name: 'search student id/name'")
        print("12. Search discipline by id/name: 'search student id/name'")
        print("13. Statistics about students at a given discipline sorted alphabetically or by average grade: 'statistics students discipline id_discipline 'alphabetically'/'grade'")
        print("14. Students failing at one or more disciplines: 'students failing'")
        print("15. Students with the best school situation, sorted in descending order of their aggregated average: 'best students'")
        print("16. All disciplines at which there is at least one grade, sorted in descending order of the average grade received by all students enrolled at that discipline: 'disciplines average'")
        print("0. Exit: 'exit'")
    
    def initial_list(self):
                               
        
        self.__service_student.add_Student(1,"Popescu")
        self.__service_student.add_Student(2,"Pop")
        self.__service_student.add_Student(3,"Gicu")
        self.__service_student.add_Student(4,"Ben")
        self.__service_student.add_Student(5,"Jack")
        self.__service_student.add_Student(6,"Rose")
        self.__service_student.add_Student(7,"Petre")
        self.__service_student.add_Student(8,"Nicu")
        self.__service_student.add_Student(9,"Ryan")
        self.__service_student.add_Student(10,"Ana")
        self.__service_student.add_Student(11,"Jay")
        self.__service_student.add_Student(12,"Beyonce")
        self.__service_student.add_Student(13,"Bea")
        self.__service_student.add_Student(14,"Alfred")
        self.__service_student.add_Student(15,"Einstein")
        
        
        self.__service_undo.perform_undo()
        
        self.__service_undo.perform_redo()
        '''
        self.__service_discipline.add_Discipline(1, "Math")
        self.__service_discipline.add_Discipline(2  , "Physics")
        self.__service_discipline.add_Discipline(3 ,"Computer Science")
        self.__service_discipline.add_Discipline(4  , "Chemistry")
        self.__service_discipline.add_Discipline(5  , "Biology")
        self.__service_discipline.add_Discipline(6  , "Music")
        self.__service_discipline.add_Discipline(7 , "ASC")
        self.__service_discipline.add_Discipline(8, "Sport")
        self.__service_grade.add_Grade(1,1,3, 7.5)
        self.__service_grade.add_Grade(2,1,1, 9)
        self.__service_grade.add_Grade(3,2,4, 6)
        self.__service_grade.add_Grade(4,2,1, 10)
        self.__service_grade.add_Grade(5,2,2, 9.5)
        self.__service_grade.add_Grade(6,3,2, 7.5)
        self.__service_grade.add_Grade(7,3,3, 9.5)
        self.__service_grade.add_Grade(8,4,1, 9.5)
        self.__service_grade.add_Grade(9,4,4, 6.5)
        self.__service_grade.add_Grade(10,4,1, 8)
        self.__service_grade.add_Grade(11,3,1, 5)
        self.__service_grade.add_Grade(12,2,1, 7)
        self.__service_grade.add_Grade(13,1,1, 6)
        self.__service_grade.add_Grade(14,3,1, 7)
        self.__service_grade.add_Grade(15,2,1, 8)
        self.__service_grade.add_Grade(16,5,5, 4)
        self.__service_grade.add_Grade(17,5,5, 3)
        self.__service_grade.add_Grade(18,5,2, 2)
        self.__service_grade.add_Grade(19,5,2, 3)
        self.__service_grade.add_Grade(20,6,1, 5)
        self.__service_grade.add_Grade(21,6,1, 4)
        self.__service_grade.add_Grade(22,7,3, 7)
        self.__service_grade.add_Grade(23,7,1, 1)
        self.__service_grade.add_Grade(24,7,2, 9)
        self.__service_grade.add_Grade(25,8,3, 7)
        self.__service_grade.add_Grade(26,8,1, 1)
        self.__service_grade.add_Grade(27,9,6, 4)
        self.__service_grade.add_Grade(28,9,5, 6)
        self.__service_grade.add_Grade(29,9,1, 2)
        self.__service_grade.add_Grade(30,9,2, 4)
        self.__service_grade.add_Grade(31,9,3, 3)
        self.__service_grade.add_Grade(32,10,4, 5)
        self.__service_grade.add_Grade(33,10,1, 2)
        self.__service_grade.add_Grade(34,10,1, 3)
        self.__service_grade.add_Grade(35,10,8, 10)
        self.__service_grade.add_Grade(36,11,6, 5.5)
        self.__service_grade.add_Grade(37,11,4, 8)
        self.__service_grade.add_Grade(38,11,5, 4.5)
        self.__service_grade.add_Grade(39,12,1, 3.20)
        self.__service_grade.add_Grade(40,12,2, 5.90)
        self.__service_grade.add_Grade(41,12,3, 2)
        self.__service_grade.add_Grade(42,13,4, 10)
        self.__service_grade.add_Grade(43,13,5, 8)
        self.__service_grade.add_Grade(44,13,6, 6)
        self.__service_grade.add_Grade(45,14,5, 7.75)
        self.__service_grade.add_Grade(46,14,1, 9)
        self.__service_grade.add_Grade(47,14,3, 6)
        self.__service_grade.add_Grade(48,15,8, 10)
        self.__service_grade.add_Grade(49,15,6, 9.10)
        self.__service_grade.add_Grade(50,15,2, 8.30)
        '''
        
    '''
    
    STUDENTS
    
    '''  
        
    def __ui_add_student(self, param):
        if len(param) != 2:
            print("Invalid number of params!")
            return
        try:
            id = int(param[0])
        except ValueError as ve:
            print("The id must be a number!")
        name = param[1]
        self.__service_student.add_Student(id, name)
    
    def __ui_print_students(self,param):
        if len(param) != 0:
            print("Invalid number of params!")
            return
        l = self.__service_student.get_all_students()
        for x in l:
            print(x)
    
    def __ui_update_student(self, param):
        if len(param) != 2:
            print("Invalid number of params!")
            return
        try:
            id = int(param[0])
        except ValueError() as ve:
            print ("The id must be a number!")
        name = param[1]
        self.__service_student.update_Student(id, name)
          
    def __ui_remove_student(self, param):       
        if len(param)!=1:
            print ("Invalid number of params!")
            return 
        try:
            id = int(param[0])
        except ValueError as ve:
            print("The id must be a number!")
        self.__service_grade.remove_Student(id)
    
    def __ui_search_student(self,param):
        if len(param) != 1:
            print("Invalid number of params!")
            return
        try:
            id = int(param[0])
            try:
                std = self.__service_student.search_Student_id(id)
                print(std)
            except RepoError as re:
                print(re)
            return
        except:
            students = self.__service_student.search_Student_name(param[0])
            if students == []:
                print("There are no students with name " + param[0] + " or students with name that partial matches with the name given.")
            else:
                for i in students:
                    print(i)
    
    def __ui_statistics_students_discipline(self, params):
        if len(params) != 2:
            print("Invalid numbers of params!")
            return 
        try:
            id = int(params[0])
        except ValueError as ve:
            print("The id must be a number!")
        if params[1]!= "alphabetically" and params[1] != "grade" :
            print("The word after what we sort the list must be 'alphabetically' or 'grade' ")
            return
        list = self.__service_grade.statistics_students_at_discipline(id, params[1])
        for i in list :
            print(i)
        
    '''
    
    DISCIPLINES
    
    
    '''
    
    
    def __ui_add_dicipline(self,param):
        if len(param) != 2:
            print("Invalid number of params!")
            return
        try:
            id = int(param[0])
        except ValueError as ve:
            print("The id must be a number!")
        name = param[1]
        self.__service_discipline.add_Discipline(id, name)
        
    def __ui_print_disciplines(self,param):
        if len(param) != 0:
            print("Invalid number of params!")
            return
        l = self.__service_discipline.get_all_disciplines()
        for x in l:
            print(x)
    
    def __ui_update_discipline(self, param):
        if len(param) != 2:
            print("Invalid number of params!")
            return
        try:
            id = int(param[0])
        except ValueError() as ve:
            print ("The id must be a number!")
        name = param[1]
        self.__service_discipline.update_Discipline(id, name)
          
    def __ui_remove_discipline(self, param):       
        if len(param)!=1:
            print ("Invalid number of params!")
            return 
        try:
            id = int(param[0])
        except ValueError as ve:
            print("The id must be a number!")
        self.__service_grade.remove_Discipline(id) 
        
    def __ui_search_discipline(self,param):
        if len(param) != 1:
            print("Invalid number of params!")
            return
        try:
            id = int(param[0])
            try:
                dspl = self.__service_discipline.search_Discipline_id(id)
                print(dspl)
            except RepoError as re:
                print(re)
            return
        except:
            disciplines = self.__service_discipline.search_Discipline_name(param[0])
            if disciplines == []:
                print("There are no disciplines with name " + param[0] + " or disciplines with name that partial matches with the name given.")
            else:
                for i in disciplines:
                    print(i)
    
    
    '''
    
    GRADES
    
    
    '''
       
    def __ui_print_grades(self, param):
        if len(param) != 0 :
            print("Invalid number of params!")
            return
        l = self.__service_grade.get_all_grades()
        for x in l:
            print(x)
            

    def __ui_add_grade(self, param):
        if len(param) != 4:
            print("Invalid number of params!")
            return
        id = int(param[0])
        id_student = int(param[1])
        id_discipline = int(param[2])
        grade = float(param[3])
        self.__service_grade.add_Grade(id, id_student, id_discipline, grade)
    

    def __ui_students_failing(self,param):
        if len(param) !=0:
            print("Invalid number of params!")
            return
        list = self.__service_grade.students_failing()
        for i in list:
            print(i)
    

    def __ui_best_students(self, params):
        if len(params) != 0:
            print("Invalid number of params!")
            return
        list = self.__service_grade.best_students()
        for i in list:
            print(i)
    

    def __ui_discipline_average(self, params):
        if len(params) != 0:
            print("Invalid number of params!")
            return 
        list = self.__service_grade.disciplines_average()
        for i in list:
            print(i)
    
    
    def __ui_undo(self):
        self.__service_undo.perform_undo()
    
    
    def __ui_redo(self):
        self.__service_undo.perform_redo()
    
    
    def run(self):
        commands = {"statistics students discipline": self.__ui_statistics_students_discipline,
                    "search discipline": self.__ui_search_discipline, 
                    "search student": self.__ui_search_student, 
                    "print grades": self.__ui_print_grades ,  
                    "remove discipline": self.__ui_remove_discipline, 
                    "update discipline": self.__ui_update_discipline, 
                    "print disciplines" : self.__ui_print_disciplines,
                    "add discipline": self.__ui_add_dicipline,
                    "remove student": self.__ui_remove_student, 
                    "update student" : self.__ui_update_student, 
                    "add student" : self.__ui_add_student , 
                    "print students" : self.__ui_print_students,
                    "give grade": self.__ui_add_grade,
                    "students failing": self.__ui_students_failing,
                    "best students" : self.__ui_best_students,
                    "disciplines average": self.__ui_discipline_average,
                    "undo" : self.__ui_undo,
                    "redo" : self.__ui_redo
                    } 
        while True:
            self.__menu()
            x = input("Give a command: ")
            new = x.split(" ")
            if x == "exit":
                return
            elif x == "undo":
                try:
                    commands[x]()
                except UndoError as ue:
                    print("Undo error!")
                    print(ue)
            elif x =="redo" :
                try:
                    commands[x]()
                except RedoError as re:
                    print("Redo error!")
                    print(re)
            elif len(new) > 1:
                if str(new[0] + " " + new[1]) in commands:
                    try:
                        commands[str(new[0] + " " + new[1])](new[2:])
                    except RepoError as re:
                        print("Repository error!")
                        print(re)
                    except ValidError as ve:
                        print("Validation error!")
                        print(ve)
                else:
                    print("Invalid command!")
            elif  len(new) > 2:
                if str(new[0]+ " " + new[1]+ " " +new[2]) in commands:
                    try:
                        commands[new[0]+ " " + new[1]+ " " +new[2]](new[3:])
                    except ValidError as ve:
                        print(ve)
                else:
                    print("Invalid command!")
            else:
                print("Invalid command!")
