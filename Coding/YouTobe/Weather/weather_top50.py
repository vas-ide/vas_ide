

import requests
import json



# url = "https://openweathermap.org/"
# url_api = "https://home.openweathermap.org/api_keys"
# response_api = requests.get(url_api)
# test_url = "http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={API key}"
test_url = "http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={16c2386c3555de5e2c6fb1907beb27c0}"
response = requests.get(url=test_url)
# response_json = json.loads(response.text)




print(response)
print(response.text)
# print(response_json)
# print(response_api.text)
#
