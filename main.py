def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

def get_book_text(text):
    with open(text) as book:
        return book.read()
    
main()