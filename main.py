def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)

    print(f"{num_words} words found in the document")
    for char in dict(sorted(num_letters.items())):
        if char.isalpha():
            print(f"the charater : {char} was found {num_letters[char]} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    all_letters = {}

    for letter in text.lower():
        if (letter in all_letters):
            all_letters[letter] += 1
        else:
            all_letters[letter] = 1

    return all_letters

main()