

# Use Open Function to read the content of the File ======>
# =========================================================


f = open('D:\Learn Python\Chapter 9\sample.txt', 'r')
data = f.read()
print(data)
f.close()

# ====> Prashant is good Boy.
#       He is Good Programmer.

f2 = open('D:\Learn Python\Chapter 9\sample.txt')
text = f2.read(9)  # read first 5 characters from the file
print(text)
f2.close

# =====> Prashant



#  Readline Function ============>
# ================================

f3 = open('D:\Learn Python\Chapter 9\sample.txt')

# read first line
data = f3.readline()
print(data)

# read second line
data = f3.readline()
print(data)

# read third line
data = f3.readline()
print(data)

# # and so on ====>

# data = f3.readlines()
# print(data)