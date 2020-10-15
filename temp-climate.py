import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.usclimatedata.com/climate/united-states/us')
print(len(r.text))

soup = BeautifulSoup(r.text,features="lxml")
# print(soup.title) # string

# print(soup.p)  # .text .parent prettify
# print(soup.a)  # title

# for link in soup.find_all('a'):
#     print(link.get('href'))

base_url = 'https://www.usclimatedata.com'
state_links = []
for link in soup.find_all('a'):
    url = link.get('href')
    if url and '/climate/' in url and '/climate/united-states/us' not in url:
        state_links.append(url)
print(state_links[1])

r = requests.get(base_url + state_links[4])
soup = BeautifulSoup(r.text,features="lxml")
print(soup.title.string)

rows = soup.find_all('tr')

print(rows[1])

### filtering
# for row in rows:
#     print(row)
rows = [row for row in rows if 'Average high' in str(row)]
print(rows[0])

# ### States temps
high_temps = []
for row in rows:
    tds = row.find_all('td')
    # print(tds)
    for i in range(0,6):
        high_temps.append(tds[i].text)
print(high_temps)

# ### State Names
state = soup.title.string.split()[1]
# print(state)


data = {}
data[state] = high_temps
# print(data)

#
# Geting all cities
#
data = {}
for state_link in state_links:
    url = base_url + state_link
    r = requests.get(base_url + state_link)
    soup = BeautifulSoup(r.text)
    rows = soup.find_all('tr')
    rows = [row for row in rows if 'Average high' in str(row)]
    high_temps = []
    for row in rows:
        tds = row.find_all('td')
        for i in range(0,6):
            high_temps.append(tds[i].text)
    s = soup.title.string
    state = s[s.find(' '):s.find('-')].strip()
    data[state] = high_temps
print(data[5]) # data.items()

