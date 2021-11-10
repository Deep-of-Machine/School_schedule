import requests
from bs4 import BeautifulSoup
import webbrowser

url = 'https://jeil.jje.hs.kr/'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#container > div.main_content > div.notice.widget > div:nth-child(6) > div > ul > li:nth-child(1) > span.text > a')
    print(title)
    print(title['href'])
else : 
    print(response.status_code)


url = 'https://jeil.jje.hs.kr'+ str(title['href'])
print(url)

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('a[target="_blank"]')
    a=title[1]
    print(a['href'])

else : 
    print(response.status_code)

url = 'https://jeil.jje.hs.kr'+ str(a['href'])
print(url)

webbrowser.open(url)

