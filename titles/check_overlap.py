import json
#
# with open("scraped_titles.json", 'r') as f:
#     scraped = json.load(f)
#
# success = set()
# with open("successful_books.txt", 'r') as f:
#     for line in f:
#         success.add(line.strip("\n"))
#
# no_overlap = set(scraped.keys()) - success
#
#
# with open("scraped_no_overlap.txt", 'w') as f:
#     for x in no_overlap:
#         f.write(x)
#         f.write("\n")

with open("Awesome_movie_titles.json", 'r') as f:
    scraped = json.load(f)



with open("../Film/Film_tropes_dataset2.json", 'r') as f:
    dataset = json.load(f)

print(len(dataset.keys()))
print(len(scraped))

scraped2 = dict()
for k in scraped:
    frag = k.split(" (")[0]
    if frag != k:
        scraped2[frag] = scraped[k]
    scraped2[k] = scraped[k]

with open("Awesome_movie_titles2.json", 'w') as f:
    json.dump(scraped2, f)

scraped_keys_filtered = set([k.split(" (")[0] for k in scraped])

scraped_keys_filtered -= set(dataset.keys())
print(len(scraped_keys_filtered))
with open("scraped_movies_no_overlap.txt", 'w') as f:
    for x in scraped_keys_filtered:
        f.write(x)
        f.write("\n")
