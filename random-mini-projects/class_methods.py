from datetime import date

class Student:
    school_name = "ABC School"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.name, self.age, "School: ", Student.school_name)
jessi = Student("Jessi", 20)
jessi.show()
#change school_name
joy = Student.calculate_age("Joy", 1955)
joy.show()

#create a class method
class School:
    #class variable
    name= "ABC School"

    def school_name(cls):
        print("School Name is: ", cls.name)
#create class method
School.school_name = classmethod(School.school_name)
#call class method
School.school_name()

#Access class method



