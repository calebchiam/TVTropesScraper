import json

with open("zerotropes_Literature.json", 'a+') as f1:
    with open("fewtropes_Literature.json", "r") as f:
        for line in f:
            a = json.loads(line)
            # print(json.loads(line))
            # print(a)
            ls = next(iter(a.values()))
            if len(ls) == 0:
                f1.write(next(iter(a.keys())))
                f1.write("\n")