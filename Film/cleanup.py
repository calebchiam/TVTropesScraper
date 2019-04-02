import os
import json
from page_scrape import simplify_name

def strip_bracket(title: str):
    return title.split(" (")[0]

def rearrange_title(title: str):
    if ", a" in title or ", an" in title:
        frags = title.split(", ")
        if len(frags) != 2: return title
        else: print(frags)
        return frags[1] + frags[0]
    else:
        return title

retval = dict()

with open("../movie_titles_with_years.txt", 'r') as f:
    for line in f:
        entry = json.loads(line)
        simplified = simplify_name(rearrange_title(strip_bracket(entry["title"])))
        retval[simplified] = entry

with open("../cleaned_movie_titles.json", 'w') as f:
    json.dump(retval, f)



