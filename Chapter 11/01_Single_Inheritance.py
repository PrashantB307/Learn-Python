




class Employee:
    company = "Google"

    def getDetails(self):
        print(f"This is an Employee.")


class Programmer(Employee):
    language = "Python"

    def getLang(self):
        print(f"The Language is {self.language}")

    def getDetails(self):
        print("This is a Programmer.")           


e = Employee()
p = Programmer()

e.getDetails()   # =====> This is an Employee.
p.getDetails()   # =====> This is a Programmer.

# e.getLang()    # =====> Error 
p.getLang()      # =====> The Language is Python

