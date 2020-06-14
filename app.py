import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def definition(_word, _data=data):
    _word=_word.lower()
    if _word in _data:
        return _data[_word]
    elif _word not in _data:
        try:
            simWords=get_close_matches(_word,_data.keys(),n=3)
            for item in simWords:
                correct=input(f"Did you mean {item}? Type yes or no: ").lower()
                if correct=="yes":
                    return _data[item]
                elif correct=="no":
                    pass
                else:
                    print("Invalid entry.")
                    break
            if correct !="yes":
                return ["Word not found."]
        except:
            return ["Word not found."]
    else:
        return ["Word not found."]

try:
    word = input("Enter a word: ")
except:
    print("Invalid entry. Make sure to enter a word.")

for item in definition(word):
    print(item)
#print(definition(word))