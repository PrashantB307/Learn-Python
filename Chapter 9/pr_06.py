



# Find the word "Prashant" in the LOG File =======>
# =================================================

word = 'Prashant'
with open("D:\Learn Python\Chapter 9\pr_06_Log_File.txt") as f:
    text = f.read()

if word in text:
    print("Found!")
else:
    print("Not found")    