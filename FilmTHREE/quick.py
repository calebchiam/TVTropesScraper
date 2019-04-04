import json
with open("tropes_FilmTHREE.json", 'r') as f:
    d = dict()
    for line in f:
        entry = json.loads(line)
        key = next(iter(entry.keys()))
        ls = next(iter(entry.values()))

        if key in d:
            d[key].extend(ls)
        else:
            d[key] = ls

    with open("zzz.json", 'w') as g:
        for k, v in d.items():
            json.dump({k: v}, g)
            g.write("\n")
