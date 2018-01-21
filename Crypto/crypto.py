from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.buyucoin.com/altcoin-rate-inr-india'


def get_data():
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    table = soup.find('table', {'id': 'inr_rate'})

    all_rows = table.find_all('tr')

    data = []

    for row in all_rows:
        row_data = [item.text.strip(' ') for item in row.find_all('td')]
        data.append(row_data)

    return data


def print_data(data):
    for row in data:
        print(" {:<25} {:<20} {:<20} {}".format(*row))


def store_csv(data):
    df = pd.DataFrame(data[1:], columns=data[0], index=None)
    df.to_csv('Crypto.csv', index=None)


def store_excel(data):
    df = pd.DataFrame(data[1:], columns=data[0], index=None)
    df.to_excel('Crypto.xlsx', sheet_name='Prices', index=None)


def main():
    data = get_data()
    print_data(data)
    store_csv(data)
    store_excel(data)


if __name__ == '__main__':
    main()
