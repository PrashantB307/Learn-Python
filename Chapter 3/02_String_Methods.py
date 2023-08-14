
# String Concatenation :--
# ========================

greeting = "Good Morning "
name = "Prashant"
c = greeting + name  
print(c)          # ==> Good Morning Prashant


# String Slicing :--  strname[start index : last index]
# ===================== X =============================

Name = "Bhardwaj"

print(Name[2])     # ==> a
print(Name[0:3])   # ==> Bha
print(Name[1:3])   # ==> ha

print(Name[:4])    # ==> Bhar ( Its same is Name[0:4])
print(Name[0:])    # ==> Bhardwaj (Its same is Name[0:8])



# String with Skip Value :-- 
# ==========================

name = "Prashant"

word = name[1:6:2]    # ==> skip every (2 --> 2nd) second value
print(word)         # ==> rsa


# String Escape Sequences :-- 
# ===========================

#     \n  --> For print new Line
#     \t  --> For print tab

story = "Prashant is good in Study.\nHe is also good in study."
print(story)
# Prashant is good in Study.
# He is also good in study.

story = "He is also good \tin study."
print(story)
# He is also good         in study.