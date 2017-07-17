from bs4 import BeautifulSoup
from terminaltables import DoubleTable
from terminaltables import DoubleTable
from colorclass import Color
import requests


def scrape():
	res=requests.get('http://synd.cricbuzz.com/j2me/1.0/sch_calender.xml')

	while(res.status_code!=200):
		res=requests.get('http://synd.cricbuzz.com/j2me/1.0/sch_calender.xml')

	soup=BeautifulSoup(res.content,'lxml')
	data=soup.find_all('mch')

	return data


def make_table(team1,team2=''):
	data=scrape()
	table_data=[['Match','Series','Date','Month','Time']]

	for i in data[:]:
		row=[]
		if team1.strip(' ') in i.get('desc') and team2.strip(' ') in i.get('desc') :
			row.extend((Color('{autoyellow}'+i.get('desc')+'{/autoyellow}'),Color('{autocyan}'+i.get('srs')[5:]+'{/autocyan}'),Color('{autored}'+i.get('ddt')+'{/autored}'),Color('{autogreen}'+i.get('mnth_yr')+'{/autogreen}'),Color('{autoyellow}'+i.get('tm')+'{/autoyellow}')))
			table_data.append(row)

	table_instance = DoubleTable(table_data)
	table_instance.inner_row_border = True

	print(table_instance.table)
	print()


def menu():
	print(' Search by team')
	print(' 1.One team: ')
	print(' 2.Two teams: ')
	choice=input('\n Enter your choice:')

	while(choice not in ['1','2']):
		print(Color('{autored}\n Wrong choice{/autored}'))
		choice=input('\n Enter your choice:')

	teams=['Ind','SL','Aus','Ban','RSA','ZIM','NZ','Eng','WI']
	print()
	print(teams)

	return int(choice)


def main():
		
	choice=menu()

	if(choice==1) :
		team=input("\n Enter team's name:")
		while(len(team)<=1):
			print(Color('{autored}\n Enter valid team name{/autored}'))
			team=input("\n Enter team's name:")

		make_table(team)

	else:
		team1=input("\n Enter name of team 1:")
		team2=input(" Enter name of team 2:")
		while(len(team1)<=1 or len(team2)<=1 or team1.strip(' ')==team2.strip(' ')):
			print(Color('{autored}\n Enter valid team names{/autored}'))
			team1=input("\n Enter name of team 1:")
			team2=input(" Enter name of team 2:")
		make_table(team1,team2)
    

if __name__ == '__main__':
    main()
