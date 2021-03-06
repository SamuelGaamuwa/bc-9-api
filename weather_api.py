import urllib3
import json

http = urllib3.PoolManager()

def weather_api(city):
	try:
		r = http.request(
				'GET', 
				'http://api.openweathermap.org/data/2.5/weather',
				fields = {'q': city, 'units': 'metric', 'appid': '2bc3e79bb974a007818864813f53fd35' }
			)

		data = json.loads(r.data.decode('utf-8'))
		return {'name': 		city,
				'description':	data['weather'][0]['description'], 
					'temp':		data['main']['temp']}
	except Exception as e:
		return e


print('{}\t{}\t{}'.format('City'.ljust(10), 'Description'.ljust(20), 'Temperature'.ljust(10)))
print("=" * 50)
for city in ['London', 'Nairobi', 'Kampala']:
	info = weather_api(city)
	print ('{}\t{}\t{}'.format(info['name'].ljust(10), info['description'].ljust(20), str(info['temp']).ljust(10)))