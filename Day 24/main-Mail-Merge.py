# TODO: Create a letter using starting_letter.docx
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.readlines()

# for each name in invited_names.txt
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

greeting = letter[0]
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
for name in names:
    letter[0] = greeting.replace("[name]", name.strip())
    with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as file:
        file.writelines(letter)

