



class Employe:
    
    company = "Google"
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit

    def getDetails(self):
        print(f"Name of Employe is {self.name}")
        print(f"Salary of Employe is {self.salary}")
        print(f"Subunit of Employe is {self.subunit}")

    
p1 = Employe("Prashant", 100000, "YouTube")
p1.getDetails()

# ====>  Name of Employe is Prashant
#        Salary of Employe is 100000
#        Subunit of Employe is YouTube