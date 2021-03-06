from flask import session
import requests


class UserClient:

    @staticmethod
    def get_user(api_key):
        headers = {
            'Authorization': api_key
        }

        response = requests.request(method="GET", url='http://0.0.0.0:2021/api/user', headers=headers)
        if response.status_code == 401:
            return False

        user = response.json()
        return user
