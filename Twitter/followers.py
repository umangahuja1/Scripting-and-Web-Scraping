from bs4 import BeautifulSoup
import requests,sys

#you can also get the twitter handle from user
handle = ' ' 
res = requests.get('https://twitter.com/'+handle)
soup = BeautifulSoup(res.text,'lxml')

try:
	follow_box = soup.find('li',{'class':'ProfileNav-item ProfileNav-item--followers'})
	followers = follow_box.find('a').find('span',{'class':'ProfileNav-value'})
	print("Number of followers are : " + followers.get('data-count'))

except:
	print('Cannot find the handle right now')
	sys.exit()
