import requests
import time
import urllib.request
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Battle_of_the_Bulge"
url2 = "https://en.wikipedia.org/wiki/Pakistan_International_Airlines"
url3 = "https://en.wikipedia.org/wiki/Battle_of_France"


def get_citations_needed_count(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    result = soup.findAll("a", href="/wiki/Wikipedia:Citation_needed")
    return len(result)


def get_citations_needed_report(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    result = soup.findAll("a", href="/wiki/Wikipedia:Citation_needed")

    collection = []

    for link in result:
        paragraph = link.parent.parent.parent
        paragraph = paragraph.text.strip()
        collection.append(paragraph)

    for para in collection:
        print(para, sep="\n")
        print("\n")

    return collection
