import urllib3
import json
def weather_api(city):
	try:
		http = urllib3.PoolManager()

		r = http.request(
						'GET', 
						'http://api.openweathermap.org/data/2.5/weather',
						fields = {'q': city, 'units': 'metric', 'appid': '2bc3e79bb974a007818864813f53fd35' }
						)

		data = json.loads(r.data.decode('utf-8'))
		return [data['weather'][0]['description'], data['main']['temp']]
	except Exception as e:
		print (e)


print('{}\t{}\t{}'.format('City'.ljust(10), 'Description'.ljust(20), 'Temperature'.ljust(10)))
print("=" * 50)
for city in ['London', 'Nairobi', 'Kampala']:
	print('{}\t{}\t{}'.format(city.ljust(10), weather_api(city)[0].ljust(20), str(weather_api(city)[1]).ljust(10)))


