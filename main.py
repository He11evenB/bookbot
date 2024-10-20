def main():
    book_path = "books/frankenstein.txt"
    print(get_book_text(book_path))
    print(get_word_count(book_path))


def get_book_text(text):
    with open(text) as book:
        return book.read()

def get_word_count(text):
    with open(text) as book:
        return len(book.read().split())

main()