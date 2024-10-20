def main():
    book_path = "books/frankenstein.txt"
    print(get_book_text(book_path))
    print(get_word_count(book_path))
    print(get_char_count(book_path))

def get_book_text(text):
    with open(text) as book:
        return book.read()

def get_word_count(text):
    return len(get_book_text(text).split())

def get_char_count(text):
    char_count = {chr(i): 0 for i in range(97, 123)}
    char_case = get_book_text(text).lower()
    for char in char_case:
        if char in char_count:
            char_count[char] += 1
    return char_count

main()