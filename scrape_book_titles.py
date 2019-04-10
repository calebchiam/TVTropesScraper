import requests
import os
from bs4 import BeautifulSoup
from typing import List, Dict, Tuple, Set
import json
import time
from tqdm import tqdm
import random
from page_scrape import fetch_page_soup


CONFIG = "Awesome"
BASE_URL = "https://tvtropes.org/pmwiki/pmwiki.php/{}/".format(CONFIG)
BASE_DIR = os.path.join(os.getcwd(), "TITLES_", CONFIG)

suffixes = ['LiteratureNoToD', 'LiteratureEToI', 'LiteratureJToM', 'LiteratureNToQ', 'LiteratureRToU', 'LiteratureVToZ']

# ZERO_TITLES_FILE = os.path.join(BASE_DIR, "zerotitles.json")
# TITLES_FILE = os.path.join(BASE_DIR, "titles.json")
# PROGRESS_FILE = os.path.join(BASE_DIR, "progress.txt")

def extract_titles_from_soup(soup) -> Dict[str, str]:
    """
    Extract tropes from soup object. Tropes are typically located in
    <ul> -> <li> -> <a class="twikilink" href=...>[TROPE NAME]
    :param soup: bs4 soup object
    :return: Set of strings of tropes
    """
    retval = dict()
    main_article = soup.select("div#main-article")
    all_ul = set(main_article[0].find_all('ul'))

    for ul in main_article[0].find_all('ul'):
        # print(ul.prettify())
        for li in ul.find_all('li'):
            first_a = li.find('a')
            if first_a is None: continue
            if not first_a.has_attr('class'): continue
            if first_a['class'][0] == "twikilink" and CONFIG in first_a['href']:
                suf = first_a['href'].split("/")[-1]
                if suf.startswith("Literature"): continue # don't want list

                title_tropey = suf
                title_proper = first_a.findAll(text=True)[0]

                trope_title = first_a['href'].split("/")[-1]
                retval[title_proper] = title_tropey

    return retval


if __name__ == "__main__":
    titles_ = dict()
    for suffix in suffixes:

        soup = fetch_page_soup(BASE_URL + suffix)
        titles = extract_titles_from_soup(soup)
        assert(len(titles) > 0)

        titles_.update(titles)

    with open("{}_titles.json".format(CONFIG), 'w') as f:
        json.dump(titles_, f)


