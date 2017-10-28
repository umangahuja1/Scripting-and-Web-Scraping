from bs4 import BeautifulSoup
import requests

handle = input('Enter twitter handle to check favorite/liked post of a user : ') 
res = requests.get('https://twitter.com/'+handle)
soup = BeautifulSoup(res.text,'lxml')

try:
    favorite_box = soup.find('li',{'class':'ProfileNav-item ProfileNav-item--favorites'})
    favorite = favorite_box.find('a').find('span',{'class':'ProfileNav-value'})
    print("Number of post {}  liked are {}: ".format(handle,favorite.get('data-count')))

except:
    print('Cannot find the handle right now')
