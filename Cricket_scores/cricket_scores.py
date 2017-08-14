from pycricbuzz import Cricbuzz
from pprint import pprint
import json

c=Cricbuzz()

def match_id(desc):
	all_matches = c.matches()
	for match in all_matches:
		if match['mchdesc'].title() == desc:
			return match['id']
	else:
		return None


def all_matches():
	match_data = c.matches()
	matches = []
	for match in match_data:
		matches.append(match['mchdesc'])
	return matches


def live_score(desc):
	mid = match_id(desc)
	data = c.livescore(mid)
	score = {}
	score['matchinfo'] = "{}, {}".format(data['matchinfo']['mnum'],data['matchinfo']['mchdesc'])
	score['status'] = "{}, {}".format(data['matchinfo']['mchstate'].title(),data['matchinfo']['status'])
	score['bowling'] = data['bowling']
	score['batting'] = data['batting']

	text = ''
	text += score['matchinfo'] + '\n' + score['status'] + '\n\n'
	text += score['batting']['team'] + '\n'
	
	for scr in reversed(score['batting']['score']):
		text += "{} :- {}/{} in {} overs\n".format(scr['desc'],scr['runs'],scr['wickets'],scr['overs']) 
	for b in reversed(score['batting']['batsman']):
		text += "{} : {}({}) \n".format(b['name'].strip('*'),b['runs'],b['balls'])
	text += "\n" + score['bowling']['team'] + '\n'
	for scr in reversed(score['bowling']['score']):
		text += "{} :- {}/{} in {} overs\n".format(scr['desc'],scr['runs'],scr['wickets'],scr['overs']) 
	for b in reversed(score['bowling']['bowler']):
		text += "{} : {}/{} \n".format(b['name'].strip('*'),b['wickets'],b['runs'])
	
	return text


def commentary(desc):
	mid = match_id(desc)
	data = c.commentary(mid)
	comm ={}
	comm['matchinfo'] = "{}, {}".format(data['matchinfo']['mnum'],data['matchinfo']['mchdesc'])
	comm['status'] = "{}, {}".format(data['matchinfo']['mchstate'].title(),data['matchinfo']['status'])
	comm['commentary'] = data['commentary']
	text =''
	text += comm['matchinfo'] + '\n' + comm['status'] + '\n\n'
	for com in comm['commentary']:
		text += "{}\n\n".format(com)

	return text


def scorecard(desc):
	mid = match_id(desc)
	data = c.scorecard(mid)
	card = {}
	card['matchinfo'] = "{}, {}".format(data['matchinfo']['mnum'],data['matchinfo']['mchdesc'])
	card['status'] = "{}, {}".format(data['matchinfo']['mchstate'].title(),data['matchinfo']['status'])
	card['scorecard'] = data['scorecard']
	text = ''
	text += card['matchinfo'] + '\n' + card['status'] + '\n\n'
	text +='*'*35 +'\n\n'

	for scr in reversed(card['scorecard']):
		text += "{} {}\n{}/{} in {} overs\n\n".format(scr['batteam'],scr['inngdesc'],scr['runs'],scr['wickets'],scr['overs'])
		text += "Batting\n"
		text += "{:<17} {:<3} {:<3} {:<3} {}\n\n".format('Name','R','B','4','6')
		for b in scr['batcard']:
			text += "{:<17} {:<3} {:<3} {:<3} {}\n{}\n\n".format(b['name'], b['runs'], b['balls'], b['fours'], b['six'], b['dismissal'])
		text +="-"*35 +"\n\n"
		text += "Bowling\n"
		text += "{:<17} {:<5} {:<3} {:<3} {}\n\n".format('Name','O','M','R','W')
		for b in scr['bowlcard']:
			text += "{:<17} {:<5} {:<3} {:<3} {}\n\n".format(b['name'], b['overs'], b['maidens'], b['runs'], b['wickets'])
		text +='*'*35 +'\n\n'
	return text


def main():
	matches = all_matches()
	print("\nALL MATCHES\n")
	for i,m in enumerate(matches,1):
		print("{}. {}".format(str(i),m))
	choice = int(input('\nEnter choice (number): '))
	while choice <1 or choice > len(matches):
		print('\nWrong choice')
		choice = int(input('\nEnter choice again: '))

	desc = matches[choice-1].title()
	print('\n')
	print('1. Live Score')
	print('2. Full Score Card')
	print('3. Commentary')
	choice = int(input('\nEnter choice (number): '))
	while choice <1 or choice > 3:
		print('\nWrong choice')
		choice = int(input('\nEnter choice again: '))
	print('\n')
	if choice ==1:
		ref = 'y'
		while ref =='y':
			print(live_score(desc))
			ref = input('\n\nDo you want to refresh:(y/n) ')
			print('\n')

	elif choice ==2:
		ref = 'y'
		while ref =='y':
			print(scorecard(desc))
			ref = input('\n\nDo you want to refresh:(y/n) ')
			print('\n')

	else:
		ref = 'y'
		while ref =='y':
			print(commentary(desc))
			ref = input('\n\nDo you want to refresh:(y/n) ')
			print('\n')


if __name__ == '__main__':
 	main()
