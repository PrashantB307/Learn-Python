


# Replace the Word "Twinkle" from the Poem with "@#$%^&*" =======>
# ================================================================


with open('D:\Learn Python\Chapter 9\pr_04.txt') as f:
    text = f.read()

content = text.replace("Twinkle", "@#$%^&*")    

with open('D:\Learn Python\Chapter 9\pr_04.txt', 'w') as f:
    f.write(content)