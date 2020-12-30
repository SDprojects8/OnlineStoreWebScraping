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
	print("Container Length     :" + str(len(containers)))
	print("ratingsAll Length    :" + str(len(ratingsAll)))
	print("pricesAll Length     :" + str(len(pricesAll)))
	print("oldPricesAll Length  :" + str(len(oldPricesAll)))
	print("discountsAll Length  :" + str(len(discountsAll)))

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
		try:
			rating.append(ratingDiv.text)
		except IndexError:
			pass
		continue

	price = []
	for pricesDiv in pricesAll:
		#print(pricesDiv.text)
		try:
			price.append(pricesDiv.text)
		except IndexError:
			pass
		continue		

	oldPrice = []
	for oldPricesDiv in oldPricesAll:
		#print(oldPricesDiv.text)
		try:
			oldPrice.append(oldPricesDiv.text)
		except IndexError:
			pass
		continue

	discount = []
	for discountsDiv in discountsAll:
		#print(discountsDiv.text)
		try:
			discount.append(discountsDiv.text)
		except IndexError:
			pass
		continue

	itemNumber = 0
	
	for itemNumber in range(0,len(containers)):
		try:
			print ("##### " + itemName[itemNumber] + "|" + rating[itemNumber] + "|" + price[itemNumber] + "|" + oldPrice[itemNumber] + "|" + discount[itemNumber])
		except IndexError:
			pass
		continue



