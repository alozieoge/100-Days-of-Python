# Locate the treasure in a 3x3 grid based on the pirate's input - "arrrgh!"
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Write your code below this row 👇
column = int(position[0])
row = int(position[1])

map[row - 1][column - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
