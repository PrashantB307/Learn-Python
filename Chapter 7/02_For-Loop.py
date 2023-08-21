

# Print Fruits list by use of For loop =====>
# ===========================================


fruits = ["Banana", 'Apple', 'Mango', 'Guava', 'Grapes', 'Orange', 'Pine-Apple']

for items in fruits:
    print(items)
# ====> Banana, Apple, Mango, Guava, Grapes, Orange, Pine-Apple


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


# Range Function  =========>
# ==========================


# range(start idx, last idx)  ====>

for i in range(1, 10):
    print(i)      # ====> Print no. from 1 to 9
# ====> 1, 2, 3, 4, 5, 6, 7, 8, 9


# range(start idx, last idx, step size) ====>

for i in range(0, 12, 2):
    print(i)
# ====> 0, 2, 4, 6, 8, 10


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


# For with else =========>
# ========================


for i in range(10):
    print(i)
else:
    print("You are Dead!")

# ====> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# ====> You are Dead!


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


# Break Statement =========>
# ==========================

for i in range(10):
    print(i)
    if i == 5:
        break

# ====> 0, 1, 2, 3, 4, 5


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


# Continue Statement =========>
# =============================

for i in range(10):
    if i == 5:
        continue
    print(i)

# ====> 0, 1, 2, 3, 4, 6, 7, 8, 9



# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


# Pass Statement =========>
# =========================


i = 4
if i > 10:
    pass
else:
    print("You are Big")

# =====> You are Big     