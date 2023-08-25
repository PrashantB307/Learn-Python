




# Make a copy of the Sample.txt File ========>
# ============================================

with open("D:\Learn Python\Chapter 9\sample.txt") as f:
    text = f.read()

with open("D:\Learn Python\Chapter 9\copy.txt", 'w') as f:
    f.write(text)    