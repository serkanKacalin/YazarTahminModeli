import requests
from bs4 import BeautifulSoup
import re


def remove_html_tags(tags):
    clean = re.compile('<.*?>')
    tags = re.sub(clean, '', tags)
    return tags


URL = input()
textFileName = URL[39:len(URL)] + '.txt'
textFileName = textFileName.replace('/', '-')
# urldeki / işareti ile bir klasör içindeki bir dosya belirtildiğinden hata alıyorduk bunu replace ile düzelttim.


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                         "AppleWebKit/537.36 (KHTML, like Gecko)"
                         "Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46"}

sayfa = requests.get(URL, headers=headers)
icerik = BeautifulSoup(sayfa.content, 'html.parser')
etiketler = str(icerik.find_all('p', class_='paragraph inline-placeholder'))   # find methodu parametre olarak verdiğimiz html etiketini bize veriyor

cleanedText = remove_html_tags(etiketler)

file = open(textFileName, 'w')
file.write(cleanedText)
file.close()
