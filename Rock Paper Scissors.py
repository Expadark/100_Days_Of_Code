rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choice = [rock, paper, scissors]
pc = int(input("Type 0 for rock, 1 for paper, and 2 for scissors : "))

if pc == 0:
    print(rock)
elif pc == 1:
    print(paper)
elif pc == 2:
    print(scissors)

cc = random.randint(0 , 2)
cc1 = choice[cc]
print("Computer choose " + cc1)



if pc == 0 and cc == 1:
    print("You lose")
elif pc == 0 and cc == 2:
    print("You win")
elif pc == 0 and cc == 0:
    print("I's a draw")

if pc == 1 and cc == 0:
    print("You win")
elif pc == 1 and cc == 1:
    print(" It's a draw")
elif pc == 1 and cc == 2:
    print("You lose")

if pc == 2 and cc == 0:
    print("You lose")
elif pc == 2 and cc == 1:
    print("You win")
elif pc == 2 and cc == 2:
    print("It's a draw")