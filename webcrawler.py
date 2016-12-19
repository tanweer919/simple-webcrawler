from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
url = input("Enter the url to be crawled:")
req = Request(url)
fhand = urlopen(req)
html = fhand.read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
