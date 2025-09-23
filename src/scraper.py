import requests 
from bs4 import BeautifulSoup

url = "https://centralnovel.com/shadow-slave-capitulo-1/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
div_conteudo = soup.find("div", class_="epcontent entry-content")

paragrafos = div_conteudo.find_all("p")

texto = "\n".join((p.get_text(strip=True)) for p in paragrafos)

with open("texto.txt", "w") as f:
    f.write(texto)


