

for i in range(2, 21):
    with open(f"D:\Learn Python\Chapter 9\pr_03.Table/Table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i} X {j} = {i * j}\n")
