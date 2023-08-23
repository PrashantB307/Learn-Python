


# Find Greatest Number in given Numbers =========>
# ================================================

def greatest_Num(num1, num2, num3):
    if(num1 > num2 and num1 > num3):
        return num1
    elif(num2 > num3):
        return num2
    else:
        return num3 
    
num = greatest_Num(34, 78, 56)
print("Greatest Number is :-", num)   

# ====> Greatest Number is :- 78