import pandas
# TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
# word_list = []
# for letter in user_input:
#     for (alpha, word) in alpha_dict.items():
#         if letter == alpha:
#             word_list.append(word)
word_list = [alpha_dict[letter] for letter in user_input]
print(word_list)
