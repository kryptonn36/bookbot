import sys
from stats import get_num_words
from stats import get_num_char
from stats import sorting

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text (path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    
    file_contents = get_book_text(sys.argv[1])
    get_num_words(file_contents)

    print("--------- Character Count -------")
    dict_count = sorting(get_num_char(file_contents))
    for each in dict_count:
        print(f"{each}: {dict_count[each]}")


main()