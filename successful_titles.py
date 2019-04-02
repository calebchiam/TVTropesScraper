import pickle
import json

jsons = ["Literature/tropes_Literature.json", "Theatre/tropes_Theatre.json"]

with open('book_titles_s2f.pickle', 'rb') as handle:
    translator = pickle.load(handle)

retval = []
for j in jsons:
    with open(j, 'r') as f:
        for line in f:
            entry = json.loads(line)
            retval.append(translator[next(iter(entry.keys()))])

with open("successful_books.txt", 'w') as f:
    for title in retval:
        f.write(title)
        f.write("\n")