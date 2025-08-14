print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first = input("You arrive at a crossroads, do you go left or right?\n       Type 'left' or 'right' ").lower()
if first == "left":
    print("You continue along the path until you come to a lake,"
          " you can wait for a boat or try to swim across")
    second = input("Type 'wait' or 'swim' ").lower()
    if second == "swim":
        print("You swim across the lake and find "
              "a house with 3 doors, red, yellow, and blue")
        third = input("Type 'red', 'yellow', or 'blue' ").lower()
        if third == "yellow":
            print("You found the treasure! YOU WIN")
        else:
            print("You open the door to find a room full of"
                  " several thousand bees that sting you to death\n GAME OVER")
    else:
        print("You see a boat approaching, you ask for a ride across "
              "the lake and are immediate shot by the captain\n       GAME OVER")

else:
    print("You choose the path to the right, and are attacked by a bear and die\n   GAME OVER")

input("")