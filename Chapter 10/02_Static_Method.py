




class Employe:
    company = "Google"
    def getSalary(self):
        print(f"Salary of p1 is {self.salary}")
    
    def Name(self):
        print(f"Name of p1 is {self.name}")
    
    @staticmethod   # Use staticmethod when not use "self"
    def greet():
        print("Good Morning, Sir")



p1 = Employe()

p1.salary = 100000
p1.getSalary()
# ====> Salary of p1 is 100000

p1.name = "Prashant"
p1.Name()
# ====> Name of p1 is Prashant

p1.greet()
# ====> Good Morning, Sir
