




# Find the File "Sample" and "Copy" or "Poems" and "Log File " are identical Same or not =====>
# ==============================================================================================

f1 = 'D:\Learn Python\Chapter 9\sample.txt'
f2 = 'D:\Learn Python\Chapter 9\copy.txt'
f3 = 'D:\Learn Python\Chapter 9\pr_01_poems.txt'
f4 = 'D:\Learn Python\Chapter 9\pr_06_Log_File.txt'

with open(f1) as f:
    text1 = f.read()

with open(f2) as f:
    text2 = f.read()

if(text1 == text2):
    print("f1 & f2 are same.")
else:
    print("f1 & f2 are not same.")        

with open(f3) as f:
    text1 = f.read()

with open(f4) as f:
    text2 = f.read()

if(text1 == text2):
    print("f3 & f4 are same.")
else:
    print("f3 & f4 are not same.")            