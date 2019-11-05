class Grade:
    
    def __init__(self, grade_id, student, discipline, grade):
        '''
        in: discipline_id, student_id - integers
            grade - float 
        '''
        
        self.__discipline = discipline
        self.__student = student
        self.__grade = grade
        self.__gradeId = grade_id
    
    def get_discipline(self):
        return self.__discipline
    
    def get_student(self):
        return self.__student
    
    def get_grade(self):
        return self.__grade
    
    def set_grade(self, grade):
        self.__grade = grade
        
    def get_grade_id(self):
        return self.__gradeId
    
    def __eq__(self, other):
        if type(other) == int:
            return self.get_grade_id() == other
        return self.get_grade_id() == other.get_grade_id()
     
    def __lt__(self, other):
        if type(other) == int : 
            return self.get_grade() < other
        return self.get_grade() < other.get_grade() 
    def __str__(self):
        return  str(self.get_student()) + "   Grade: " + str(self.get_grade()) + " " + str((self.get_discipline()))