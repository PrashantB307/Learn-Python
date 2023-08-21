


# Print the Following Pattern ======>
# ===================================
#          *
#        * * *  
#      * * * * *

num = int(input("Enter the Number :- "))

for i in range(num):
    print(" " * (num - i - 1), end = "")
    print("*" * (2 * i + 1), end = "")
    print(" " * (num - i - 1))
