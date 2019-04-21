import requests
import os
from bs4 import BeautifulSoup
from typing import List, Dict, Tuple, Set
import json
import time
from tqdm import tqdm
import random


CONFIG = "FilmFIVE" # Literature or Film
RESET = False

BASE_URL = "https://tvtropes.org/pmwiki/pmwiki.php/Literature/"
BASE_DIR = os.path.join(os.getcwd(), CONFIG)

ZERO_TROPES_FILE = os.path.join(BASE_DIR, "zerotropes_{}.json".format(CONFIG))
TROPES_FILE = os.path.join(BASE_DIR, "tropes_{}.json".format(CONFIG))
PROGRESS_FILE = os.path.join(BASE_DIR, "{}_progress.txt".format(CONFIG))


def simplify_name(title: str) -> str:
    """
    :return: title string lowercased and special characters removed
    """
    return ''.join(c for c in title.lower() if c.isalnum())

def load_titles(filename: str) -> List[str]:
    """

    :param filename: Filename containing line-separated movie/book titles
    :return: List of titles
    """
    with open(filename, 'r') as f:
        return [title for title in f.readlines()]



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
    for f in [ZERO_TROPES_FILE, TROPES_FILE, PROGRESS_FILE]:
        if os.path.exists(f):
            os.remove(f)



if __name__ == "__main__":
    if RESET:
        clear_progress()
    #
    # with open("titles/Awesome_movie_titles2.json", 'r') as f:
    #     title_dict = json.load(f)
    #
    # titles = []
    # with open("titles/scraped_movies_no_overlap.txt", 'r') as f:
    #     for line in f:
    #         titles.append(line.strip("\n"))

    titles = ["Paprika"]
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    for b in tqdm(titles):
        print(b)
        try:
            s = fetch_page_soup(os.path.join(BASE_URL, simplify_name(b))) #simplify_name(b)
            tropes = list(extract_tropes_from_soup(s))

            obj = {b: tropes}
            if len(tropes) > 0:
                with open(TROPES_FILE, 'a+') as f:
                    json.dump(obj, f)
                    f.write("\n")
            else:
                with open(ZERO_TROPES_FILE, 'a+') as f:
                    f.write(b)
                    f.write("\n")

        except requests.exceptions.HTTPError:
            with open(ZERO_TROPES_FILE, 'a+') as f:
                f.write(b)
                f.write("\n")

        with open(PROGRESS_FILE, 'a+') as f:
            f.write(b)
            f.write("\n")