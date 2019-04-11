import json


with open("Awesome_movie_titles.json", 'r') as f:
    awesome_titles = json.load(f)

with open("Characters_titles.json", 'r') as f:
    character_titles = json.load(f)

print(len(awesome_titles))
print(len(character_titles))

titles_ = dict()
titles_.update(awesome_titles)
titles_.update(character_titles)
print(len(titles_))

with open("scraped_titles.json", 'w') as f:
    json.dump(titles_, f)