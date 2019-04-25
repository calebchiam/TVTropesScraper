import json
import editdistance

with open("../Literature/Literature_tropes_dataset3.json", 'r') as f:
    dataset = json.load(f)

film_titles = sorted([f for f in dataset])

prev = ""

for title in film_titles:
    if editdistance.eval(title, prev) == 4:
        print((prev, title))
    prev = title
