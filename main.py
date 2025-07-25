from stats import get_book_text
from stats import count_words
from stats import letter_stats
from stats import sort_dictionary
from stats import final_report
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 main.py <path_to_book>")

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    count = count_words(book_path)
    letters = letter_stats(text)
    sort = sort_dictionary(letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    print(final_report(sort))
    print("============= END ===============")


main()
