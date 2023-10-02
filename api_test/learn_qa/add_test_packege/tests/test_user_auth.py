
import requests
import pytest
f


class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"), ("no_token")
    ]

    def setup(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        response_login = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        self.auth_sid = self.get_cookie(response_login, "auth_sid")
        self.token = self.get_header(response_login, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response_login, "user_id")

    def test_auth_user(self):
        response_auth = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )
        Assertions.assert_json_value_by_name(
            response_auth,
            f"user_id",
            self.user_id_from_auth_method,
            f"User id from auth method is not equal to user id from check method "
        )

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
        Assertions.assert_json_value_by_name(
            response,
            "user_id",
            0,
            f"User is  authorized with condition {condition}"
        )
