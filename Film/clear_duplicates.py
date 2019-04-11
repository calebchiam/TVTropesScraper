import json
from collections import Counter
with open("Film_tropes_dataset3.json", 'r') as f:
    dataset = json.load(f)

print(len(dataset))

lowered = [k.lower() for k in dataset]
c = Counter(lowered)

for k in c:
    if c[k] > 1:
        print(k)