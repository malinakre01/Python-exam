# Question 1

# Person - class:
class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    
    def get_info(self):
        print("Full Name:", self.fname, self.lname)
        print("Age:", self.age)


# Student - class (inherit from the "Person" class, and add "student id):
class Student(Person):
    def __init__(self, fname, lname, age, student_id):
        super().__init__(fname, lname, age)
        self.student_id = student_id
        
    def get_stuinfo(self):
         self.get_info()
         print("Student ID:", self.student_id)

# Employee - class (inherit from the "Person" class, and add "employee number" and "salary"):
class Employee(Person):
    def __init__(self, fname, lname, age, emp_number, salary):
        super().__init__(fname, lname, age)
        self.emp_number = emp_number
        self.salary = salary
    
    def get_empinfo(self):
        self.get_info()
        print("Employee Number:", self.emp_number)
        print("Salary:", self.salary, "USD")
 
# The code below works with the implementation over:^^

#new_student = Student ("Anthony", "Smith", 35, "s346571")
#new_student.get_stuinfo ()
#print ("==========================")
#new_employee = Employee ("Sarah", "Taylor", 34, 2919736, 5000)
#new_employee.get_empinfo ()  
