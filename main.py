import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html): 
    soup = BS(html, 'html.parser')
    return soup

def get_mashina(soup):
    mashina = soup.find_all('div',class_= 'list-item list-label')
    # print(mashina)
    info = soup.find_all('div', class_='list-item list-label new-line')
    # print(info)
    for i in mashina:
        try:
            title = i.find('h2', class_='name').text.strip()
        except AttributeError:
            title = 'машина?'

        try:
            price = i.find('p', class_='price').text.strip()
        except AttributeError:
            price = '0'
    
    for x in info:
        # print(x)
        try:
            image = x.find('img',class_='lazy-image').get('data-src')
        except AttributeError:
            image = 'нет фото'

        try:
            image = i.find('div',class_= 'thumb-item-carousel brazzers-daddy>')
        except AttributeError:
            image = 'где фото ?'
        print(title)
        print(price)
        print(image)
        print(image)

        write_csv({
            'title': title,
            'price': price,
            'image': image
        })


def write_csv(data):
    with open('avto.csv', 'a') as file:
        names = ['title', 'price', 'image']
        write = csv.DictWriter(file, delimiter=',', fieldnames=names)
        write.writerow(data)


def main():
    url = 'https://www.mashina.kg/commercialsearch/all/?type=3&page=1'
    html = get_html(url)
    soup = get_soup(html)
    get_mashina(soup)
        
     
main()