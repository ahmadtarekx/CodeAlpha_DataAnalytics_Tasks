from bs4 import BeautifulSoup
import requests
import pandas as pd

#define the url of the webpage
url = 'https://books.toscrape.com/'

page=requests.get(url)

#Get The response Code from the server to determine  if we can scrape the data
print(page)
