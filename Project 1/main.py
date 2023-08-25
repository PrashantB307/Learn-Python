

# ROCK , PAPER, SCISSORS Game ===========>
# ========================================


import random


def game_Win(comp, you):

    if comp == you:
        return None
    
    if comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
        
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
        
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False  


print("Comp Turn : Rock(r) , Paper(p) or Scissors(s)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your Turn : Rock(r) , Paper(p) or Scissors(s)? ")

winner = game_Win(comp, you)

print("Comp Chooses :-", comp)
print("You Chooses :-", you)

if winner == None:
    print("The game is a tie!")
elif winner == True:
    print("You Win, Hurray!")
else:
    print("You Lose!")        




# # Snake Water Gun or Rock Paper Scissors =========>
# # =================================================


# def gameWin(comp, you):
#     # If two values are equal, declare a tie!
#     if comp == you:
#         return None

#     # Check for all possibilities when computer chose s
#     elif comp == 's':
#         if you=='w':
#             return False
#         elif you=='g':
#             return True
    
#     # Check for all possibilities when computer chose w
#     elif comp == 'w':
#         if you=='g':
#             return False
#         elif you=='s':
#             return True
    
#     # Check for all possibilities when computer chose g
#     elif comp == 'g':
#         if you=='s':
#             return False
#         elif you=='w':
#             return True

# print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
# randNo = random.randint(1, 3) 
# if randNo == 1:
#     comp = 's'
# elif randNo == 2:
#     comp = 'w'
# elif randNo == 3:
#     comp = 'g'

# you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
# a = gameWin(comp, you)

# print(f"Computer chose {comp}")
# print(f"You chose {you}")

# if a == None:
#     print("The game is a tie!")
# elif a:
#     print("You Win!")
# else:
#     print("You Lose!")


