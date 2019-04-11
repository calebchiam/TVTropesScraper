import json
from collections import Counter
with open("../Literature/Literature_tropes_dataset2.json", 'r') as f:
    dataset = json.load(f)

print(len(dataset))

lowered = [k.lower() for k in dataset]
c = Counter(lowered)

for k in c:
    if c[k] > 1:
        titles = []
        for title in dataset:
            if title.lower() == k:
                titles.append(title)
        to_delete = sorted(titles)[0]
        del dataset[to_delete]

with open("../Literature/Literature_tropes_dataset3.json", 'w') as f:
    json.dump(dataset, f)