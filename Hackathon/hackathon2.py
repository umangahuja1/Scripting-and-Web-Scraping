""" Web scraped from http://www.hackathon.io/  """

import requests
from bs4  import BeautifulSoup

res = requests.get('http://www.hackathon.io/events')
soup = BeautifulSoup(res.text, 'lxml')
hacks = soup.find_all('div',{'class':'event-teaser'})

for i,f in enumerate(hacks,1):
	print("[{}] {}\n{}\n\n".format(i,f.find('h4').text,f.find('h5').text))
