from bs4 import BeautifulSoup
import requests,sys

handle = input('Enter twitter handle to check following of a user : ') 
res = requests.get('https://twitter.com/'+handle)
soup = BeautifulSoup(res.text,'lxml')

try:
    follow_box = soup.find('li',{'class':'ProfileNav-item ProfileNav-item--followers'})
    followers = follow_box.find('a').find('span',{'class':'ProfileNav-value'})
    print("Number of people following {} are {}: ".format(handle,followers.get('data-count')))

except:
    print('Cannot find the handle right now')
    sys.exit()
