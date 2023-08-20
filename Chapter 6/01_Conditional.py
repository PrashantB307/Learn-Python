

#  if-elif-else  Ladder in Python =====>
# ======================================

a = 45

if(a < 5):
    print("The value of a is less than 5")
elif(a < 60):
    print("The value of a is less than 60")
elif(a > 40):
    print("The value of a is Greater than 40")
else:
    print("The value of a is Greater")        



#  Multiple if statement =====>
# =============================

b = 35

if(b < 5):
    print("The value of a is less than 5")

if(b > 60):
    print("The value of a is Greater than 60")

if(b < 40):
    print("The value of a is less than 40")
else:
    print("The value of a is Greater")   





age = int(input("Enter ypur age :- "))

if(age >= 18):
    print("You are Eligible for voting.")
else:
    print("You are not Eligible for voting.")



# Logiacal & Relational Operators ======>
# =======================================


age = int(input("Enter ypur Age :- "))

if(age >= 18 and age <= 25):
    print("You are aligible for this Job.")
else:
    print("You are not aligible for this Job.")




age = int(input("Enter ypur Age :- "))

if(age >= 18 or age <= 60):
    print("You are aligible for this Job.")
else:
    print("You are not aligible for this Job.")