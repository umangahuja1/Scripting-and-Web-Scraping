''' Scraped from http://quotes.toscrape.com '''

from bs4 import BeautifulSoup
import requests

URL = 'http://quotes.toscrape.com/page/'
i = 1

def get_soup(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text,'lxml')
	return soup

def quotes(soup):
	global i
	all_quotes = soup.find_all('div',{'class':'quote'})
	
	for quote_box in all_quotes:
		quote = quote_box.find('span',{'class':'text'}).text
		author = quote_box.find('small',{'class':'author'}).text
		print("{:<4} {}\n-{:>5}\n\n".format(str(i)+')',quote,author))
		i +=1

def main():
	pages = 10
	for p in range(1,pages+1):
		soup = get_soup(URL + str(p))
		quotes(soup)

if __name__ == '__main__':
	main()
