''' Webscraped from https://www.brainyquote.com '''

import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.brainyquote.com/quotes_of_the_day.html')
soup = BeautifulSoup(res.text, 'lxml')

quote = soup.find('img',{'class':'p-qotd'})
print(quote['alt'])
