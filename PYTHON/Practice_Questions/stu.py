# Create a class Student that:
# - Takes name and marks.
# - Has a method check_result().
# - Displays Pass if marks are 50 or above.
# - Otherwise displays Fail.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_result(self):
        if self.marks >= 50:
            print("pass")
        else:
            print("fail")

    def display(self):
           print("Name:", self.name)
           print("Marks:", self.marks)

s1 = Student("Ali", 75)
s2 = Student("Ahmed", 45)

s1.display()
s1.check_result()
s2.display()
s2.check_result()
