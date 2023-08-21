


# Check the Number is Prime or not ======>
# ========================================

num = int(input("Enter the Number :- "))

count = 1
for i in range(2, num + 1):
    if(num % i == 0):
        count = count + 1

if count == 2:
    print("Number is Prime")
else:
    print("Number is not Prime")           