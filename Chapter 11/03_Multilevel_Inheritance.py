





class Person:
    Country = "India"

    def takeBreath(self):
        print(f"I am Breathing.....")


class Employee(Person):
    Company = "Tata"
    
    def getSalary(self):
        print(f"The Salary is {self.salary}.")

    def takeBreath(self):
        print(f"I am an Employee so I am Luckilly Breathing.....")    


class Programmer(Employee):
    Company = "Mahindra"

    def getSalary(self):
        print(f"There are no Salary for the Programmer.")


p = Person() 
p.takeBreath()       # ====> I am Breathing.....
# print(p.Company)   # ====> Error()
e = Employee()
e.takeBreath()       # ====> I am an Employee so I am Luckilly Breathing.....
print(e.Company)     # ====> Tata
pr = Programmer()
pr.takeBreath()      # ====> I am an Employee so I am Luckilly Breathing.....
print(pr.Company)    # ====> Mahindra