import pickle
import json

with open('real_movie_titles.p', 'rb') as handle:
    b = pickle.load(handle)


inverted_dict = dict()

for k in b:
    inverted_dict[b[k]['simple1']] = k
    inverted_dict[b[k]['simple2']] = k

with open('Film_tropes_dataset.json', 'r') as f:
    dataset = json.load(f)

dataset2 = dict()

for k in dataset:
    if k in inverted_dict:
        dataset2[inverted_dict[k]] = dataset[k]

with open("Film_tropes_dataset2.json", 'w') as f:
    json.dump(dataset2, f)
