import json

filename = 'fav_num.json'

with open(filename) as f:
    fav_numb = json.load(f)
    print(f"I know your favorite number --> {fav_numb}")