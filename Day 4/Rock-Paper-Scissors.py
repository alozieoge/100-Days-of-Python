import random

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

choices = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player >= 3 or player < 0:
  print("You typed an invalid number. You lose :(") 
else:
  computer = random.randint(0, 2)
  
  print(choices[player])
  print(f"Computer chose:\n{choices[computer]}")

  if player == 0 and computer == 2:
    print("You win :)")
  elif player == 2 and computer == 0:
    print("You lose :(")
  elif computer > player:
    print("You lose :(")
  elif player > computer:
    print("You win :)")
  elif computer == player:
    print("It's a draw :|")


#score = ""

# if player == 0 and computer != 0:
#   if computer == 1:
#     score = "You lose! :("
#   elif computer == 2:
#     score = "You win! :)"

# elif player == 1 and computer != 1:
#   if computer == 2:
#     score = "You lose! :("
#   elif computer == 0:
#     score = "You win! :)"

# elif player == 2 and computer != 2:
#   if computer == 0:
#     score = "You lose! :("
#   elif computer == 1:
#     score = "You win! :)"

# else:
#   score = "It's a draw! :|"





