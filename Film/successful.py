import json

with open("Film_tropes_dataset3.json", 'r') as f:
    dataset = json.load(f)

with open("../titles/successful_books2.txt", 'w') as f:
    for k in dataset:
        f.write(k)
        f.write("\n")