from string import ascii_lowercase as alc

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    text = text.lower()
    for char in alc:
        chars[char] = text.count(char)
    return chars

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report(book, word_count, chars_list):
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the book")
    print()
    for char in chars_list:
        print(f"The '{char["char"]}' character was found {char["num"]} times")
    print("--- End report ---")

main()