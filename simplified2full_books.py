from page_scrape import simplify_name
import pickle

# For creating a Dictionary of simplified names to full names, e.g.
# whosthere: Who's There?

TARGET = "book_titles.txt"

retval = dict()
with open(TARGET, 'r') as f:
    for line in f:
        retval[simplify_name(line)] = line.strip("\n")

print(len(retval))

tgt_name = TARGET.split(".")[0]

with open('{}_s2f.pickle'.format(tgt_name), 'wb') as handle:
    pickle.dump(retval, handle, protocol=pickle.HIGHEST_PROTOCOL)

# How to load the dictionary pickle

with open('{}_s2f.pickle'.format(tgt_name), 'rb') as handle:
    b = pickle.load(handle)

print(len(b))