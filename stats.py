# function to count the words in a string
def get_word_count(content_string):
    # capture the word count
    word_count_int = 0
    words_list = content_string.split()
    for word_string in words_list:
        word_count_int += 1
    return word_count_int

# function that counts the occurences of a character in a string, captures it in a string -> int dict
def get_count_chars(content_string):
    character_dict = {}
    content_string = content_string.lower()
    # iterate over string
    for character_char in content_string:
        if character_char not in character_dict:
            character_dict[character_char] = 0
        if character_char in character_dict:
            character_dict[character_char] += 1
    return character_dict

def count_helper(dict):
    return list(dict.values())[0]
    

# function to sort dict of characters and their count descending
def sort_char_count(character_dict):
    character_count_sorted = []
    for i in character_dict:
        tmp = {}
        tmp[i] = character_dict[i]
        character_count_sorted.append(tmp)

    character_count_sorted.sort(reverse=True, key=count_helper)
    return character_count_sorted

def print_report(dict_list, file_path_string, word_count_int):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path_string}")
    print("----------- Word Count ----------")
    print(f"Found {word_count_int} total words")
    print("--------- Character Count -------")
    for pair in dict_list:
        for key in pair:
            if key.isalpha() == True:
                print(f"{key}: {pair[key]}")
    print("============= END ===============")
