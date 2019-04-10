import json

with open("../Literature/Literature_tropes_dataset.json", 'r') as f:
    dataset = json.load(f)


print(len(dataset))

with open("tropes_LiteratureTWO.json", 'r') as f:
    i = 0
    for line in f:
        i+=1
        print(i)
        entry = json.loads(line.strip("\n"))
        dataset.update(entry)

with open("../Literature/Literature_tropes_dataset2.json", 'w') as f:
    json.dump(dataset, f)