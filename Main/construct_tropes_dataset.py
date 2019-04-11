import json

tropes_description_dataset = dict()

with open("tropes_descriptions.json", 'r') as f:
    for line in f:
        entry = json.loads(line.strip("\n"))
        tropes_description_dataset.update(entry)

with open("../Main2/tropes_descriptions.json", 'r') as f:
    for line in f:
        entry = json.loads(line.strip("\n"))
        tropes_description_dataset.update(entry)

with open("tropes_description_dataset.json", 'w') as f:
    json.dump(tropes_description_dataset, f)