from bs4 import BeautifulSoup
from ntfy import notify
import requests

def get_data():
	url='http://indiatoday.intoday.in/section/120/1/top-stories.html'
	res=requests.get(url)
	
	while(res.status_code!=200):
		try:
			res=requests.get('url')
		except:
			pass

	soup=BeautifulSoup(res.text,'lxml')
	
	short=soup.find('ul',{'class':'topstr-list gap topmarging'}).find_all('a')
	head_lines=soup.find_all('div',{'class':'innerbox'})
	return short,head_lines

def top_news(short):
	for top in short:
		print(top.text,end='\n\n')

def main_news(head_lines):
	for news in head_lines:
		for head in news.find_all('a'):
			print(head.text)
		for cont in news.find_all('p'):
			print(cont.text,end='\n\n')

def top_not(title):
	for i in title:
		notify('',i.text)

def main_not(head_lines):
	for news in head_lines:
		for head in news.find_all('a'):
			title=head.text
		for cont in news.find_all('p'):
			msg=cont.text
		notify(msg,title)

def menu():
	print()
	print(' -----------------------')
	print(' |   Menu              |')
	print(' |1. Top News          |')
	print(' |2. Top News Notify   |')
	print(' |3. Main News         |')
	print(' |4. Main News Notify  |')
	print(' -----------------------')

def main():
	ch='y'
	while(ch=='y'):
		menu()
		choice=input('\nEnter your choice:')
		print()
		short,head_lines=get_data()
		out={'1':'Top News','2':'Top Notify','3':'Main News','4':'Main Notify'}
		
		if choice in out:
			print('\t\t\t\t{}\n'.format(out[choice]))
		
		if choice=='1':
			top_news(short)
		elif choice=='2':
			top_not(short)
		elif choice=='3':
			main_news(head_lines)
		elif choice=='4':
			main_not(head_lines)
		else:
			print('Wrong Input')

		ch=input('Do you want to continue (y/n) :')
		print()

if __name__=='__main__':
	main()
