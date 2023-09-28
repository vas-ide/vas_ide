import requests

data = {
    "email": "vinkotov@example.com",
    "password": "1234"
}
response_login = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
auth_sid = response_login.cookies.get("auth_sid")
token = response_login.headers.get("x-csrf-token")
user_id_from_auth_method = response_login.json()["user_id"]


print(response_login.cookies, auth_sid)
print(response_login.headers, '\n', token)
print(response_login.json(), user_id_from_auth_method)

response_auth = requests.get(
    "https://playground.learnqa.ru/api/user/auth",
    headers={"x-csrf-token": token},
    cookies={"auth_sid": auth_sid}
)
print(response_auth.json())