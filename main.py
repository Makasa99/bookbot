def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main(get_book_text):
    print(get_book_text("books/frankenstein.txt"))

main(get_book_text)

from stats import word_count
from stats import letter_count