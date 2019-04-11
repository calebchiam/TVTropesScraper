import os, json


with open("Literature/Literature_tropes_dataset3.json", 'r') as f:
    lit = json.load(f)


with open("Film/Film_tropes_dataset3.json", 'r') as f:
    film = json.load(f)

tropes = set()

for _, v in lit.items():
    for trope in v:
        tropes.add(trope)

for _, v in film.items():
    for trope in v:
        tropes.add(trope)

with open("tropes_titles2.txt", 'w') as f:
    for trope in tropes:
        f.write(trope)
        f.write("\n")