from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib
import urllib
import random

a = input("Enter Your Letterboxd Username:")
url_pagination = f'https://letterboxd.com/{a}/watchlist'
r = requests.get(url_pagination)
soup = BeautifulSoup(r.content, "html.parser")
pagination = soup.find("div", {"class": "pagination"})
li_page = 0
if pagination:
    li_page = pagination.find_all("li")[-1].get_text()
else:
    li_page = 1

movie_titles = []    
for i in range(1,int(li_page)+1):
    URL = f'https://letterboxd.com/{a}/watchlist/page/{i}/'
    
    page = requests.get(URL)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    movie = soup2.find('ul', {'class': 'poster-list -p125 -grid -scaled128'})
    li_items = movie.find_all('li')
    for li in li_items:
        img = li.find('img', alt=True)
        titles = (img['alt'])
        movie_titles.append(titles)    
print(random.choice(movie_titles))
