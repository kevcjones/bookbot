from collections import Counter

def read_book(bookName):
    with open(f'books/{bookName}.txt', 'r') as file:
        text = file.read()
        return text

def count_words(text):
    return len(text.split())

def count_letters(text):
    characters = Counter(char.lower() for char in text if char.isalpha())
    return dict(characters)
    
    
def print_report(book_name):
    book = read_book(book_name)

    print(f"--- Begin report of books/{book_name}.txt ---")
    print(f"{count_words(book)} words found in the document")
    print("")

    letter_dict = count_letters(book)
    for letter in sorted(letter_dict):
        print(f"The '{letter}' character was found {letter_dict[letter]} times")


print_report('frankenstein')