# Recomendado recriar em um jupyternotebook
# buscando dados do site do professor Edson Melo de Souza na Uninove


import requests #realiza requisições web
from bs4 import BeautifulSoup #tratar dados html
import re #expressões regulares
import time

def lista(lista):
    for l in lista:
        print(l)

#recuperando os dados de um site via requests
url = 'https://www.edsonmelo.com.br'
site = requests.get(url)

#mostra o texto (conteúdo) completo da página acesada
#print(site.text)

# criar um objeto BS para manipular os dados
soup = BeautifulSoup(site.text, 'html.parser')
#print(soup.prettify())

# mostrando o título da página
soup.title

# mostrando o título sem as TAGs
soup.title.string

# encontrando os links na página (a)[href]
links = soup.find_all("a")

# vamos verificar link a link
result = []
for link in links:
    if re.search("http", link.get("href")):
        result.append(link.get("href"))
    else:
        if not re.search("#", link.get("href")):
            result.append(url + "/" + link.get("href"))
lista(result)

# procurando elementos dentro do html
soup.find_all("div")

# mostrando apenas os links para redes sociais
soup.find_all("div", class_="social-links")

#procurando imagens
soup.find_all("img", alt=True)

# para finalizar, vamos mostar apenas os textos das imagens

texto = soup.find_all("img", alt=True)

for r in texto:
    print(r.get("alt"))

time.sleep(5)