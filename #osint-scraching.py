import requests
from bs4 import BeautifulSoup

# Adresse du site web 
url = 'https://www.rosaliaastorino.be'

# Faire une requête HTTP pour obtenir le contenu de la page
response = requests.get(url)
content = response.text

# Parser le contenu HTML avec BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Extraire des informations du site web
title = soup.title.text
links = [link['href'] for link in soup.find_all('a')]
meta_tags = [meta['name'] for meta in soup.find_all('meta', attrs={'name': True})]

# Afficher les informations extraites
print(f'Title: {title}')
print(f'Links: {links}')
print(f'Meta tags: {meta_tags}')
