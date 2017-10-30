# Install PhantomJS to use this script

from selenium import webdriver
from bs4  import BeautifulSoup
from time import sleep
from terminaltables import DoubleTable
from colorclass import Color

print('--- Fetching hackathons--- \n')
driver = webdriver.PhantomJS()
driver.get('https://www.hackerearth.com/challenges/')
res = driver.page_source
soup = BeautifulSoup(res, 'lxml')
upcoming = soup.find('div',{'class':'upcoming challenge-list'})
all_hackathons = upcoming.find_all('div',{'class':'challenge-content'})

table_data = [['S.No', 'Name', 'Type', 'Timings']]

for s_no,hackathon in enumerate(all_hackathons,1):
    row = []
    challenge_type = hackathon.find('div',{'class':'challenge-type'}).text.replace("\n"," ").strip()
    challenge_name = hackathon.find('div',{'class':'challenge-name'}).text.replace("\n"," ").strip()
    date_time = hackathon.find('div',{'class':'challenge-list-meta challenge-card-wrapper'}).text.replace("\n"," ").strip()
    row.extend((Color('{autoyellow}' + str(s_no) + '.' + '{/autoyellow}'),
                    Color('{autocyan}' + challenge_name + '{/autogreen}'),
                    Color('{autogreen}' + challenge_type + '{/autoyellow}'),
                    Color('{autoyellow}' + date_time + '{/autoyellow}')))
    table_data.append(row)


table_instance = DoubleTable(table_data)
table_instance.inner_row_border = True

print(table_instance.table)
print()

    
