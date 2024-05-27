def main():
    book_path = "books/frankenstein.txt"
    book = get_book(book_path)
    count_words = word_count(book)
    counted_letters = count_letters(book)
    letters_sorted = dic_to_list(counted_letters)
    
    print(book)
    print()
    print(f"{count_words} words found in the book")
    print()
    print(counted_letters)
    print()
    for l in letters_sorted:
        if not l["letter"].isalpha():
            continue
        print(f"The '{l["letter"]}' character was found {l["num"]} times")

def get_book(path):
    with open(path) as f:
        return f.read()
    
def word_count(book):
    words = book.split()
    return len(words)

def count_letters(book):
    uncap_book = book.lower()
    letter_count = {}
    for letters in uncap_book: 
        if letters in letter_count:
            letter_count[letters] += 1
        else:
            letter_count[letters] = 1
    return letter_count

def sorted_count(dic):
    return dic["num"]

def dic_to_list(letter_count):
    sorted_list = []
    for letters in letter_count:
        sorted_list.append({"letter": letters, "num": letter_count[letters]})
    sorted_list.sort(reverse=True, key=sorted_count)
    return sorted_list
      

main()