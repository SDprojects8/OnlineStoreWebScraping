#!/usr/bin/python
# Sumit Das 2020 12 29
# Get Deals of the Day from Flipkart - Day_Bakeware_

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uOpen
import datetime
import csv

DT = datetime.datetime.now()
DateStamp = DT.strftime('%Y-%m-%d_%H-%M-%S')

# Inputs
pages=20
#pages = input("How many pages do you want to scan :  ")
baseURL = 'https://www.flipkart.com/kitchen-cookware-serveware/bakeware/pr?sid=upp%2Cbgd&offer=nb:mp:114b43bd28,nb:mp:114c76b528&hpid=raTquFPh2dVzU7zKGnuhF6p7_Hsxr70nj65vMAAFKlc=&fm=neo%2Fmerchandising&iid=M_9911b1fd-044c-46b5-9132-43310cf1cfbb_2.RBVM3W9LQHB8&ssid=h6bfjo0ng00000001609335246968&otracker=clp_omu_infinite_Deals%2Bof%2Bthe%2BDay_3_2.dealCard.OMU_INFINITE_dotd-store_dotd-store_RBVM3W9LQHB8&cid=RBVM3W9LQHB8'
#CSVpath = input("Provide the full path where CSV reports shall be stored ... :  ")
CSVfile = "../collect/Flipkart_Deals.of.the.Day_Bakeware_%s.CSV" % DateStamp #Assuming you run from scripts directory
#OutCSV = open(CSVpath + "/" + CSVfile, 'w', newline='')

# Main

OutCSV = open(CSVfile, 'w', encoding="utf-8", newline='')
OutWriter = csv.writer(OutCSV)

print("SlNo.|itemName|rating|price|oldPrice|discount")
#OutWriter.writerow("SlNo.|itemName|rating|price|oldPrice|discount")
OutWriter.writerow("IRVPODL")
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
	reviewsAll = PageSoup.find_all("span", {"class":"_2_R_DZ"})
	pricesAll = PageSoup.find_all("div", {"class":"_30jeq3"})
	oldPricesAll = PageSoup.find_all("div", {"class":"_3I9_wc"})
	discountsAll = PageSoup.find_all("div", {"class":"_3Ay6Sb"})
	imageLinksAll = PageSoup.find_all("div", {"class":"_2rpwqI"})
	#containers = PageSoup.find_all("div")
	#print(containers)
	#print("###########\n")
	#print("Container Length     :" + str(len(containers)))
	#print("ratingsAll Length    :" + str(len(ratingsAll)))
	#print("pricesAll Length     :" + str(len(pricesAll)))
	#print("oldPricesAll Length  :" + str(len(oldPricesAll)))
	#print("discountsAll Length  :" + str(len(discountsAll)))

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

	review = []
	for reviewSpan in reviewsAll:
		#print(reviewSpan.text)
		try:
			review.append(reviewSpan.text)
			#print(review)
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
	
	for itemNumber in range(0,len(containers)):
		try:
			#print ("##### " + itemName[itemNumber] + "|" + rating[itemNumber] + "|" + price[itemNumber] + "|" + oldPrice[itemNumber] + "|" + discount[itemNumber])
			#OutWriter.writerow([itemName[itemNumber], rating[itemNumber], price[itemNumber], oldPrice[itemNumber], discount[itemNumber]]) #, "https://www.flipkart.com" + imageLink[itemNumber]])
			print("Printing Line # %d " % itemNumber)
			print ("##### " + itemName[itemNumber] + "|" + rating[itemNumber] + "|" + review[itemNumber] + "|" + price[itemNumber] + "|" + oldPrice[itemNumber] + "|" + discount[itemNumber])
			OutWriter.writerow([itemName[itemNumber], rating[itemNumber], review[itemNumber], price[itemNumber], oldPrice[itemNumber], discount[itemNumber], "https://www.flipkart.com" + imageLink[itemNumber]])
		except IndexError:
			pass
		continue


OutCSV.close()


