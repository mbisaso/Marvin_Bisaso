#overriding

class Person:
    def occupation(self):
        return 'PERSON'
    
class Student(Person):
    def occupation(self):
        return "Student"

class Lecturer(Person):
    def occupation(self):
        return "Teacher"

class AssistantLecturer(Student, Lecturer):
    pass

obj1 = AssistantLecturer()

print(obj1.occupation())

print(AssistantLecturer.mro())
