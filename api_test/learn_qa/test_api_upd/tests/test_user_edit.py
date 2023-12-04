import random as rand
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserEdit(BaseCase):
    def test_edit_just_creating_user(self):
        register_data = self.prepare_registration_data()
        response_edit = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response_edit, 200)
        Assertions.assert_json_has_key(response_edit, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response_edit, "id")

        # LOGIN
        login_data = {
            "email": email,
            "password": password
        }
        response_login = MyRequests.post("/user/login", data=login_data)
        # auth_sid = response_login.cookies.get("auth_sid")
        # token = response_login.headers.get("x-csrf-token")
        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_header(response_login, "x-csrf-token")

        # EDIT
        new_name = f"Changed Name"
        # new_name = f"Changed Name - {rand.randint(100500, 10005000)}"
        response_change = MyRequests.put(f"/user/{user_id}",
                                         headers={"x-csrf-token": token},
                                         cookies={"auth_sid": auth_sid},
                                         data={"firstName": new_name},
                                         )
        Assertions.assert_code_status(response_change, 200)
        # GET
        response_user_id = MyRequests.get(f"/user/{user_id}",
                                          headers={"x-csrf-token": token},
                                          cookies={"auth_sid": auth_sid})

        Assertions.assert_json_value_by_name(response_user_id, "firstName", new_name,
                                             f"Wrong name of the user after edit.")
