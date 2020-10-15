import requests
from bs4 import BeautifulSoup

response = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.09927000000005&lon=-118.33806999999996#.XIRJ81NKgUE')

soup = BeautifulSoup(response.content, 'html.parser')
main = soup.find(id='seven-day-forecast-body')

week_list = main.find_all(class_='tombstone-container')
for i in week_list:
    print(i.find(class_='period-name').get_text())
    print(i.find(class_='short-desc').get_text())
    print(i.find(class_='temp').get_text())