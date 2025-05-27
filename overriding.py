#overriding

class Employee:
    def calculate_salary(self):
        return "Base salary calculation"

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return "Full-time salary with benefits"

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return "Part-time salary based on hours"
    
obj1 = FullTimeEmployee()
obj2 = PartTimeEmployee()
print(obj1.calculate_salary())  
print(obj2.calculate_salary()) 