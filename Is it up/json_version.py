""" Check if site is up """

import requests

domain = input('Enter the name of site to check (format google.com): ')
res = requests.get('https://isitup.org/' + domain + '.json')

data = res.json()
status_code = data['status_code']

if status_code == 1:
    print(domain, 'is up')

elif status_code == 2:
    print(domain, 'is down')

elif status_code == 3:
    print('Please enter a valid domain to check availability.')

else:
    print('Something unexpected happened!')
