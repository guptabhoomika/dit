import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def definition(w):
    w = w.lower() 
    if w in data:
        return data[w]
    elif w.title()in data:
        return data[w.title()]
    elif w.upper()in data:
        return data[w.upper()]        
    elif len(get_close_matches(w,data.keys())) > 0:
        yn=input("did you mean %s . enter Y if yea and N if no" % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return"The word doesnt exist in dictionary" 
        else:
            return "did not understand"  
    else:
        return "The word doesnt exist in dictionary" 

word = input("enter word to be searched ")
op = definition(word)
if type(op) == list:
    for item in op:
        print(item)
else:
    print(op)