print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")
at_cross_road = input('you\'re at a cross road. Where do you want to go? Type "left" or "right" ')

if at_cross_road == "left":
    gate = input('You come to a lake. There is an island in the middle of the lake. Type  "wait" to wait for a boat. Type "swim" to swim across\n')
    if gate == "wait":
        door = input('You arrive at the island unharmed. there is a house with 3 doors. One red, one yellow and one blue. which colour do you choose?\n')
        if door == "Red":
            print("Burned by fire.\nGame Over.")
        elif door == "Blue":
            print("Eaten by beasts.\nGame Over.")
        elif door == "Yellow":
            print("You win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout")
else:
    print("Fall into a hole.\nGame Over.")
