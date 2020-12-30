from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uOpen

pages=10
baseURL = 'https://www.flipkart.com/audio-video/pr?sid=0pm&marketplace=FLIPKART&offer=nb:mp:1154f86928,nb:mp:11cc851a28&hpid=u0KJH80uWRAYeEJJpMIZYap7_Hsxr70nj65vMAAFKlc=&fm=neo%2Fmerchandising&iid=M_62ce2069-ba72-4633-a9f3-272c137582ba_2.VLO9AZPF3DJW&ppt=clp&ppn=dotd-store&ssid=m03cg1ws6o0000001609272953413&otracker=clp_omu_infinite_Deals%2Bof%2Bthe%2BDay_2_2.dealCard.OMU_INFINITE_dotd-store_dotd-store_VLO9AZPF3DJW&cid=VLO9AZPF3DJW'

print("SlNo.|itemName|rating|price|oldPrice|discount")
for pg in range(0,pages):
	URL = (baseURL + "&page=" + str(pg))
	#print("\n\n\n ############# \n Now URL is :    " + URL)
	#URL = 'https://www.flipkart.com/audio-video/pr?sid=0pm&marketplace=FLIPKART&offer=nb:mp:1154f86928,nb:mp:11cc851a28&hpid=u0KJH80uWRAYeEJJpMIZYap7_Hsxr70nj65vMAAFKlc=&fm=neo%2Fmerchandising&iid=M_62ce2069-ba72-4633-a9f3-272c137582ba_2.VLO9AZPF3DJW&ppt=clp&ppn=dotd-store&ssid=m03cg1ws6o0000001609272953413&otracker=clp_omu_infinite_Deals%2Bof%2Bthe%2BDay_2_2.dealCard.OMU_INFINITE_dotd-store_dotd-store_VLO9AZPF3DJW&cid=VLO9AZPF3DJW'
	#URL = 'https://www.flipkart.com/audio-video/pr?sid=0pm&marketplace=FLIPKART&offer=nb%3Amp%3A1154f86928%2Cnb%3Amp%3A11cc851a28&hpid=u0KJH80uWRAYeEJJpMIZYap7_Hsxr70nj65vMAAFKlc%3D&fm=neo%2Fmerchandising&iid=M_62ce2069-ba72-4633-a9f3-272c137582ba_2.VLO9AZPF3DJW&ppt=clp&ppn=dotd-store&ssid=m03cg1ws6o0000001609272953413&otracker=clp_omu_infinite_Deals%2Bof%2Bthe%2BDay_2_2.dealCard.OMU_INFINITE_dotd-store_dotd-store_VLO9AZPF3DJW&cid=VLO9AZPF3DJW&page=2'
	uReq = uOpen(URL)
	HtmlPage = uReq.read()
	uReq.close()

	PageSoup = soup(HtmlPage, "html.parser")
	containers = PageSoup.find_all("div", {"class":"_4ddWXP"})
	ratingsAll = PageSoup.find_all("div", {"class":"_3LWZlK"})
	pricesAll = PageSoup.find_all("div", {"class":"_30jeq3"})
	oldPricesAll = PageSoup.find_all("div", {"class":"_3I9_wc"})
	discountsAll = PageSoup.find_all("div", {"class":"_3Ay6Sb"})
	#containers = PageSoup.find_all("div")
	#print(containers)
	#print("###########\n")

	itemName = []
	for container in containers:
		itemName.append(container.a.img["alt"])
		#rating = container.div.div
		#rating = container.find_all("div", {"class:":"_3LWZlK"})
		#print("##### Item Name:   " + itemName + "\n")
		#print("###### Item: " + itemName + "\n##Rating: " + rating + "~~~~~\n\n")
		#print(rating + " - " + itemName)
		#item = container.a.img["title"]

	rating = []
	for ratingDiv in ratingsAll:
		#print(ratingDiv.text)
		rating.append(ratingDiv.text)

	price = []
	for pricesDiv in pricesAll:
		#print(pricesDiv.text)
		price.append(pricesDiv.text)

	oldPrice = []
	for oldPricesDiv in oldPricesAll:
		#print(oldPricesDiv.text)
		oldPrice.append(oldPricesDiv.text)

	discount = []
	for discountsDiv in discountsAll:
		#print(discountsDiv.text)
		discount.append(discountsDiv.text)

	itemNumber = 0
	
	for itemNumber in range(0,len(containers)):
		print ("##### " + itemName[itemNumber] + "|" + rating[itemNumber] + "|" + price[itemNumber] + "|" + oldPrice[itemNumber] + "|" + discount[itemNumber])





"""containers = PageSoup.find_all("div", {"class":"item-container"})
print(containers)

for container in containers:
	brand = container.div.div.a.img["title"]
	item = container.a.img["title"]
	priceClass = container.find_all("div", {"class":"item-action"})
	#for priceTag in priceClass:
	#	price = priceTag.ul.li["title"]

	print("brand  :" + brand)
	print("item   :" + item)
	#print("price  :" + price)"""
