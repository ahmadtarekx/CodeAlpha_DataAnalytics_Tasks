from bs4 import BeautifulSoup
import requests
import pandas as pd

#define the url of the webpage
url = 'https://finance.yahoo.com/markets/stocks/most-active/'

page=requests.get(url)

#Get The response Code from the server to determine  if we can scrape the data
print(page)
