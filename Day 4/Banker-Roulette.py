import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Using random.randint()
# num_names = len(names)
# choice = random.randint(0, num_names - 1)
# person_to_pay = names[choice]

# Using random.choice()
person_to_pay = random.choice(names)

print(f"{person_to_pay} is going to buy the meal today!")
