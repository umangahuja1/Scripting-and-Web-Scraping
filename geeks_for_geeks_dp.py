from bs4 import BeautifulSoup
from collections import OrderedDict
import pdfkit
import requests
import os

URL = 'http://www.geeksforgeeks.org/dynamic-programming/'
config = pdfkit.configuration()

data = OrderedDict()

match = {
    'Basic Problems': 'basicProblems',
    'Medium Problems': 'mediumProblems',
    'Hard Problems': 'hardProblems'
}


def make_soup(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup


def get_data(type, soup):

    content = soup.find('div', {'class': '' + match[type]})
    links = content.find_all('a')

    list_problems = OrderedDict()
    for i, link in enumerate(links[:7], 1):
        list_problems[link.text] = link['href']

    data[type] = list_problems


def pdf(type, data):
    current_dir = os.getcwd()
    folder = os.path.join(current_dir, type)
    if not os.path.exists(folder):
        os.mkdir(folder)

    for problem_name in data[type]:
        link = data[type][problem_name]
        pdf_name = problem_name + ".pdf"
        try:
            pdfkit.from_url(link, os.path.join(folder, pdf_name), configuration=config)
        except:
            pass


def main():
    soup = make_soup(URL)
    for type in match:
        get_data(type, soup)
        pdf(type, data)


if __name__ == '__main__':
    main()
