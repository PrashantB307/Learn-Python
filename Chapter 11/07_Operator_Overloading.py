




class Number():
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num
    
    def __sub__(self, num2):
        print("Lets subtract")
        return self.num - num2.num
    
    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num
    
    def __truediv__(self, num2):
        print("Lets divide")
        return self.num / num2.num

n1 = Number(12)
n2 = Number(6)

sum = n1 + n2
print(sum)     # ====> 18

sub = n1 - n2
print(sub)     # ====> 6

multi = n1 * n2
print(multi)   # ====> 72

div = n1 / n2
print(div)     # ====> 2.0
 