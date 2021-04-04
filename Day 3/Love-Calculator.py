#  A program that tests the love compatibility between two people 🥰
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1 + name2
names_lower = names.lower()

true_count = names_lower.count("t") + names_lower.count("r") + names_lower.count("u") + names_lower.count("e")
love_count = names_lower.count("l") + names_lower.count("o") + names_lower.count("v") + names_lower.count("e")

score_str = str(true_count) + str(love_count)
score = int(score_str)

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
