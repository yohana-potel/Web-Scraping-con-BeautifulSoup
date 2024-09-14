from bs4 import BeautifulSoup
import requests

url = 'https://eviatienda.com/'
seObtiene = requests.get(url)
html_doc = seObtiene.text

soup = BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())
#titulo = soup.findAll('img')
#print(titulo)

#print(soup.prettify())

#print(soup.html)

#print(soup.title.name)



#print(soup.p['class'])

#print(soup.get_text())

#print(soup.p)

#for i in soup.find_all('img'):
#    print(i.get('alt'))

#print(soup.find("form"))

#print(soup.div['id'])

#print(soup.get_text())

link = soup.a
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

imgenes = soup.img
for parent in imgenes:
    if parent is None:
        print(parent)
    else:
        print(parent)