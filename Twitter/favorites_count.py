from bs4 import BeautifulSoup
import requests,sys

#you can also get the twitter handle from user
handle = input('Enter twitter handle to check favorite/liked post of a user : ') 
res = requests.get('https://twitter.com/'+handle)
soup = BeautifulSoup(res.text,'lxml')

try:
    follow_box = soup.find('li',{'class':'ProfileNav-item ProfileNav-item--favorites'})
    favorite = follow_box.find('a').find('span',{'class':'ProfileNav-value'})
    print("Number of post {}  liked are {}: ".format(handle,favorite.get('data-count')))

except:
    print('Cannot find the handle right now')
    sys.exit()
