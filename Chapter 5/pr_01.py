

# Make a Hindi to English Dictionary =========>
# =============================================


myDict = {
    "Pankha" : "Fan",
    "Saman" : "Objects",
    "Kitab" : "Book",
    "Mej" : "Table"
}

print("Options are :- ", myDict.keys())

a = input("Enter the Hindi Word :- ")

print("English of Hindi word is :-", myDict.get(a))