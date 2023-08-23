



# Print First n Natural Numbers ========>
# =======================================
 
# By using of Function ===========>
# =================================

num = int(input("Enter Number :- "))

def sum(n):
    s = 0
    for i in range(n + 1):
        s = s + i
    return s
    
print ("Sum is :- ", sum(num))   


# By using of Recursion ===========>
# ==================================

def summ(n):
    if n == 0:
        return n
    
    return n + summ(n - 1)

print(summ(5))