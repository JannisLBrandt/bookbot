import sys
from stats import get_word_count
from stats import get_count_chars
from stats import sort_char_count
from stats import print_report

# function to extract book text into a single string
def get_book_text(file_path):
    content_string = ""
    with open(file_path) as f:
        content_string = f.read()
    return content_string


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    file_path = sys.argv[1]
    content_string = get_book_text(file_path)
    word_count = get_word_count(content_string)
    count_char_dict = get_count_chars(content_string)
    sorted_count_list = sort_char_count(count_char_dict)
    print_report(sorted_count_list, file_path, word_count)
    
    

main()
