from bs4 import BeautifulSoup
import requests


#url = 'https://eviatienda.com/'
url = 'https://www.revesderecho.com/'

seObtiene = requests.get(url)
html_doc = seObtiene.text

soup = BeautifulSoup(html_doc,'html.parser')


#print(soup.prettify())

#print(soup.html)

#print(soup.title.name)



#print(soup.p['class'])

#print(soup.get_text())

#print(soup.p)

for i in soup.find_all('a'):
   print(i.get('href'))

#print(soup.find("form"))

#print(soup.div['id'])

#print(soup.get_text())

