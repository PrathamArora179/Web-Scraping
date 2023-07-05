#install the requirements
# pip install htlm5lib
# pip install requests
# pip install bs4

import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"

#get the html
r=requests.get(url)
htmlContent=r.content  
#print(htmlContent)

#parse the html
soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)

#html tree traversel
title=soup.title
print(type(title)) #tag object
print(type(title.string)) #navigablestring
print(type(soup)) #beautifulsoap

#get all the para and anchor tags from the page
paras=soup.find_all('p')
print(paras)
anchors=soup.find_all('a')
print(anchors)



 