import json

tuples = [("5050", "FiftyFifty"), # FILL IN YOUR TUPLES HERE
          ("2012", "TwoThousandTwelve")]

with open("fixednames.json", 'w') as f:
    for t in tuples:
        entry = {"name": t[0], "trope": t[1]}
        json.dump(entry, f)
        f.write("\n")
