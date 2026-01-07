#class variables = shared among all instances of the class
#                   defined outside the constructor
#                   allow you to share data among all objects created from that class

class Student:
    class_year = 2024
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("John", 25)
student2 = Student("Patrick", 26)
student3 = Student("Smith", 27)

print(student1.name)
print(student2.name)
print(Student.class_year)
print(Student.num_students)
print(f"My graduating class of {Student.class_year} has {Student.num_students} students")