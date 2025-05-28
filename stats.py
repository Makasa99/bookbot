import sys

def word_count():
    with open(sys.argv[1]) as f:
        text = f.read()
        words = text.split()
        total_words = len(words)
        print(f"Found {total_words} total words")

word_count()

letters = {}

def letter_count():
    with open(sys.argv[1]) as f:
        text = f.read().lower()
        #letters = {}
        for i in text:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
        #print(letters)
        return letters

letter_count()

def sort_on(dict):
    return dict["num"]

def sort_letter_count():
    sorted_letters = []
    for i in letters:
        if i.isalpha():
            sorted_letters.append({"char": i, "num": letters[i]})
            sorted_letters.sort(reverse=True, key=sort_on)
    for i in sorted_letters:
        print(f"{i["char"]}: {i["num"]}")



sort_letter_count()