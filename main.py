def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main(get_book_text):
    print(get_book_text("books/frankenstein.txt"))

main(get_book_text)

from stats import word_count

def test():
    string = "string"
    letters = string.split()
    count = 0
    for i in letters:
        count += 1
    print(count)

test()