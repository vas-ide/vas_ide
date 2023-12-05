import requests
import allure
from lib.logger import Logger
from enviroment import ENV_OBJECT


class MyRequests():

    @staticmethod
    def get(url: str, params: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"GET request to URL {url}"):
            return MyRequests._send(url, params, headers, cookies, "GET")

    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"POST request to URL {url}"):
            return MyRequests._send(url, data, headers, cookies, "POST")

    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"PUT request to URL {url}"):
            return MyRequests._send(url, data, headers, cookies, "PUT")

    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"DELETE request to URL {url}"):
            return MyRequests._send(url, data, headers, cookies, "DELETE")

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        url = f"{ENV_OBJECT.get_base_url()}{url}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        Logger.add_request(url, data, headers, cookies, method)

        if method == "GET":
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Unsupported HTTP method: '{method}' was received")

        Logger.add_response(response)

        return response
