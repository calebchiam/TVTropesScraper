import json

with open("../Film/Film_tropes_dataset2.json", 'r') as f:
    dataset = json.load(f)

print(len(dataset))
with open("tropes_FilmFOUR.json", 'r') as f:
    for line in f:
        entry = json.loads(line)
        dataset.update(entry)

print(len(dataset))

with open("Film_tropes_dataset3.json", 'w') as f:
    json.dump(dataset, f)