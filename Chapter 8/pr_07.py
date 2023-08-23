


# Write a function to remove a given word from the list and strip it ===>
# =======================================================================


def remove_and_strip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "       My Name is P1    "
n = remove_and_strip(this, "Name")
print(n)