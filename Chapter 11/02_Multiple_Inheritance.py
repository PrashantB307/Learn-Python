




class Employee:
    company = "Google"

    def getComp(self):
        print(f"The Company is {self.company}.")


class Programmer:
    language = "Python"
    level = "1 Star"
    
    def getLang(self):
        print(f"The Language is {self.language}.")


class Student(Employee, Programmer):
    name = "Prashnat"

    def getName(self):
        print(f"The Name is {self.name}.")


s = Student()

print(s.level)   # ====> 1 Star
s.getName()      # ====> The Name is Prashnat.
s.getComp()      # ====> The Company is Google.
s.getLang()      # ====> The Language is Python.
