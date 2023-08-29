


# Sum of 2 number by using of OOPS =======>
# =========================================

class Number:
    def sum(n):
        return n.a + n.b
    
num = Number()
num.a = 20
num.b = 34
s = num.sum()
print(s)     # ====> 54


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


# Print Circle Area and Pepripheral using of OOPS =======>
# ========================================================


class Circle:
    def Area(n):
        print(f"Circle Area is {3.17 * n.r * n.r}")

    def Pepripheral(n):
        print(f"Circle Peripheral is {2 * 3.17 * n.r}")


circle = Circle()
circle.r = int(input("Enter the Radius :- "))
circle.Area()        # ====> Circle Area is 114.12
circle.Pepripheral() # ====> Circle Peripheral is 38.04



# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


class Employe:
    company = "Meta"
    def getSalary(self):
        print(f"Salary of p1 working in {self.company} is {self.salary}")


p1 = Employe()
p1.salary = 100000
p1.getSalary()

# ====> Salary of p1 working in Meta is 100000