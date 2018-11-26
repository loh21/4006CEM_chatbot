import requests

def weather():
    city = input('Enter your city : ')

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=1ee311d03b2c63e7fdab818a30c8624e&units=metric'.format(city)

    req = requests.get(url)

    data = req.json()

    temp = data['main']['temp']
    mini = data['main']['temp_min']
    maxi = data['main']['temp_max']
    humid = data['main']['humidity']
    speed = data['wind']['speed']
    cloud = data['clouds']['all']
    desc = data['weather'][0]['description']

    print('Temperature : {}°C'.format(temp))
    print('Minimum Temperature : {}°C'.format(mini))
    print('Maximum Temperature : {}°C'.format(maxi))
    print('Humidity : {}%'.format(humid))
    print('Wind Speed : {}mph'.format(speed))
    print('Average Cloud Cover : {}%'.format(cloud))
    print('Short Description : {}'.format(desc))

weather()

