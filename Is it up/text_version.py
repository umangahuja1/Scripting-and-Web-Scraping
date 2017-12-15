''' Check if a site is up or not '''

from bs4 import BeautifulSoup
import requests

url = input('Enter the name of site to check (format google.com): ')
res = requests.get('https://isitup.org/' + url)
soup = BeautifulSoup(res.text, 'lxml')

container = soup.find('div', {'id': 'container'})
status = container.find('p')
print(status.text)
