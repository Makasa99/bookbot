def word_count():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        words = text.split()
        total_words = len(words)
        print(f"{total_words} words found in the document")

word_count()

def letter_count():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        words = text.split()
        for i in words:
            pass