from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uOpen

URL = 'https://www.newegg.com/global/in-en/Mobile-Workstations/SubCategory/ID-3413?Tid=1297922'
uReq = uOpen(URL)
HtmlPage = uReq.read()
uReq.close()

PageSoup = soup(HtmlPage, "html.parser")
containers = PageSoup.find_all("div", {"class":"item-container"})
print(containers)

for container in containers:
	brand = container.div.div.a.img["title"]
	item = container.a.img["title"]
	priceClass = container.find_all("div", {"class":"item-action"})
	#for priceTag in priceClass:
	#	price = priceTag.ul.li["title"]

	print("brand  :" + brand)
	print("item   :" + item)
	#print("price  :" + price)
