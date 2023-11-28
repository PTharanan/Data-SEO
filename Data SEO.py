import json  # Use python lib
from difflib import get_close_matches

jsonfile = json.load(open('Details.json'))  # Open json file
word = input('Enter:-').lower()  # Get value


def check(data):  # Function creation
    if data in jsonfile:
        return jsonfile[data]
    elif len(get_close_matches(data, jsonfile.keys())) > 0:
        a = input("did you mean: %s " % get_close_matches(data, jsonfile.keys())[0]).lower()
        if a == 'y':
            return jsonfile[get_close_matches(data, jsonfile.keys())[0]]
        elif a == 'n':
            pass
        else:
            print('f')

    else:
        return 'no value'


result = (check(word))  # Function calling
if type(result) == list:   # Get output oder
    for i in result:
        print(i)
else:
    print(result)
