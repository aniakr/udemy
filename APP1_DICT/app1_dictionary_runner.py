from APP1_DICT.app1_dictionary import search_dictionary

quess_word = input("Enter the word: ")
output = search_dictionary(quess_word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)