class Student:
    def __init__(self,name=None,roll_no=None,subject=None,marks=None):
        self.name=name
        self.roll_no=roll_no
        self.subject=subject
        self.marks=marks
    def Subjects(self,subject):
        self.subject=subject
    def Mark(self,marks):
        self.marks=marks
    def display(self):
        print("Student Name:",self.name)
        print("Roll_no :",self.roll_no)
        print("Subject :",self.subject)
        print("Mark obtained is:",self.marks)

obj=Student("Reshma",5)
obj.Subjects("physics")
obj.Mark(50)
obj.display()
