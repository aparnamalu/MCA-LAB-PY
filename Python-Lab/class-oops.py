class Student:
    def __init__(self,rollno, name,course):
        self.rollno=rollno
        self.name = name
        self.course = course
    def display(self):
        print("Rollno:",self.rollno)
        print("Name:", self.name)
        print("course:", self.course)
s1 = Student(16,"Aparna","mca")
s2 = Student(22,"Devu","mca")
s1.display()
s2.display()
