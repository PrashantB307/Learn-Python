

myDict = {
    "Fast" : "I am Quick Learner",
    "Good" : "You are a Good Boy",
    "Marks" : [3, 5, 7, 9],
    "AnotherDict" : {
        'Name' : "Bhardwaj"
    },
    1 : 2
}


# keys() ===> (Print the keys of the Dictionary)
# ===================== X ======================

print(myDict.keys())
# ===> dict_keys(['Fast', 'Good', 'Marks', 'AnotherDict', 1])


# values() ===> (Print the keys of the Dictionary)
# ====================== X =======================

print(myDict.values())
# ===> dict_values(['I am Quick Learner', 'You are a Good Boy', [3, 5, 7, 9], 
#      {'Name': 'Bhardwaj'}, 2])


# items() ===> (Print the keys, values of the Dictionary)
# ========================== X ==========================

print(myDict.items())
# ===> dict_items([('Fast', 'I am Quick Learner'), ('Good', 'You are a Good Boy'), 
#      ('Marks', [3, 5, 7, 9]), ('AnotherDict', {'Name': 'Bhardwaj'}), (1, 2)])


# update() ===> (Add or Update the Dictionary by adding key - values Pair)
# =================================== X ==================================

updateDict = {
    "Motua" : "Friens",
    "4g" : "Friend"
}
myDict.update(updateDict)
print(myDict)
# ===> {'Fast': 'I am Quick Learner', 'Good': 'You are a Good Boy', 
#      'Marks': [3, 5, 7, 9], 'AnotherDict': {'Name': 'Bhardwaj'}, 1: 2, 
#      'Motua': 'Friens', '4g': 'Friend'}


# get() ===>
# ==========

print(myDict.get("4g"))
# ===> Friend

print(myDict.get("motuaa"))
# ===> None  ( Because motuaa is not avalible in the myDict )