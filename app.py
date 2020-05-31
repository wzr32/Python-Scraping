import os
from main import scraping

while True:
    print('Python Scraping')
    
    search = input("Type an element to seach in => ")
    param = search.replace(' ', '+')
    page = 1

    os.system('clear')

    scraping(param, page)