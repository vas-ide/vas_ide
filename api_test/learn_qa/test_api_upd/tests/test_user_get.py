import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserGet(BaseCase):
    def setup_method(self):
        self.data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        response_login = MyRequests.post("/user/login", data=self.data)
        assert "auth_sid" in response_login.cookies, f"There is no auth cookies in the response"
        assert "x-csrf-token" in response_login.headers, f"There is no CSRF token header in the response"
        assert "user_id" in response_login.json(), f"There is no user id in the response"

        self.auth_sid = response_login.cookies.get("auth_sid")
        self.token = response_login.headers.get("x-csrf-token")
        self.user_id_from_auth_method = response_login.json()["user_id"]

    def test_get_user_details_not_auth(self):
        response = MyRequests.get("/user/2")
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    def test_get_user_details_as_same_user(self):
        response_auth = MyRequests.get(
            f"/user/{self.user_id_from_auth_method}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
        )
        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response_auth, expected_fields)

    @pytest.mark.parametrize("id", [("85813"), ("85812"), ("85811"), ("85810"), ("85000"), ("84000")])
    # def get_id(self):
    #     for item in range(85000, 85100):
    #         yield (f"{item}")
    #
    # @pytest.mark.parametrize("id", [(get_id())])
    def test_auth_check_wrong(self, id):
        response_wrong_id = MyRequests.get(
            f"/user/{id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
        )
        expected_fields = ["username"]
        Assertions.assert_json_has_keys(response_wrong_id, expected_fields)
        unexpected_fields = ["email", "firstName", "lastName"]
        Assertions.assert_json_has_not_keys(response_wrong_id, unexpected_fields)
