import json # required to read data.json
from difflib import get_close_matches # to check for similar words in data.json if 

## Functions
def definition(_word):
    """Takes user input string. Searches for string in data.json. Checks for similar strings if not found. Returns definition.

    Args:
        _word (string): user entered word

    Returns:
        (list): list of definitiions
    """    
    # Load dictionary from data.json
    data = json.load(open("data.json"))
    
    # Forcing user input to lowercase to search data.json
    _word=_word.lower()

    # Word found
    if _word in data:
        return data[_word]
    
    # Word not found. Check for up to 3 similar words using get_close_matches()
    elif _word not in data:
        try:
            simWords=get_close_matches(_word,data.keys(),n=3)
            for item in simWords:
                correct=input(f"Did you mean {item}? Type yes or no: ").lower()
                if correct=="yes":
                    return data[item]
                elif correct=="no":
                    pass
                else:
                    return ["Invalid entry."]
                    break
            if correct !="yes":
                return ["Word not found."]
        except:
            return ["Word not found."]
    # No similar words found
    else:
        return ["Word not found."]


## Run program
word = input("Enter a word: ")

# Since definition() returns a list, program iterates through list to print each found definition
for item in definition(word):
    print(item)