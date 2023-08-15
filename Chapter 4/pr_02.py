


# Accept marks of 6 student in sorted manner ====> 
# ================================================

m1 = int(input("Enter 1st Student Marks :- ")) 
m2 = int(input("Enter 2st Student Marks :- ")) 
m3 = int(input("Enter 3st Student Marks :- ")) 
m4 = int(input("Enter 4st Student Marks :- ")) 
m5 = int(input("Enter 5st Student Marks :- ")) 
m6 = int(input("Enter 6st Student Marks :- ")) 

allMarks = [m1, m2, m3, m4, m5, m6]
print("Befor sort :- " , allMarks)

allMarks.sort()
print("After Sort :- " , allMarks)
