import requests
from bs4 import BeautifulSoup
import random
from PIL import Image
import io

url = 'https://www.reddit.com/r/dogpictures/'
headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0"}
page  = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

links = soup.findAll("img", {"class":"_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax"})


choice = random.choice(links)

src = choice['src']

img = requests.get(src)

imgbyte = io.BytesIO(img.content)


img = Image.open(imgbyte)

img.show(title='Start your day the right way!')


