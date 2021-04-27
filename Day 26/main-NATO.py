import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data)
nato_dict = {row["letter"]: row["code"] for (index, row) in nato_data.iterrows()}
# print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()
code_words = [nato_dict[letter] for letter in user_word]
print(code_words)
