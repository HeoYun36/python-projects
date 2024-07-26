import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_alphabet():
    user_input = input("Enter a word: ").upper()
    try:
        word_list = [alpha_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_alphabet()
    else:
        print(word_list)


generate_alphabet()
