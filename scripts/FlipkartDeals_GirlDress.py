#!/usr/bin/python
# Sumit Das 2020 12 29
# Get Deals of the Day from Flipkart - Flipkart_GirlDresses_

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uOpen
import datetime
import csv

DT = datetime.datetime.now()
DateStamp = DT.strftime('%Y-%m-%d_%H-%M-%S')

# Inputs
pages=20
#pages = input("How many pages do you want to scan :  ")
baseURL = 'https://www.flipkart.com/clothing-and-accessories/pr?sid=clo&otracker=categorytree&p%5B%5D=facets.ideal_for%255B%255D%3DGirls&p%5B%5D=facets.ideal_for%255B%255D%3DBoys%2B%2526%2BGirls&p%5B%5D=facets.ideal_for%255B%255D%3DBaby%2BBoys%2B%2526%2BBaby%2BGirls&p%5B%5D=facets.ideal_for%255B%255D%3DBaby%2BGirls&otracker=nmenu_sub_Baby%20%26%20Kids_0_Girls%27%20Clothing'
#CSVpath = input("Provide the full path where CSV reports shall be stored ... :  ")
CSVfile = "../collect/Flipkart_GirlDresses_%s_.CSV" % DateStamp #Assuming you run from scripts directory
#OutCSV = open(CSVpath + "/" + CSVfile, 'w', newline='')

# Main

OutCSV = open(CSVfile, 'w', encoding="utf-8", newline='')
OutWriter = csv.writer(OutCSV)

print("Brand|ItemName|ItemType|price|oldPrice|discount|Link")
#OutWriter.writerow("SlNo.|itemName|rating|price|oldPrice|discount")
OutWriter.writerow("BITPODL")
for pg in range(0,pages):
	URL = (baseURL + "&page=" + str(pg))
	#print("\n\n\n ############# \n Now URL is :    " + URL)
	#URL = 'https://www.flipkart.com/audio-video/pr?sid=0pm&marketplace=FLIPKART&offer=nb:mp:1154f86928,nb:mp:11cc851a28&hpid=u0KJH80uWRAYeEJJpMIZYap7_Hsxr70nj65vMAAFKlc=&fm=neo%2Fmerchandising&iid=M_62ce2069-ba72-4633-a9f3-272c137582ba_2.VLO9AZPF3DJW&ppt=clp&ppn=dotd-store&ssid=m03cg1ws6o0000001609272953413&otracker=clp_omu_infinite_Deals%2Bof%2Bthe%2BDay_2_2.dealCard.OMU_INFINITE_dotd-store_dotd-store_VLO9AZPF3DJW&cid=VLO9AZPF3DJW'
	#URL = 'https://www.flipkart.com/audio-video/pr?sid=0pm&marketplace=FLIPKART&offer=nb%3Amp%3A1154f86928%2Cnb%3Amp%3A11cc851a28&hpid=u0KJH80uWRAYeEJJpMIZYap7_Hsxr70nj65vMAAFKlc%3D&fm=neo%2Fmerchandising&iid=M_62ce2069-ba72-4633-a9f3-272c137582ba_2.VLO9AZPF3DJW&ppt=clp&ppn=dotd-store&ssid=m03cg1ws6o0000001609272953413&otracker=clp_omu_infinite_Deals%2Bof%2Bthe%2BDay_2_2.dealCard.OMU_INFINITE_dotd-store_dotd-store_VLO9AZPF3DJW&cid=VLO9AZPF3DJW&page=2'
	uReq = uOpen(URL)
	HtmlPage = uReq.read()
	uReq.close()

	PageSoup = soup(HtmlPage, "html.parser")
	brandsALL = PageSoup.find_all("div", {"class":"_2WkVRV"})
	itemsALL = PageSoup.find_all("div", {"class":"_2B099V"})
	itemTypesALL = PageSoup.find_all("div", {"class":"_3eWWd-"})
	#ratingsAll = PageSoup.find_all("div", {"class":"_3LWZlK"})
	pricesAll = PageSoup.find_all("div", {"class":"_30jeq3"})
	oldPricesAll = PageSoup.find_all("div", {"class":"_3I9_wc"})
	discountsAll = PageSoup.find_all("div", {"class":"_3Ay6Sb"})
	imageLinksAll = PageSoup.find_all("div", {"class":"_1xHGtK _373qXS"})
	#containers = PageSoup.find_all("div")
	#print(containers)
	#print("###########\n")
	#print("Brand     Length     :" + str(len(brands)))
	#print("Item      Length     :" + str(len(itemsALL)))
	#print("ratingsAll Length    :" + str(len(ratingsAll)))
	#print("pricesAll Length     :" + str(len(pricesAll)))
	#print("oldPricesAll Length  :" + str(len(oldPricesAll)))
	#print("discountsAll Length  :" + str(len(discountsAll)))

	brand = []
	for brandDIV in brandsALL:
		#print(ratingDiv.text)
		try:
			brand.append(brandDIV.text)
		except IndexError:
			pass
		continue

	itemName = []
	for itemNameDiv in itemsALL:
		itemName.append(itemNameDiv.a.text)
		#rating = container.div.div
		#rating = container.find_all("div", {"class:":"_3LWZlK"})
		#print("##### Item Name:   " + itemName + "\n")
		#print("###### Item: " + itemName + "\n##Rating: " + rating + "~~~~~\n\n")
		#print(rating + " - " + itemName)
		#item = container.a.img["title"]
	
	itemType = []
	for itemTypeDiv in itemTypesALL:
		#print(ratingDiv.text)
		try:
			itemType.append(itemTypeDiv.text)
		except IndexError:
			pass
		continue

	# rating = []
	# for ratingDiv in ratingsAll:
	#	# print(ratingDiv.text)
		# try:
			# rating.append(ratingDiv.text)
		# except IndexError:
			# pass
		# continue

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

	imageLink = []
	for imageLinkDiv in imageLinksAll:
		#print(imageLinkDiv.text)
		try:
			imageLink.append(imageLinkDiv.a['href'])
			#print(imageLink)
		except IndexError:
			pass
		continue

	itemNumber = 0
	
	for itemNumber in range(0,len(itemsALL)):
		try:
			# Link will not be printed but captured in csv file only
			print ("##### " + brand[itemNumber] + "|" + itemName[itemNumber] + "|" + itemType[itemNumber] + "|" + price[itemNumber] + "|" + oldPrice[itemNumber] + "|" + discount[itemNumber]) # + "|" + imageLink[itemNumber])
			OutWriter.writerow([brand[itemNumber], itemName[itemNumber], itemType[itemNumber], price[itemNumber], oldPrice[itemNumber], discount[itemNumber], "https://flipkart.com" + imageLink[itemNumber]])
		except IndexError:
			pass
		continue


OutCSV.close()


