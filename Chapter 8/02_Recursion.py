


# Find the Factorial of the given Number ==========>
# ==================================================


# Noramal Way ============>
# =========================

n = 5
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i
    i = i + 1

print(factorial)     # ====> 120



# By using Function ============>
# ===============================


def factorial(num):
    prod = 1
    for i in range(num):
        prod = prod * (i + 1)
    return factorial  

fact = factorial(5)
print(fact)   



# By using Recursion ============>
# ================================

def fact_rec(n):
    if n == 1 or n == 0:
        return n

    return n * fact_rec(n - 1)
 
factorial = fact_rec(5)
print(factorial)

# ====> 120