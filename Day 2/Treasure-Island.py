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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

choice1 = input("You are at a crossroad. Where do you go? Type \"left\" or \"right\".\n").lower()

if choice1 == "left":
    print("You find yourself at the bank of a river with an island.")
    
    choice2 = input("Do you swim across or wait for a boat? Type \"swim\" or \"wait\".\n").lower()
    if choice2 == "wait":
        print("You are ferried safely across.")
        
        choice3 = input("You arrive at a house with 3 doors. Which do you open? \"blue\", \"yellow\" or \"red\".\n").lower()
        if choice3 == "yellow":
            print("Congratulations! You found the treasure.")
        elif choice3 == "red":
            print("It's a room full of fire. Game over!")
        elif choice3 == "blue":
            print("A large monster gobbles you up. Game over!")
        else:
            print("Game over!")

    else:
        print("You were attacked by a crocodile in the water. Game over!")
else:
    print("You fell into a ditch. Game over!")
