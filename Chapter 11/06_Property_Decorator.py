




class Employee:
    company = "Google"
    salary = 4532
    salaryBonus = 765

    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus


e = Employee()
print(e.totalSalary)