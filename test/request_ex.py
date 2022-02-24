
import requests as rq

from bs4 import BeautifulSoup

home_url = "https://mdn.github.io/beginner-html-site/ " 
r = rq.get(home_url)
soup = BeautifulSoup(r.text, "lxml")

print(r)
print(soup.prettify())
print(soup.body)