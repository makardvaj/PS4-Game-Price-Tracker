import html5lib
import requests
from bs4 import BeautifulSoup

def trackAmazonINPrice(url):
  headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, lick Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'}
  response = requests.get(url, headers = headers)
  content = response.content
  soup = BeautifulSoup(content, features = 'html5lib')
  productPrice = soup.find('span', attrs="a-price-whole").text
  return float(productPrice)
