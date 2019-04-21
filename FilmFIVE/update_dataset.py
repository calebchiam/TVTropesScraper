import json

with open("../Film/Film_tropes_dataset3.json", 'r') as f:
    dataset = json.load(f)

with open("tropes_FilmFIVE.json", 'r') as f:
    for line in f:
        entry = json.loads(line.strip("\n"))
        dataset.update(entry)

with open("../Film/Film_tropes_dataset3.json", 'w') as f:
    json.dump(dataset, f)