import requests
import bs4
import lxml
import re
import pymongo

#Connecting to the database.
myclient = pymongo.MongoClient("mongodb+srv://Kamnadagar:Gardenit@cluster0.mu77t.mongodb.net/")
mydb = myclient["Gardening"]
mycol = mydb["Fruitseeds"]
prefix = "https://www.trustbasket.com"

#This function takes collections from the starting page and for each collection call the scrapedata function.
def scrapecollections(starturl):
  res = requests.get(starturl)
  soup = bs4.BeautifulSoup(res.text,'lxml')
  collections = soup.select('.h5 a')
  #We selected each collection title and link.
  for i in collections:
    collectionname  = i.text.strip()
    collectionlink = i.get('href')
    if collectionlink:
      collink = prefix + collectionlink
      scrapedata(collink , 1 , collectionname)



#This function is to directly scrape from Collection Pages.
#We are passing URL, Page Number  and Collection name to this function. 
def scrapedata(urlprefix ,page , collectionname):
  # initial url , and page parameters are added here. 
  url = urlprefix +'?page='+ str(page)
  # print(url)
  res = requests.get(url)
  soup = bs4.BeautifulSoup(res.text,'lxml')
  products = soup.select('#shopify-section-collection-template .product-title')
  for i in products:
    title = i.text.strip()
    strlink = i.get('href')
    if strlink:
      final = prefix + strlink
      # print(final)
      mydict = { "Name": title , "Link": final  , "Collection" : collectionname}
      #print(mydict)
      #x = mycol.insert_one(mydict)
      print("DONE!") 
  if len(products) > 0:
    newpage = page + 1
    # print("scraping page no ", newpage)
    scrapedata(urlprefix , newpage , collectionname)


#this is the initial point of our script to tell which method to call first
starturl = "https://www.trustbasket.com/pages/greens-and-fruit-seeds"
scrapecollections(starturl)  