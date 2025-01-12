

def read_book(book_name):
    with open(f'books/{book_name}.txt', 'r') as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text):
    words_list = book_text.split()
    words_count = len(words_list)
    return words_count

def count_character(book_text):
    character_count = {}
    book_text = book_text.lower()
    for c in book_text:
        if c.isalpha():
            if c not in character_count.keys():
                character_count[c] = 1
            else:
                character_count[c] += 1
    return character_count

def sort_key(dictionary):
    return dictionary['num']

def convert_dict_to_list(old_dictionary):
    new_list = []
    for c,v in old_dictionary.items():
        new_list.append({'name':c , 'num': v})
    new_list.sort(reverse=True, key = sort_key)
    return new_list

def summarize_book(book_text):
    words_count = count_words(book_text=book_text)
    character_count = count_character(book_text=book_text)
    new_character_count = convert_dict_to_list(old_dictionary = character_count)
    print(f'{words_count} words found in the document')
    for c in new_character_count:
        print(f"The {c['name']} character was found {c['num']} times")

def main():
    book_name = "frankenstein"
    book_text = read_book(book_name=book_name)
    words_count = count_words(book_text=book_text)
    character_count = count_character(book_text=book_text)
    summarize_book(book_text =  book_text)

main()