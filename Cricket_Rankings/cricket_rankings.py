from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable


def Menu():
	print('\n1. Men \n2. Women\n')
	gen=Gender()
	print('\n1. Team Rankings \n2. Player Ranking\n')
	tp=TeamOrPlayer()
	
	mode=''
	val=''
	
	if gen=='mens':
		print('\n1. Test\n2. ODI\n3. T20\n')
		mode=Mode()

	if tp=='player-rankings':
		if mode=='':
			print('\n1. ODI\n2. T20\n')
			mode=Mode2()
		print('\n1. Batting\n2. Bowling\n3. All-Rounder\n')
		val=Value()
	
	return gen,tp,mode,val


def Gender():
	gender=input('Enter your choice:')
	code={'1':'mens','2':'womens'}

	if gender in code:
		return code[gender]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return Gender();


def TeamOrPlayer():
	choice=input('Enter your choice:')
	tp={'1':'team-rankings','2':'player-rankings'}
	
	if choice in tp:
		return tp[choice]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return TeamOrPlayer();

	
def Mode():
	choice=input('Enter your choice:')
	word={'1':'/test','2':'/odi','3':'/t20i'}
	
	if choice in word:
		return word[choice]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return Choice();


def Mode2():
	choice=input('Enter your choice:')
	word={'1':'/odi','2':'/t20i'}
	
	if choice in word:
		return word[choice]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return Choice();


def Value():
	choice=input('Enter your choice:')
	val={'1':'batting','2':'bowling','3':'all-rounder'}
	
	if choice in val:
		return val[choice]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return Value()


def URL():
	gen,tp,mode,val=Menu()
	url='https://www.icc-cricket.com/rankings/'+gen+'/'+tp+mode+'/'+val
	header=gen.upper() +' ' +mode[1:].upper() + ' ' + val.upper()
	print('\n{:<15}  {:<30}\n{:<15}  {:<30}'.format('',tp.upper(),'',header))
	return url,tp


def SOUP(url,tp):
	try:
		res=requests.get(url)
		soup=BeautifulSoup(res.text,'lxml')
		a= soup.find_all('tr',{'class':'table-body'})
		data={}
			
		for i in a :
			team=[]
			name=''
			rating=''

			try:
				rank=int(i.contents[1].text)
			except:
				pass
			
			try:	
				name=i.contents[3].text.replace('\n','')
				name=" ".join(name.split())
				if rank==1 and tp=='player-rankings':
					name=name[0:-3]
			except:
				pass

			try:
				rating=i.contents[9].text
			except:
				if rank==1 :
					rating=i.contents[5].text
				else:
					rating=i.contents[7].text
			
			team.extend([name,rating])
			data[rank]=team
		
		return data

	except:
		return SOUP(url,tp)


def Print(data):
	print('\nRANKING \t TEAM\t\t\t\tRATING')
	for i in sorted(data):
		print('{:<10}       '.format(i),end='')
		for j in range(len(data[i])):
			print('{:<26}'.format(data[i][j]),end='     ')
		print()


def main():
	
	url,tp=URL()
	data=SOUP(url,tp)
	Print(data)	


if __name__=='__main__':
	main()
