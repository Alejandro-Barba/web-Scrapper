
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?d=graphic+card'

#Opens the connection
uClient = uReq(my_url)

#Save the html in a variable
page_html = uClient.read()

#Closes the conecction
uClient.close()

#html parsing
page_soup = soup(page_html, 'html.parser')

#Select all cards
containers = page_soup.findAll("div",{"class":"item-container"})
print(len(containers))

filename = "products.csv"
f = open(filename, "w")

headers = "product_name, price\n"
f.write(headers)

for container in containers:
    #title = container.div.a['title']
    item_title = container.findAll('a',{'class':'item-title'})
    product_name = item_title[0].text
    price = container.findAll('li',{'class':'price-current'})[0].strong.text

    #print('title:' + title)
    #print('product_name: ' + product_name)
    #print('price:' + price)

    f.write(product_name.replace(',','|') + "," + price.replace(',','') + "\n")

f.close()