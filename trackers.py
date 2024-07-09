import html5lib
import requests
from bs4 import BeautifulSoup

def trackAmazonINPrice(url):
  headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, lick Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'}
  response = requests.get(url, headers = headers)
  content = response.content
  soup = BeautifulSoup(content, features = 'html5lib')
  productPrice = str(soup.find('span', attrs="a-price-whole").text)
  productPrice = list(productPrice)
  productPrice.remove(',')
  productPrice = ''.join(productPrice)
  return float(productPrice)

def trackGameNationPrice(url):
  headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, lick Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'}
  response = requests.get(url, headers = headers)
  content = response.content
  soup = BeautifulSoup(content, features = 'html5lib')
  productPrice = str(soup.find('span', id="ProductPrice").text)
  return float(productPrice)

def trackGameLootPrice(url):
  headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, lick Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'}
  response = requests.get(url, headers = headers)
  content = response.content
  soup = BeautifulSoup(content, features = 'html5lib')
  productPrice = str(soup.find('span', attrs="woocommerce-Price-amount amount").text)
  productPrice = ''.join(char for char in productPrice if char.isdigit())
  return (float(productPrice))

# DRIVER CODE
# myurl = "https://www.amazon.in/Peter-Greats-African-Experiments-Prose/dp/1681375990/?_encoding=UTF8&pd_rd_w=8N2xE&content-id=amzn1.sym.f8b2fc0c-779f-43a6-b25a-069849dd23a6%3Aamzn1.symc.fc11ad14-99c1-406b-aa77-051d0ba1aade&pf_rd_p=f8b2fc0c-779f-43a6-b25a-069849dd23a6&pf_rd_r=0S2ME6X11DH65T3YK0V1&pd_rd_wg=89pdj&pd_rd_r=f8e0a608-bbf1-4dfd-a090-a0852cd9f00c&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d"
# url2 = "https://amzn.in/d/0jfCLZ3b"

# print(trackAmazonINPrice(myurl))
# print(trackAmazonINPrice(url2))

# myurl = "https://gamenation.in/Products/Games/Assassin's-Creed-Odyssey?Age=PreOwned&a=16&b=19"
# print(trackGameNationPrice(myurl))

# url = "https://gameloot.in/shop/life-is-strange-before-the-storm-ps4-pre-owned/"
# print(trackGameLootPrice(url)) 
