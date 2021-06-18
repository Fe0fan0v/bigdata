# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = 'https://ru.investing.com/crypto/bitcoin/btc-usd'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
course = soup.find('span', class_='arial_26 inlineblock pid-945629-last')

for i, v in enumerate(course):
    print(v)
