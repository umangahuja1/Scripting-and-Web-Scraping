''' Web Scraped from  https://hackevents.co site '''

import requests
from bs4  import BeautifulSoup

res = requests.get('https://hackevents.co/hackathons')
soup = BeautifulSoup(res.text, 'lxml')
hacks = soup.find_all('div',{'class':'hackathon '})

for i,f in enumerate(hacks,1):
	month = f.find('div',{'class':'date'}).find('div',{'class':'date-month'}).text.strip()
	date = f.find('div',{'class':'date'}).find('div',{'class':'date-day-number'}).text.strip()
	days = f.find('div',{'class':'date'}).find('div',{'class':'date-week-days'}).text.strip()
	final_date = "{} {}, {} ".format(date, month, days )
	
	name = f.find('div',{'class':'info'}).find('h2').text.strip()

	city = f.find('div',{'class':'info'}).find('p').find('span',{'class':'city'}).text.strip()
	country = f.find('div',{'class':'info'}).find('p').find('span',{'class':'country'}).text.strip()

	print("{:<5} {:<20} :  {:<100} :   {}, {}\n ".format(str(i)+')',final_date, name.title(), city, country))
