from bs4 import BeautifulSoup
import requests
import pandas as pd

#define the url of the webpage
url = 'https://finance.yahoo.com/markets/stocks/most-active/'

page=requests.get(url)

print(page)
