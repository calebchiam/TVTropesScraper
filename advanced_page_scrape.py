import requests
import os
from bs4 import BeautifulSoup
from typing import List, Dict, Tuple, Set
import json
import time
from tqdm import tqdm
import random
import itertools


CONFIG = "FilmTHREE" # Literature or Film
RESET = True

BASE_URL = "https://tvtropes.org/pmwiki/pmwiki.php/{}/".format(CONFIG)
BASE_DIR = os.path.join(os.getcwd(), CONFIG)

ZERO_TROPES_FILE = os.path.join(BASE_DIR, "zerotropes_{}.json".format(CONFIG))
FEW_TROPES_FILE = os.path.join(BASE_DIR, "fewtropes_{}.json".format(CONFIG))
TROPES_FILE = os.path.join(BASE_DIR, "tropes_{}.json".format(CONFIG))
PROGRESS_FILE = os.path.join(BASE_DIR, "{}_progress.txt".format(CONFIG))


def simplify_name(title: str) -> str:
    """
    :return: title string lowercased and special characters removed
    """
    return ''.join(c for c in title.lower() if c.isalnum())


def fetch_page_soup(url: str):
    res = requests.get(url)
    res.raise_for_status()
    return BeautifulSoup(res.text, 'html.parser')


def extract_tropes_from_soup(soup) -> Set[str]:
    """
    Extract tropes from soup object. Tropes are typically located in
    <ul> -> <li> -> <a class="twikilink" href=...>[TROPE NAME]
    :param soup: bs4 soup object
    :return: Set of strings of tropes
    """
    retval = set()
    main_article = soup.select("div#main-article")
    all_ul = set(main_article[0].find_all('ul'))

    for ul in main_article[0].find_all('ul'):
        # print(ul.prettify())
        all_li = set(ul.find_all('li'))
        children2 = set(ul.children)
        for li in all_li.intersection(children2): # only immediate children
            first_a = li.find('a')
            if first_a is None: continue
            if not first_a.has_attr('class'): continue
            if first_a['class'][0] == "twikilink" and "Main" in first_a['href']:
                trope_title = first_a['href'].split("/")[-1]
                retval.add(trope_title)
    return retval

def clear_progress():
    for f in [ZERO_TROPES_FILE, FEW_TROPES_FILE, TROPES_FILE, PROGRESS_FILE]:
        if os.path.exists(f):
            os.remove(f)

def attempt_scrape(domain: str, title: str) -> bool:
    BASE_URL = "https://tvtropes.org/pmwiki/pmwiki.php/{}/".format(domain)

    try:
        s = fetch_page_soup(os.path.join(BASE_URL, title))
        tropes = list(extract_tropes_from_soup(s))

        obj = {title: tropes}
        if len(tropes) > 0:
            with open(TROPES_FILE, 'a+') as f:
                json.dump(obj, f)
                f.write("\n")
            return True
        else:
            return False


    except requests.exceptions.HTTPError:
        return False

if __name__ == "__main__":
    if RESET:
        clear_progress()

    with open("cleaned_movie_titles.json", 'r') as f:
        movies = json.load(f)

    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

# 4, 5, 2, 4
#     tups = [("AvengersInfinityWar", ["TropesAToD", "TropesEToM", "TropesNToR", "TropesSToZ"]),
#             ("GoneWithTheWind", ["GoneWithTheWindTropesNoToD", "GoneWithTheWindTropesEToH",
#                                   "GoneWithTheWindTropesIToL", "GoneWithTheWindTropesMToR", "GoneWithTheWindTropesSToZ"]),
#             ("Megamind", ["TropesAToL", "TropesMToZ"]),
#             ("TheAvengers", ["TropesAToD", "TropesEToL", "TropesMToP", "TropesQToZ"])
#     ]

    for domain, pages in tups:
        for p in pages:
            attempt_scrape(domain, p)
    # with open("FilmTWO/zerotropes_FilmTWO.json", 'r') as f:
    #     for line in tqdm(f):
    #         # entry = json.loads(line)
    #         # t = entry["trope"]
    #         t = line.strip("\n")
    #         print(t)
    #
    #         if t in ["Lagaan", "ThreeIdiots"]:
    #             attempt_scrape("Bollywood", t)
    #
    #         dt = [("Film", t),
    #               ("WesternAnimation", t), ("Anime", t),
    #               ("Disney", t), ("Animation", t)]
    #
    #         success = False
    #         for domain, title in dt:
    #             if attempt_scrape(domain, title) is True:
    #                 success = True
    #                 break
    #
    #         if not success:
    #             with open(ZERO_TROPES_FILE, 'a+') as f:
    #                 f.write(t)
    #                 f.write("\n")

    # for t in tqdm(movies.keys()):
    #     entry = movies[t]
    #     t_year = "{}{}".format(t, entry["year"])
    #
    #     dt = [("Film", t), ("Film", t_year),
    #           ("WesternAnimation", t), ("Anime", t),
    #           ("Disney", t), ("Animation", t)]
    #
    #     success = False
    #     for domain, title in dt:
    #         if attempt_scrape(domain, title) is True:
    #             success = True
    #             break
    #
    #     if not success:
    #         with open(ZERO_TROPES_FILE, 'a+') as f:
    #             f.write(t)
    #             f.write("\n")