from bs4 import BeautifulSoup
import requests

username = input('Enter username to scrape : ')
count = int(input('Number of tweets to scrape : '))

res=requests.get('https://twitter.com/'+ username)
soup=BeautifulSoup(res.content,'lxml')

all_tweets = soup.find_all('div',{'class':'tweet'})

for tweet in all_tweets[:count]:
	
	context = tweet.find('div',{'class':'context'}).text.replace("\n"," ").strip()
	content = tweet.find('div',{'class':'content'})

	header = content.find('div',{'class':'stream-item-header'})
	user = header.find('a',{'class':'account-group js-account-group js-action-profile js-user-profile-link js-nav'}).text.replace("\n"," ").strip()
	time = header.find('a',{'class':'tweet-timestamp js-permalink js-nav js-tooltip'}).find('span').text.replace("\n"," ").strip()
	
	message = content.find('div',{'class':'js-tweet-text-container'}).text.replace("\n"," ").strip()
	
	footer = content.find('div',{'class':'stream-item-footer'})
	stat = footer.find('div',{'class':'ProfileTweet-actionCountList u-hiddenVisually'}).text.replace("\n"," ").strip()

	if context:
		print(context)
	print(user,time)
	print(message)
	print(stat)
	print()
