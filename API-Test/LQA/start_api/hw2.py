import json
import requests
import time

#
# print(f'---1---')
# json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
# string_upd = json.loads(json_text)
# for key, value in string_upd.items():
#     for key_add, value_add in value[1].items():
#         if value_add == 'And this is a second message':
#             print(value_add)
# print(f'---2---')
# response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
# for i in response.history:
#     print(i.url)
# print(f'---3---')
#
# # requests.request("method", "url", **kwargs)
#
# url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
# response = requests.get(url=url)
# response1 = requests.get(url=url, params={'method': 'GET'})
# response2 = requests.post(url=url, data={'method': 'POST'})
# response3 = requests.delete(url=url, data={'method': 'DELETE'})
# response4 = requests.put(url=url, data={'method': 'PUT'})
# response5 = requests.head(url, data={'method': 'head'})
# response6 = requests.options(url=url, data={'method': 'options'})
# print(response.text, '\n', response1.text, '\n', response2.text, '\n', response3.text, '\n', response4.text, '\n',
#       response5.text, '\n', response6.text)
# print(f'___for___')
# method_lst = ["GET", "POST", "DELETE", "PUT"]
# for i in method_lst:
#     print(i)
#     response1 = requests.get(url=url, params={'method': i})
#     response2 = requests.post(url=url, data={'method': i})
#     response3 = requests.delete(url=url, data={'method': i})
#     response4 = requests.put(url=url, data={'method': i})
#     print(response1.text, '\n', response2.text, '\n', response3.text, '\n', response4.text)
print(f'---4---')
# def analiZe():
#     url = "https://playground.learnqa.ru/ajax/api/longtime_job"
#     response_init = requests.get(url=url)
#     response_json = json.loads(response_init.text)
#     token = response_json['token']
#     seconds = response_json['seconds']
#     print(f'token={token}    seconds={seconds}')
#     response = requests.get(url=url, params={'token': token})
#     print(response.text)
#     response_json = json.loads(response.text)
#     response_status = response_json['status']
#     if response_status == "Job is NOT ready":
#         print(True, f"--->>>     {response_status}")
#     else:
#         print(False, f"Unknown status")
#     time.sleep(seconds)
#     response = requests.get(url=url, params={'token': token})
#     response_json = json.loads(response.text)
#     response_status = response_json["status"]
#     response_result = response_json["result"]
#     if response_status == "Job is ready" and response_result is not None:
#         print(True, f"--->>> result-{response_result} status-{response_status}")
#     else:
#         print(False, f"Unknown errors")
#
#
# analiZe()
print(f'---5---')

url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url_sec = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
login = "super_admin"
# password = ["123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou", "111111", "123123",
#             "abc123", "qwerty123", "1q2w3e4r", "admin", "qwertyuiop", "654321", "555555", "lovely", "7777777",
#             "welcome", "888888", "princess", "dragon", "password1", ]
password_lst = [
    "password", "123456", "123456789", "12345678", "12345", "qwerty", "abc123", "football", "1234567", "monkey",
    "111111", "letmein", "1234", "1234567890", "dragon", "baseball", "sunshine", "iloveyou", "trustno1",
    "princess",
    "adobe123[a]", "123123", "welcome", "login", "admin", "princess", "qwerty123", "solo", "1q2w3e4r", "master",
    "letmein", "666666", "photoshop[a]", "1qaz2wsx", "qwertyuiop", "ashley", "mustang", "121212", "starwars",
    "654321",
    "bailey", "access", "flower", "555555", "passw0rd", "shadow", "lovely", "7777777", "michael", "!@#$%^&*", "jesus",
    "password1", "hello",
    "charlie", "888888", "superman", "696969", "hottie",
    "freedom", "aa123456", "ninja", "azerty", "solo", "loveme", "whatever", "donald", "batman", "passw0rd",
    "zaq1zaq1", "qazwsx", "password1", "Football", "000000", "123qwe"
]

for i in password_lst:
    response = requests.post(url, data={"login": login, "password": i})
    # print(response.cookies)
    cookie_value = response.cookies.get('auth_cookie')
    cookies = {}
    if cookie_value is not None:
        cookies.update({'auth_cookie': cookie_value})
    response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
    if response2.text == "You are NOT authorized":
        pass
    else:
        print(f"PASSWORD-{i}  >>>   response-{response2.text}")

# "You are NOT authorized"
# response = requests.post(url, data={})+
