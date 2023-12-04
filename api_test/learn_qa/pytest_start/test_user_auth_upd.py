import requests
import pytest


class TestUserAuth:
    exclude_params = [
        ("no_cookie"), ("no_token")
    ]

    def setup_method(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        response_login = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        assert "auth_sid" in response_login.cookies, f"There is no auth cookies in the response"
        assert "x-csrf-token" in response_login.headers, f"There is no CSRF token header in the response"
        assert "user_id" in response_login.json(), f"There is no user id in the response"

        self.auth_sid = response_login.cookies.get("auth_sid")
        self.token = response_login.headers.get("x-csrf-token")
        self.user_id_from_auth_method = response_login.json()["user_id"]

    def test_auth_user(self):
        response_auth = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        assert "user_id" in response_auth.json(), f" There is no user id in the second response"
        user_id_from_check_method = response_auth.json()["user_id"]
        assert self.user_id_from_auth_method == user_id_from_check_method, f"User id from auth method is not equal user id from check method"

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):


        if condition == "no_cookie":
            response = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token": self.token}
            )
        else:
            response = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )
        assert "user_id" in response.json(), f"There is no user in the second response"
        user_id_from_check_method = response.json()["user_id"]
        assert user_id_from_check_method == 0, f"User is  authorized with condition {condition}"









