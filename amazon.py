import requests 
from bs4 import BeautifulSoup

response = requests.get('https://www.amazon.com/s?k=lenovo+x1+carbon&ref=nb_sb_noss_2')
# url = 'https://www.amazon.de/s?k=lenovo+x1+carbon&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2RH2QG2Z7TDJJ&sprefix=lenovo+x1%2Caps%2C356&ref=nb_sb_ss_i_2_9'
headers = {"User-Agent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content,'html.parser')


info = soup.find(class_='a-size-medium').get_text()
price = soup.find(class_='a-price-whole').get_text()

print(info)
if (price < 500):
    send_mail('Now you cant hbdv')
print(price)
