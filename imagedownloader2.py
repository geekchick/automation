import requests, bs4, re


def findLinks(page):
    res = requests.get('https://imgur.com/search?q=sports')
    res.raise_for_status()
    imagesSoup = bs4.BeautifulSoup(res.text, "html.parser")

    startLink = imagesSoup.find("<img ")
    endLink = imagesSoup.find("/>")

    link = page[startLink:endLink]
