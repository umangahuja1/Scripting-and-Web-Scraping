''' Charts and rating from IMDBB '''

from bs4 import BeautifulSoup
from terminaltables import DoubleTable
from colorclass import Color
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


def get_data(option):
	res = requests.get('http://m.imdb.com/chart/'+option)
	soup = BeautifulSoup(res.text, 'lxml')
	card_list = soup.find_all('span',{'class':'media-body media-vertical-align'})
	result = []
	for card in card_list:
		try:
			name = card.find('h4').text.replace("\n"," ").strip()
		except: 
			pass
		try:
			rating = card.find('p').text.strip()
		except:
			pass

		result.append((name,rating))

	return result


def make_table(result):
    table_data = [['S.No', 'Name', 'Rating']]

    for s_no,res in enumerate(result,1):
        row = []
        row.extend((Color('{autoyellow}' + str(s_no) + '.' + '{/autoyellow}'),
                        Color('{autogreen}' + res[0] + '{/autogreen}'),
                        Color('{autoyellow}' + res[1] + '{/autoyellow}')))
        table_data.append(row)

    table_instance = DoubleTable(table_data)
    table_instance.inner_row_border = True

    print(table_instance.table)
    print()
		
def main():
	option = select()
	data = get_data(option)
	make_table(data)

if __name__ == '__main__':
	main()
