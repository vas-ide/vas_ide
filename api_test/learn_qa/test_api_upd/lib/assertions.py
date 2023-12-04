from requests import Response
import json


class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_values(params: list,
                           expected_values: list = ["password", "username", "firstName", "lastName", "email"]):
        for item in params:
            assert item in expected_values and len(params) == len(
                expected_values), f"Error: {item} is not in expected or unexpected number of parameters: {len(expected_values)}"

    @staticmethod
    def assert_json_value_by_email(name):
        assert "@" in name, "Email is required '@' "

    @staticmethod
    def assert_json_value_by_short_name(name):
        assert len(name) > 1, f"Username is too short"

    @staticmethod
    def assert_json_value_by_long_name(name):
        assert len(name) < 250, f"Username is too long"

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code: Expected-{expected_status_code} Actual-{response.status_code}"

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON  doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        for name in names:
            assert name in response_as_dict, f"Response JSON  doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name not in response_as_dict, f"Response JSON have key '{name}' But it present"

    @staticmethod
    def assert_json_has_not_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        for name in names:
            assert name not in response_as_dict, f"Response JSON have key '{name}' But it present"
