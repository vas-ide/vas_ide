import json
from json.decoder import JSONDecodeError
import requests


# response = requests.get("https://playground.learnqa.ru/api/hello")
# print(response)
# print(response.text)
#
# payload = {"name": "VAS"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# print(response)
# print(response.text)
#
#
#
# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)
#
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print(F"Response is't JSON format")


# response = requests.get("https://playground.learnqa.ru/api/check_type", params={"key": "value"})
# print(response.status_code, response.text)
# response = requests.post("https://playground.learnqa.ru/api/check_type", data={"key": "value"})
# print(response.status_code, response.text)
# response = requests.post("https://playground.learnqa.ru/api/add_info")
# print(response.status_code, response.text)
# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# first_response = response.history[0]
# second_response = response
# print(first_response.url, "\n", second_response.url)
# headers = {"some_header": "123"}
# response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
# print(response.text, '\n', response.headers)
# payload = {"login": "secret_login", "password": "secret_pass"}
# response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
# print(response.text, '\n', response.status_code, '\n', response.cookies, '\n', dict(response.cookies), '\n', response.headers)

payload = {"login": "secret_login", "password": "secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
cookie_value = response1.cookies.get('auth_cookie')
cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})
response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
print(response2.text)
























