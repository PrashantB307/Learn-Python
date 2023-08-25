



words = ['wonder', 'little', 'world', 'high']

with open('D:\Learn Python\Chapter 9\pr_04.txt') as f:
    text = f.read()

for word in words:
    content = text.replace(word, "@#$%^&*")    
    with open('D:\Learn Python\Chapter 9\pr_04.txt', 'w') as f:
        f.write(content)