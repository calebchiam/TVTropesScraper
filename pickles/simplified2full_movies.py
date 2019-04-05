from page_scrape import simplify_name
import pickle
import json

# For creating a Dictionary of simplified names to full names, e.g.
# whosthere: Who's There?

simplified2orig = dict()

with open("cleaned_movie_titles_with_years.txt", 'r') as f:
    for line in f:
        entry = json.loads(line)
        simplified2orig[entry["simplified"]] = entry["title"]
        with_year = entry["simplified"] + str(entry["year"])
        simplified2orig[with_year] = entry["title"]

tgt_name = "movie"

with open('{}_s2f.pickle'.format(tgt_name), 'wb') as handle:
    pickle.dump(simplified2orig, handle, protocol=pickle.HIGHEST_PROTOCOL)

# How to load the dictionary pickle

# with open('{}_s2f.pickle'.format(tgt_name), 'rb') as handle:
#     b = pickle.load(handle)

# print(b)

# trope2simplified = dict()
#
# with open("Film/fixednames/combined_fixednames.json", 'r') as f:
#     for line in f:
#         entry = json.loads(line)
#         trope2simplified[entry["trope"]] = entry["name"]
#
# print(trope2simplified)
# succeeded = set()
#
# with open("FilmTWO/tropes_FilmTWO.json", 'r') as f:
#     for line in f:
#         entry = json.loads(line)
#         title = next(iter(entry.keys()))
#         succeeded.add(trope2simplified[title])
#
# with open("Film/tropes_Film.json", 'r') as f:
#     for line in f:
#         entry = json.loads(line)
#         title = next(iter(entry.keys()))
#         succeeded.add(simplified2orig[title])
#
#
# with open("successful_movies.txt", 'w') as f:
#     for title in succeeded:
#         f.write(title)
#         f.write("\n")
#
