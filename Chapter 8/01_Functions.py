
# Noramal Way =======>
# ====================


marks1 = [43, 76, 56, 98, 55]
persentage1 = ((sum(marks1) / 500) * 100)

marks2 = [66, 96, 86, 80, 75]
persentage2 = (sum(marks2) / 500) * 100

print(persentage1, persentage2)



# By using Function =======>
# ==========================


def percent(marks):
    return((sum(marks) / 600) * 100)

marks3 = [43, 76, 54, 56, 98, 55]
persentage1 = percent(marks1)

marks4 = [66, 96, 56, 86, 80, 75]
persentage2 = percent(marks2)

print(persentage1, persentage2)


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


# Greeting Function =======>
# ==========================

def greet(name):
    print("Good Morning ,", name)

greet("Prashant")    
# =====> Good Morning , Prashant



# Sum of 2 Number by Function =======>
# ====================================

def sum(num1, num2):
    return(num1 + num2)


s = sum(34 , 45)
print(s)     # ======> 79



# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



# Default Parameter Function ============>
# ========================================


def greets(name = "Stranger"):
    print("Good Morning ,", name)

greets()