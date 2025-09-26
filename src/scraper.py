import requests 
from bs4 import BeautifulSoup
from ebooklib import epub

url_info = "https://centralnovel.com/series/shadow-slave-20230928/"
url_cap = "https://centralnovel.com/shadow-slave-capitulo-1/"


def getText(soup):
    div_conteudo = soup.find("div", class_="epcontent entry-content")
    paragrafos = div_conteudo.find_all("p")
    texto = "\n".join((p.get_text(strip=True)) for p in paragrafos)
    return texto

def getTitle(soup):
    title = soup.find("h1", class_="entry-title")
    return title.text.strip()

def getAuthor(soup):
    div_author = soup.find("div", class_="spe")
    spans = div_author.find_all("span")
    author = spans[2]
    author_name = author.find("a").text
    return author_name


def getNovelInfo(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    info = {}
    info["title"] = getTitle(soup)
    info["author"] = getAuthor(soup)

    return info

def buildEpub(content):
    novel_content = getContent(url_info)
    print(content["text"])
    #book = epub.EpubBook()
    #book.set_title("Livro teste")
    #book.set_language('pt')
    #book.add_author("Alfredo Lucas")
    #c1 = epub.EpubHtml(title="Livro Teste", file_name="cap1.xhtml")
    #html_content = "<h1>Capitulo 1</h1>"
    #for par in content.split('\n'):
    #    html_content += f"<p>{par}</p>"
    #c1.content = html_content
    #book.add_item(c1)
    #
#
    #book.toc = (epub.Link('cap1.xhtml', 'Capítulo 1', 'cap1'),)
    #book.spine = ['nav', c1]
#
    #book.add_item(epub.EpubNcx())
    #book.add_item(epub.EpubNav())
#
    #epub.write_epub('teste.epub', book, {})

buildEpub(getContent(url))







