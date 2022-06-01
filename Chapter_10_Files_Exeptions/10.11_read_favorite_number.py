import json

favorite_number = input("Eneter your favorite number: ")
filename = 'fav_num.json'

with open(filename, 'w') as f:
    json.dump(favorite_number, f)
