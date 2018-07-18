# Ania

import json
from difflib import SequenceMatcher, get_close_matches
data=json.load(open("data.json","r"))

# def search(word):
#     return data[word]
#
# word=input("Enter the word: ")
# try:
#     search(word)
#     output = ""
#     for i in search(word):
#         output = output + i + "\n"
#     print(output)
# except KeyError:
#     print("No such word in the dictionary")

def search2(word):
    word=word.lower()
    ratio = 0
    output = ""
    if word in data:
        for i in data[word]:
            output = output + i + "\n"
        return output
    else:
        for key in data:
            ratio1 = SequenceMatcher(None, key, word).ratio()
            if ratio1 > ratio:
                ratio = ratio1
                b = key
        if ratio < 0.5:
            return "No such word in the dictionary"
        else:
            print("Did you mean " + b + "? Press Y if yes and N if No:")
            answer = input(" ").lower()
            if answer == "y":
                for i in data[b]:
                    output = output + i + "\n"
                return output

def search3(word):
    word=word.lower()
    output = ""
    if word in data:
        for i in data[word]:
            output = output + i + "\n"
        return output
    else:
        guess = get_close_matches(word, data.keys(),cutoff=0.8)
        if guess == []:
            return "No such word in the dictionary"
        else:
            yn = input("Did you mean %s ? Press Y if yes and N if No: " % guess[0]).lower()
            if yn == "y":
                for i in data[guess[0]]:
                    output = output + i + "\n"
                return output
            elif yn == "n":
                return "No such word in the dictionary"
            else:
                return "We didn't understand your entry"

def search4(word):
    word=word.lower()
    output = ""
    if word in data:
        for i in data[word]:
            output = output + i + "\n"
        return output
    elif get_close_matches(word, data.keys(), cutoff=0.8)==[]:
        return "No such word in the dictionary"
    else:
        guess = get_close_matches(word, data.keys(), cutoff=0.8)
        yn = input("Did you mean %s ? Press Y if yes and N if No: " % guess[0]).lower()
        if yn == "y":
            for i in data[guess[0]]:
                output = output + i + "\n"
            return output
        elif yn=="n":
            return "No such word in the dictionary"
        else:
            return "We didn't understand your entry"




# word=input("Enter the word: ")
# print(search3(word))


def search5(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif get_close_matches(word, data.keys(), cutoff=0.8)==[]:
        return "No such word in the dictionary"
    else:
        guess = get_close_matches(word, data.keys(), cutoff=0.8)
        yn = input("Did you mean %s ? Press Y if yes and N if No: " % guess[0]).lower()
        if yn == "y":
            return data[guess[0]]
        elif yn=="n":
            return "No such word in the dictionary"
        else:
            return "We didn't understand your entry"

quess_word = input("Enter the word: ")
output = search5(quess_word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)