import requests

# const
baseURL = 'https://api.open-meteo.com/v1/forecast?'


def getcurrentweather(latitude, longitude):
    weather = requests.get(baseURL + 'latitude=' + latitude + '&longitude=' + longitude + '&current_weather=true')
    resp = weather.json()
    return resp['current_weather']['temperature']