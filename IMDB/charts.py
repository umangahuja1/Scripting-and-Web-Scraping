''' Charts and rating from IMDBB '''

from bs4 import BeautifulSoup
import requests

def select():
	options = {
		1: ('Top movies' , 'top'),
		2: ('Most Popular Movies' , 'moviemeter'),
		3: ('Top TV Shows' , 'toptv'),
		4: ('Top English Movies' , 'top-english-movies'),
		5: ('Most Popular TV Shows' , 'tvmeter'),
	}

	for i,option in enumerate(options,1):
		print("{}) {}".format(i,options[option][0]))

	choice = int(input('\nEnter your choice: '))
	while(choice<1 or choice>len(options)):
		print('Wrong choice')
		choice = int(input('\nEnter your choice: '))

	return options[choice][1]


def display(option):
	res = requests.get('http://m.imdb.com/chart/'+option)
	soup = BeautifulSoup(res.text, 'lxml')
	card_list = soup.find_all('span',{'class':'media-body media-vertical-align'})

	for card in card_list:
		try:
			name = card.find('h4').text.replace("\n"," ").strip()
		except: 
			pass
		try:
			rating = card.find('p').text.strip()
		except:
			pass
		print('{:<100}\t{}\n'.format(name,rating))
		
def main():
	option = select()
	print()
	display(option)

if __name__ == '__main__':
	main()
