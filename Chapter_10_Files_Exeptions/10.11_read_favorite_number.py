import json

filename = 'fav_num_remembered.json'

try:
    with open(filename) as f:
        fav_numb = json.load(f)
except FileNotFoundError:
    favorite_number = input("Eneter your favorite number: ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
else:
    print(f"I know your favorite number --> {fav_numb}")
