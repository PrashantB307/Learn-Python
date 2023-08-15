

# Sort ===>
# =========

l1 = [2, 4, 54, 34, 20, 65, 9]
print("Before Sort: ")
print(l1)    # ==> [2, 4, 54, 34, 20, 65, 9]
l1.sort()
print("After Sort: ")
print(l1)    # ==> [2, 4, 9, 20, 34, 54, 65]



# Reverse ===>
# ============

l2 = [2, 4, 9, 20, 34, 54, 65]
l2.reverse()
print(l2)    # ==> [65, 54, 34, 20, 9, 4, 2]



# Append ===> (Add the element at the end of the list)
# ===================== X ===========================

l3 = [2, 4, 54, 34, 20, 65, 9]
l3.append(88)
print(l3)    # ==> [2, 4, 54, 34, 20, 65, 9, 88]



# Insert ===> (Add the element at the given index)
# ===================== X ========================

l4 = [2, 4, 54, 34, 20, 65, 9]
l4.insert(3, 999)
print(l4)     # ==> [2, 4, 54, 999, 34, 20, 65, 9]



# Pop ===> (Delete the element at the given index)
# ===================== X =======================

l5 = [2, 4, 54, 34, 20, 65, 9]
l5.pop(3)
print(l5)    # ==> [2, 4, 54, 20, 65, 9]



# Remove ===> (Delete the element)
# =============== X ==============

l6 = [2, 4, 54, 34, 20, 65, 9]
l6.remove(54)
print(l6)      # ==> [2, 4, 34, 20, 65, 9]