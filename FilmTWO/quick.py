import json, os

trope2simplified = dict()

with open("../Film/fixednames/combined_fixednames.json", 'r') as f:
    for line in f:
        entry = json.loads(line)
        trope2simplified[entry["trope"]] = entry["name"]

with open("updated_tropes_FilmTWO.json", 'w') as f0:
    with open("tropes_FilmTWO.json", 'r') as f:
        for line in f:
            entry = json.loads(line)
            key = next(iter(entry.keys()))
            vals = next(iter(entry.values()))
            json.dump({trope2simplified[key]: vals}, f0)
            f0.write("\n")

