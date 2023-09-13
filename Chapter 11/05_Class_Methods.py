




class Employee:
    company = "Google"
    salary = 4532
    location = "Delhi"

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal


e = Employee()
e.changeSalary(6758)
print(e.salary)
