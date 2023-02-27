import requests

baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID':'4b00c2ff9a2101e1680241065f344942', 'q':'Seattle,US'}

response = requests.get(baseUrl, params=parameters)

print(response.content)

