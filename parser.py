from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

root = "https://www.google.com/"
link = "https://www.google.com/search?q=hera+pheri+cast&oq=hera+p&aqs=chrome.1.69i57j69i59l2j46i67i433j46i67j69i60l3.1875j0j7&sourceid=chrome&ie=UTF-8"
req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html5lib')
actors = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")
#actors = (soup.find('div', class_={'BNeawe vvjwJb AP7Wnd'}).get_text())
for actor in actors:
    print(actor, end="\n"*2)