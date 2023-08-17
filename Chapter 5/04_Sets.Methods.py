

# s = {1, 3, 5, 7}

# # Adding values in Set =====>
# # ===========================

# # add() ====> ( Adding values in Set )
# # ================ X =================

# s.add(8)
# s.add(76)
# print(s)    # ====. {1, 3, 5, 7, 8, 76}


# # len() ====> (Print thge length of the set)
# # =================== X ====================

# print(len(s))    # ====> 6


# # remove() ====> (Remove elementg form the set )
# # ===================== X ======================

# s.remove(5)
# print(s)     # ====> {1, 3, 7, 8, 76}



# # pop() =====> (Remove 1st element from the set)
# # ===================== X ======================

# s.pop()
# print(s)     # ====> {3, 7, 8, 76}


# # clear() =====> (Clear all element from the set)
# # ===================== X =======================

# s.clear()
# print(s)     # set()



# union() ====> ( Return the new set with all elements)
# ======================= X ==========================

a = {4, 67, 65, 34}
b = {82, 65, 99}
print(a.union(b))    # ====> {65, 34, 67, 4, 82, 99}



# intersection() ====> ( Return the new set with common elements)
# ============================= X ===============================

a = {4, 67, 65, 34}
b = {82, 65, 99}
print(a.intersection(b))     # ====> {65}