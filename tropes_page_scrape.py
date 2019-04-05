import requests
import os
from bs4 import BeautifulSoup
from typing import List, Dict, Tuple, Set
import json
import time
from tqdm import tqdm
import random
from page_scrape import load_titles, fetch_page_soup


CONFIG = "Main" # Literature or Film
RESET = True

BASE_URL = "https://tvtropes.org/pmwiki/pmwiki.php/{}/".format(CONFIG)
BASE_DIR = os.path.join(os.getcwd(), CONFIG)

ERROR_FILE = os.path.join(BASE_DIR, "error_file.txt")
OUTPUT_FILE = os.path.join(BASE_DIR, "tropes_descriptions.json")
PROGRESS_FILE = os.path.join(BASE_DIR, "tropes_progress.txt")

def extract_paras_from_trope_soup(soup):
    main_article = soup.select("div#main-article")
    all_p = main_article[0].find_all('p')

    retval = ""
    for p in all_p:
        para_text = ''.join(p.findAll(text=True))
        if len(para_text) < 10: continue
        retval += ''.join(p.findAll(text=True))

    return retval

    #
    #
    # for ul in main_article[0].find_all('ul'):
    #     # print(ul.prettify())
    #     all_li = set(ul.find_all('li'))
    #     children2 = set(ul.children)
    #     for li in all_li.intersection(children2): # only immediate children
    #         first_a = li.find('a')
    #         if first_a is None: continue
    #         if not first_a.has_attr('class'): continue
    #         if first_a['class'][0] == "twikilink" and "Main" in first_a['href']:
    #             trope_title = first_a['href'].split("/")[-1]
    #             retval.add(trope_title)
    # return retval

if __name__ == "__main__":
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    titles = load_titles("tropes_titles.txt")
    titles = ["PaidForFamily"]
    # titles = ['UnkemptBeauty']

    for t in tqdm(titles):
        t = t.strip("\n")
        try:
            s = fetch_page_soup(os.path.join(BASE_URL, t))
            text = extract_paras_from_trope_soup(s)

            if len(text) < 10: raise Exception("Invalid page")

            with open(OUTPUT_FILE, 'a+') as f:
                json.dump({t: text}, f)
                f.write("\n")

        except Exception as e:
            with open(os.path.join(BASE_DIR, "error_file.txt"), 'a+') as f:
                f.write("{}: {}".format(t, str(e)))
                f.write("\n")


    # for b in tqdm(titles):
    #     print(b)
    #     try:
    #         s = fetch_page_soup(os.path.join(BASE_URL, b)) #simplify_name(b)
    #         tropes = list(extract_tropes_from_soup(s))
    #
    #         obj = {b: tropes}
    #         if len(tropes) > 0:
    #             with open(TROPES_FILE, 'a+') as f:
    #                 json.dump(obj, f)
    #                 f.write("\n")
    #         else:
    #             with open(ZERO_TROPES_FILE, 'a+') as f:
    #                 f.write(b)
    #                 f.write("\n")
    #
    #     except requests.exceptions.HTTPError:
    #         with open(ZERO_TROPES_FILE, 'a+') as f:
    #             f.write(b)
    #             f.write("\n")
    #
    #     with open(PROGRESS_FILE, 'a+') as f:
    #         f.write(b)
    #         f.write("\n")
