




class Person:
    Country = "India"
 
    def __init__(self):
        print("Initializing Person...\n")

    
    def takeBreath(self):
        print(f"I am Breathing.....")


class Employee(Person):
    Company = "Tata"

    def __init__(self):
        super().__init__()
        print("Initializing Employee...\n")
    
    def getSalary(self):
        print(f"The Salary is {self.salary}.")

    def takeBreath(self):
        super().takeBreath()
        print(f"I am an Employee so I am Luckilly Breathing.....")    


class Programmer(Employee):
    Company = "Mahindra"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer...\n")

    def getSalary(self):
        print(f"There are no Salary for the Programmer.")
 
    def takeBreath(self):
        super().takeBreath()
        print(f"I am an Programmer so I am Luckilly Breathing ++ ...")    


p = Person()
p.takeBreath()

e = Employee()
e.takeBreath()

pr = Programmer()
pr.takeBreath()