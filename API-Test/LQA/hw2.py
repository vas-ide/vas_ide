import json
import requests

print(f'---1---')
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
string_upd = json.loads(json_text)
for key, value in string_upd.items():
    for key_add, value_add in value[1].items():
        if value_add == 'And this is a second message':
            print(value_add)
print(f'---2---')
response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
for i in response.history:
    print(i.url)
print(f'---3---')

# requests.request("method", "url", **kwargs)

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
response = requests.get(url=url)
response1 = requests.get(url=url, params={'method': 'GET'})
response2 = requests.post(url=url, data={'method': 'POST'})
response3 = requests.delete(url=url, data={'method': 'DELETE'})
response4 = requests.put(url=url, data={'method': 'PUT'})
response5 = requests.head(url, data={'method': 'head'})
response6 = requests.options(url=url, data={'method': 'options'})
print(response.text, '\n', response1.text, '\n', response2.text, '\n', response3.text, '\n', response4.text, '\n',
      response5.text, '\n', response6.text)
print(f'---4---')

print(f'---5---')

print(f'---6---')
