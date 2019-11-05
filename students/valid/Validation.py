
from errors.Errors import ValidError

class StudentValidator(object):
    
    def __init__(self):
        pass
    
    def validateStudent(self, student):
        '''
        Function that validates a student
        in: student= id, name
            id>0
            name != ""
        raise ValidError if the conditions aren't met 
        '''
        errors=""
        if student.get_id() is not None and student.get_id() < 0:
            errors+="Invalid id!\n"
        if student.get_name() is not None :
            if len(student.get_name()) ==  0:
                errors+="Empty name!\n"
        
        if len(errors) > 0:
            raise ValidError(errors)


class DisciplineValidator(object):
  
    
    def __init__(self):
        pass
    
    def validateDiscipline(self, discipline):
        '''
        Function that validates a discipline
        in: discipline= id, name
            id>0
            name != ""
        raise ValidError if the conditions aren't met 
        '''
        
        errors=""
        if discipline.get_id() is not None and discipline.get_id() < 0:
            errors+="Invalid id!\n"
        if discipline.get_name() is not None and len(discipline.get_name()) ==  0:
            errors+="Empty name!\n"
        
        if len(errors) > 0:
            raise ValidError(errors)




class GradeValidator(object):
    
    def __init__(self):
        pass
    
    def validateGrade(self, grade):
        '''
        Function that validates a grade
        in: discipline= id, name
            id_discipline > 0
            id_student > 0
            id_grade > 0
            1 < grade_value < 10
        raise ValidError if the conditions aren't met 
        '''
        errors=""
        if grade.get_grade_id() is not None and grade.get_grade_id() < 0:
            errors += "Invalid grade id!\n"
        if grade.get_grade()is not None and (int(grade.get_grade()) < 1 or int(grade.get_grade()) > 10):
            errors += "Invalid value for grade!\n" 
            
        if len(errors) != 0 :
            raise ValidError(errors)
            