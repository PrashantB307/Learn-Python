



# Find the Line of word "Prashant" in the LOG File  =======>
# ==========================================================

word = 'Prashant'
text = True
i = 1
with open("D:\Learn Python\Chapter 9\pr_06_Log_File.txt") as f:
    while text:
        text = f.readline()

        if word in text:
            print("Found")
            print(i)

        i += 1    