import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(data.text,'html.parser')
soup.find_all('tag_name',{'class','class_name'})
soup.find_all('tag_name',{'id','id_name'})
for name in  soup.find_all('strong'):
    print(name.text)
