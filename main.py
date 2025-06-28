import requests
from bs4 import BeautifulSoup

#Insira a URL da página que deseja raspar
url = 'https://exame.com/webstories/inteligencia-artificial/ultimas-publicacoes/'

site = requests.get(url)
conteudo_site = BeautifulSoup(site.text, 'html.parser')
titulo_link = conteudo_site.find_all('a', class_='touch-area')

publicacoes= []

for i, a in enumerate(titulo_link, start=1):
    titulo = a.get_text(strip=True)
    link = f"https://exame.com{a.get('href').replace(' ', '')}"

    publicacoes.append(f"--> {i}º Publicação\n Título: {titulo} \n Link: {link}\n")

if publicacoes:
    with open('resultado_web_scraping.txt', 'w', encoding='utf-8') as txt:
        for publicacao in publicacoes:
            txt.write(publicacao + "\n")
    print('Web scraping realizado com sucesso! As publicações foram salvas em "resultado_web_scraping.txt".')
else:
    print('Não foi possível extrair publicações. Por favor, tente outra URL do site.')