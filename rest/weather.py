import urllib.parse
import requests
from pprint import pprint

city = input('Enter City: ')
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=YOUR-KEY-HERE&units=metric'.format(city)

res = requests.get(url)
data = res.json()

pprint (data)

