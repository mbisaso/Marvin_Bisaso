#real world problem

class Person:
    def display_info(self, name=None, age=None):
        if name and age:
            print(f"Person's Name: {name}, Age: {age}")
        else:
            print("A person's information.")
    
class Student(Person):
    def display_info(self, name=None, age=None, reg_no=None):
        if name and age and reg_no:
            print(f"Student Name: {name}, Age: {age}, ID: {reg_no}")
        else:
            print("Incomplete student information.")
            
class Lecturer(Person):
    def display_info(self, name=None, age=None, courseunit=None):
        if name and age and courseunit:
            print(f"Lecturer Name: {name}, Age: {age}, Teaches: {courseunit}")
        else:
            print("Incomplete lecturer information.")
            
class Staff(Person):
    def display_info(self, name=None, age=None, department=None):
        if name and age and department:
            print(f"Staff Name: {name}, Age: {age}, Department: {department}")
        else:
            print("Incomplete staff information.")
            
obj1 = Person()
obj1.display_info('Abdallah',30)

obj2 = Student()
obj2.display_info('John',22,'23/U/3242')

obj3 = Lecturer()
obj3.display_info('Nasser',41,'Data Science')

obj4 = Staff()
obj4.display_info('Kintu',48,'Registrar')