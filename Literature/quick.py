import json
#
# with open("zerotropes_Literature.json", 'a+') as f1:
#     with open("fewtropes_Literature.json", "r") as f:
#         for line in f:
#             a = json.loads(line)
#             # print(json.loads(line))
#             # print(a)
#             ls = next(iter(a.values()))
#             if len(ls) == 0:
#                 f1.write(next(iter(a.keys())))
#                 f1.write("\n")


with open("Literature_tropes_dataset3.json", 'r') as f:
    entries = json.load(f)

with open("../titles/successful_books2.txt", 'w') as f:
    for k in entries:
        f.write(k)
        f.write("\n")