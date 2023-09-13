



class Number():

    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"Decimal Number : {self.num}"
    
    def __len__(self):
        return 1
    

n = Number(68)
print(n)       # ======> Decimal Number : 68

print(len(n))  # ======> 1