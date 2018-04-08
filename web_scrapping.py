import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uopen

url="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"
client=uopen(url)
page_html=client.read()
client.close()
page=soup(page_html,"html.parser")

containers=page.findAll("div",{"class":"item-container"})
len(containers)
container=containers[0]
print(container)

container.div.div.a.img["title"]

container.a.img["title"]

#prices=page.findAll("li",{"class":"price-ship"})
#price=prices[0]
shipping=container.findAll("li",{"class":"price-ship"})
shipping[0].text
#for removing initial and final /r\r\n
shipping[0].text.strip()

#forming loop
for container in containers:
    brand=container.div.div.a.img["title"]
    brand_info=container.a.img["title"]
    shipping=container.findAll("li",{"class":"price-ship"})
    shipping=shipping[0].text.strip()
    print("brand" + brand)
    print("brand_info" + brand_info)
    print("shipping" + shipping)
    
