from bs4 import BeautifulSoup
from ntfy import notify
import requests


def get_data(query):
	res=requests.get('http://www.thesaurus.com/browse/'+query+'?s=t')
	soup=BeautifulSoup(res.text,'lxml')
	des=soup.find('div',{'class':'synonym-description'}).find('strong')
	syn=soup.find('div',{'class':'relevancy-list'}).find_all('span',{'class':'text'})
	return des,syn


def notification(des,synonym,query):
	notify(des.text+"\n"+", ".join(synonym[:3]),query.upper())


def file_out(word,des):
	fa=open('synonym.txt','a')
	for i in word:
		fa.write("WORD:     {} \n".format(i))
		fa.write("MEANING:  {}\n".format(des.text))
		fa.write("SYNONYMS: {}\n\n".format(word[i]))


def data(des,syn,query):
	word={}
	synonym=[]
	
	for i in syn[:10]:
		synonym.append(i.text)

	word[query]=", ".join(synonym)
	return synonym,word


def main():
	query=input('Enter word:')
	des,syn=get_data(query)
	synonym,word=data(des,syn,query)
	notification(des,synonym,query)
	file_out(word,des)
	

if __name__=='__main__':
	main()
