import requests

class Weather:
	def __init__(self, API_KEY):
		super(Weather, self).__init__()
		self.API_KEY = API_KEY
		self.BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


	def request_Infors(self, city):
	  request_url = f"{self.BASE_URL}?appid={self.API_KEY}&q={city}"
	  response = requests.get(request_url)

	  if response.status_code == 200:
	    data = response.json()
	    weather = data['weather'][0]['description']
	    temperature = round(data["main"]["temp"] - 273.15, 2)

	    return weather, temperature
	  else:
	    raise Exception("An error occurred.")