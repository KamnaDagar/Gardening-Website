#FLOWER POTS 

import requests
import bs4
import lxml
import re
import pymongo

res = requests.get('https://www.trustbasket.com/collections/metal-flower-planters-pots')
soup = bs4.BeautifulSoup(res.text,'lxml')

#Connecting to the database.
myclient = pymongo.MongoClient("mongodb+srv://Kamnadagar:Gardenit@cluster0.mu77t.mongodb.net/")
mydb = myclient["Gardening"]
mycol = mydb["Flowerpots"]

prefix = "https://www.trustbasket.com"
titlefound = 0
linkfound = 0

for i in soup.select('#shopify-section-collection-template .product-title'):
	title = i.text.strip()
	print(title)
	titlefound =  titlefound + 1
	strlink = i.get('href')

	if strlink:
		linkfound =  linkfound + 1
		final = prefix + strlink
		print(final)
		mydict = { "Name": title , "Link": final }
		#x = mycol.insert_one(mydict)

print("Titles Found - ", titlefound)
print("Links Found - ", linkfound)

	

