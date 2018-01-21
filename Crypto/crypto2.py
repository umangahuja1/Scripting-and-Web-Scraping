from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://coinmarketcap.com/all/views/all/'


def get_data():
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    table = soup.find('table', {'id': 'currencies-all'})

    all_rows = table.find_all('tr')

    data = [[item.text.strip(' ') for item in all_rows[0].find_all('th')]]

    for row in all_rows[1:101]:
        row_data = [item.text.replace('\n', '').replace('*', '').strip(' ') for item in row.find_all('td')]
        data.append(row_data)

    return data


def print_data(data):
    for row in data:
        print(*row)


def store_csv(data):
    df = pd.DataFrame(data[1:], columns=data[0], index=None)
    df.to_csv('crypto2.csv', index=None)


def store_excel(data):
    df = pd.DataFrame(data[1:], columns=data[0], index=None)
    df.to_excel('crypto2.xlsx', sheet_name='Prices', index=None)


def main():
    data = get_data()
    print_data(data)
    store_csv(data)
    store_excel(data)


if __name__ == '__main__':
    main()
