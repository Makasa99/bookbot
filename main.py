import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main(get_book_text):
    print(get_book_text(sys.argv[1]))

main(get_book_text)
print("============ BOOKBOT ============")
print(f"Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
from stats import word_count
print("--------- Character Count -------")
from stats import sort_letter_count
print("============= END ===============")