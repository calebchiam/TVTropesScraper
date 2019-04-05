import os, json, pickle


with open('../pickles/book_titles_s2f.pickle', 'rb') as handle:
    proper_names = pickle.load(handle)


retval = dict()
with open("Literature_tropes_dataset.json", 'r') as f:
    entries = json.load(f)

    for k in entries:
        retval[proper_names[k]] = entries[k]


with open("Literature_tropes_dataset.json", 'w') as f:
    json.dump(retval, f)