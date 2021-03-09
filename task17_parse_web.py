#task17 New York Times articles
from bs4 import BeautifulSoup
import requests


url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)
news = soup.findAll("div", {"class":"css-debyuq e1voiwgp1"})
for result in news:
    print(result.text)


print("number of results: \n" + str(len(news)))
