import json

with open("Film_tropes_dataset.json", 'r') as f:
    a = json.load(f)
    print(type(a))
    print(len(a))
