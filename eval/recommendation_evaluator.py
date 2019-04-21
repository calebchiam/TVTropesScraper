from typing import List, Dict

good_movie_to_book_results = {
    "Harry Potter and the Chamber of Secrets": ["Harry Potter and the Sorcerer's Stone",
                                                "Harry Potter and the Chamber of Secrets"],
    "The Truman Show": ["Time Out of Joint"],
    "The Hunger Games": ["The Hunger Games", "Battle Royale"],
    "Blade Runner": ["Idoru", "Neuromancer"],
    "Groundhog Day": ["Before I Fall"],
    "I, Robot": ["I, Robot", "Foundation"],
    "Murder on the Orient Express": ["Murder On The Orient Express", "The Mousetrap"],
    "Train to Busan": ["World War Z", "The Enemy"],
    "Persepolis": ["The Kite Runner", "Fahrenheit 451"],
    "Terminator 2: Judgment Day": ["Robopocalypse"]
}

good_book_to_movie_results = {
    "The Hunger Games": ["The Hunger Games", "The Hunger Games: Catching Fire", "Battle Royale"],
    "Heart Of Darkness": ["The Man Who Would Be King", "Apocalypse Now"],
    "Fight Club": ["Fight Club", "Raging Bull"],
    "Foundation": ["I, Robot"],
    "I, Robot": ["I, Robot"],
    "I Know Why The Caged Bird Sings": ["Moonlight"],
    "I Know What You Did Last Summer": ["I Know What You Did Last Summer",
                                        "Scream", "Scream 2", "Scream 3", "Scream 4"],
    "Murder On The Orient Express": ["Murder on the Orient Express", "Gosford Park", "The Hateful Eight"],
    "And Then There Were None": ["Identity", "And Then There Were None"],
    "It": ["It", "Cult of Chucky"]
}

def eval_results(results: Dict[str, List[str]],
                 direction: str="movie-to-book", # or "book-to-movie"
                 verbose: bool=True):
    """

    :param results: the outputs from a ranking algorithm, e.g.
    {"2012": ["Book of Job", "Mel Gibson", "The Tutelaries"],
     "It": ["Carrie", "The Killing"]
    }
    :param direction: "movie-to-book" or "book-to-movie"
    :param verbose: False to just get the overall score, True to get a description of which
             outputs were successful and which were not
    :return: None
    """

    score = 0

    if direction == "movie-to-book":
        good_results = good_movie_to_book_results
        print("Evaluating results for movie input to book recommendations!")
    else:
        good_results = good_book_to_movie_results
        print("Evaluating results for book input to movie recommendations!")

    max_score = sum([1 for books in good_results.values() for book in books])
    for input, outputs in good_results.items():
        if input not in results:
            print("WARNING: {} is not present in inputted results".format(input))
            continue
        for output in outputs:
            if output not in results[input]:
                if verbose: print("FAIL: {} -> {}".format(input, output))
            else:
                score += 1
                if verbose: print("SUCCESS: {} -> {}".format(input, output))

    print("OVERALL SCORE: {:.2f}%".format(100*score / max_score))


if __name__ == "__main__":
    # AS AN EXAMPLE
    results = {
        "Harry Potter and the Chamber of Secrets": ["Harry Potter and the Sorcerer's Stone",
                                                    "Highfalutin"],
        "The Truman Show": ["Time Out of Joint"],
        "The Hunger Games": ["The Hunger Games", "Battle Royale"],
        "Blade Runner": ["Idoru", "Androds Dreaming"],
        "Groundhog Day": ["Before I Fall"],
        "I, Robot": ["I, Robot", "Foundation"],
        "Murder on the Orient Express": ["Murder On The Orient Express", "The Mousetrap"],
        "Train to Busan": ["World War Z", "The Enemy"],
        "Persepolis": ["The Kite Runner", "Fahrenheit 451"],
        "Terminator 2: Judgment Day": ["Robopocalypse"]
    }

    eval_results(results, direction="movie-to-book", verbose=True)
    
