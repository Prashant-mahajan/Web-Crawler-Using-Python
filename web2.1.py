import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://online.stepashka.com/filmy/#/page/' + str(page)
        source_code = requests.get(url)     #all website code
        plain_text = source_code.text       #links,images,texts from website page
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('div', {'class': 'video-title'}):
            # href = link.get('href')
            a_tag = link.a
            print(a_tag['href'])
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for  item_name in soup.findAll('div', {'class' : 'alternative-title'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = link.get('href')
        print(href)


trade_spider(1)

