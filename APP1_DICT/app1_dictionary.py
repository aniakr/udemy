# my version of dictionary search

import json
from difflib import SequenceMatcher, get_close_matches
data=json.load(open("data.json","r"))

def search_dictionary(word):
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