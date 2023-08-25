

# Find the word "Little" is present in Poem.txt file or not ===>
# ==============================================================


f = open('D:\Learn Python\Chapter 9\pr_01_poems.txt')
t = f.read()
if 'little' in t :
    print("Little is Present.")
else:
    print("Little is not Present.")

f.close()       

