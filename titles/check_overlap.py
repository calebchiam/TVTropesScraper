import json

with open("scraped_titles.json", 'r') as f:
    scraped = json.load(f)

success = set()
with open("successful_books.txt", 'r') as f:
    for line in f:
        success.add(line.strip("\n"))

no_overlap = set(scraped.keys()) - success


with open("scraped_no_overlap.txt", 'w') as f:
    for x in no_overlap:
        f.write(x)
        f.write("\n")