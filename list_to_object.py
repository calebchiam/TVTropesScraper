"""
Quick and dirty script for converting JSONList to JSONObject
"""
import json

retval = dict()
with open("Literature/tropes_Literature.json", 'r') as f:
    for line in f:
        entry = json.loads(line)
        for title, tropes in entry.items():
            retval[title] = tropes

with open("Literature/Literature_tropes_dataset.json", "w") as f:
    json.dump(retval, f)