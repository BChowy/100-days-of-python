import pandas

data = pandas.read_csv('./nato_phonetic_alphabet.csv')
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonic():
    word = input("Enter a word: ").upper()
# while True:
    try:
        result = [new_dict[letter] for letter in word]
    except KeyError:
        print("Please enter letters ONLY.")
        # word = input("Enter a word: ").upper()
        generate_phonic()
    else:
        print(result)
        # break
