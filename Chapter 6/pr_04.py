

# Check user Name contain less than 10 character or not ========>
# ===============================================================
 

str = input("Enter Your Name :- ")
len = len(str)

if(len < 10):
    print("Your name contain less than 10 characters")
elif(len == 10):
    print("Your name contain  10 characters")   
else:
    print("Your name contain greater than 10 characters")   