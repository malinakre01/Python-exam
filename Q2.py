# Question 2:
    
class Student:
    passingMark = 50

# "__init__" methos is to initialize objects of a class (constructor)
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
    
    def __str__(self):
     return f"Name: {self.name}, Mark: {self.mark}"  

    def passOrFail(self):
        if self.mark >= self.passingMark:
            return "Pass"
        else:
            return "Fail.."

# Student 1
student1 = Student("John", 52)
status1 = student1.passOrFail()
print("Status of student1:", status1)


# Student 2
student2 = Student("Jenny", 69)
status2 = student2.passOrFail()
print("Status of student2:", status2)


Student.passingMark = 60

status1 = student1.passOrFail()
status2 = student2.passOrFail()

print("Updated status of student1:", status1)
print("Updated status of student2:", status2)
