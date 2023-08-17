


myDict = {
    "Fast" : "I am Quick Learner",
    "Good" : "You are a Good Boy",
    "Marks" : [3, 5, 7, 9],
    "AnotherDict" : {
        'Name' : "Bhardwaj"
    }
}

print(myDict["Fast"])     # ===> I am Quick Learner
print(myDict["Good"])     # ===> You are a Good Boy
print(myDict["Marks"])    # ===> [3, 5, 7, 9]

print(myDict["AnotherDict"])     # ===> {'Name': 'Bhardwaj'}
print(myDict["AnotherDict"]['Name'])    # ===> Bhardwaj

myDict["Marks"] = [45, 67, 87]
print(myDict["Marks"])    # ===> [45, 67, 87]


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

s = {}
print(type(s))  # ===> <class 'dict'>