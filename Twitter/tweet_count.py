from bs4 import BeautifulSoup
import requests

handle = input('Enter twitter handle : ') 
res = requests.get('https://twitter.com/'+handle)
soup = BeautifulSoup(res.text,'lxml')

try:
    tweet_box = soup.find('li',{'class':'ProfileNav-item ProfileNav-item--tweets is-active'})
    tweets= tweet_box.find('a').find('span',{'class':'ProfileNav-value'})
    print("Number of tweets of {} are {}: ".format(handle,tweets.get('data-count')))

except:
    print('Cannot find the handle right now')
