


def game(n):
    return n

num = int(input("Enter the Score :- "))

score = game(num)

with open('D:\Learn Python\Chapter 9\pr_02_score.txt') as f:
    hiscore = int(f.read())

if hiscore < score:
    with open('D:\Learn Python\Chapter 9\pr_02_score.txt', 'w') as f:
        f.write(str(score))    

newHscore = open('D:\Learn Python\Chapter 9\pr_02_score.txt')
print("new Hish Score is :-", newHscore.read())
newHscore.close()