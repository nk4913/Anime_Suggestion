from bs4 import BeautifulSoup
import requests

data = requests.get("https://gogoanime.gr/genre/action")
converted_data = data.content
soup = BeautifulSoup(converted_data , 'lxml')

names = soup.find_all("p",{"class": "name"})
# images = soup.find_all("div",{"class": "img"})


for image in soup.find_all('div', attrs={'class':'img'}):
    for picture in image.find_all('img'):
        print(picture["src"])


