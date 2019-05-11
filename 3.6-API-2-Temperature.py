import requests

API_URL = 'http://api.openweathermap.org/data/2.5/weather'
CITY = input('Input city: ')

params = {
    'q': CITY,
    'appid': 'a80675e06f73ac9ce09ebe39b696a11d',
    'units': 'metric'
}

res = requests.get(API_URL, params=params)
data = res.json()
template = 'Current temperature in {} is {} C'

print(template.format(CITY, data['main']['temp']))
