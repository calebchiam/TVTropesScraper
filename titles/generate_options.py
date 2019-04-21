
with open("options_books.txt", 'w') as g:
    with open("successful_books2.txt", 'r') as f:
        for line in f:
            g.write("<option>{}</option>".format(line.strip("\n")))
            g.write("\n")

with open("options_movies.txt", 'w') as g:
    with open("successful_movies2.txt", 'r') as f:
        for line in f:
            g.write("<option>{}</option>".format(line.strip("\n")))
            g.write("\n")


