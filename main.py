from bs4 import BeautifulSoup
import requests


def scraping(param = '', page = 1):

    url = f"https://www.newegg.com/p/pl?d={param}&Page={page}"

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')

    items = []

    item_container = soup.find_all('div', class_="item-container")
    for item in item_container[4:]:
        name = item.find('a', class_="item-title").text
        price = item.find('li', class_="price-current").strong.text
        items.append([name, price])

    for i in items:
        print(f'Product: {i[0]:150} \nPrice: {i[1]:10}\n')

    return page