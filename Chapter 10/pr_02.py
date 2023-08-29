




class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"Square of {self.num} is {self.num **2}")

    def cube(self):
        print(f"Cube of {self.num} is {self.num **3}")

    def sqrRoot(self):
        print(f"SquareRoot of {self.num} is {self.num **0.5}")


a = Calculator(4)
a.square()
# ====> Square of 4 is 16

a.cube()
# ====> Cube of 4 is 64

a.sqrRoot()    
# ====> SquareRoot of 4 is 2.0