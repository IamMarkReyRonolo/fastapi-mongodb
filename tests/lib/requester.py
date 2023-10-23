from email import header
from email.mime import application
import json, pdb, sys, os, requests
from turtle import pd
from urllib import response
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
WORKING_DIR = os.path.abspath(CURRENT_DIR)
PARENT_DIR = os.path.join(CURRENT_DIR, '..')
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)
from dotenv import load_dotenv
import lib.generate_token as generate_token

load_dotenv()

BASE_URL = os.getenv('BASE_URL')

class Requester(object):
    def __init__(self):
        self.admin_email: str = "adminXYZ@gmail.com"
        self.admin_password: str = "Admin123!"
        self.base_url = 'http://localhost:8000'
        self.env = os.environ.get('ENV', 'test')
        self.headers: dict = {"Content-Type": "application/json"}
        self.expired_token: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IldlbGxpbmd0b25fMjAyMiFAZ21haWwuY29tIiwiZXhwIjoxNjYzNDU2OTQxfQ.rmERAE2wRsFM3BEopf6ARRvhlp_F80ypbtMIcVTeQWg'

    def post(self, endpoint: str, payload: str, headers: dict = {}, **kwargs):
        url = self.base_url  + endpoint
        if not headers:
            headers = self.headers
        results = requests.post(url = url, data = json.dumps(payload), headers = headers, files=[])
        return results

    def mw_post(self, endpoint: str, payload, headers: dict = {}, files=[]):
        url = self.base_url + endpoint
        if not headers:
            headers = self.headers
        response = requests.request("POST", url, headers={}, data=payload, files=files)
        return response

    def get(self, endpoint: str, payload: dict = {}, headers: dict = {}):
        url = self.base_url + endpoint
        if not headers:
            headers = self.headers
        results = requests.get(url=url, headers=headers)
        return results

    def mw_get(self, endpoint: str, payload: dict = {}, headers: dict = {}):
        url = self.base_url + '/' + endpoint
        if not headers:
            headers = self.headers
        response = requests.request("GET", url, headers=headers, data=payload)
        return response

    def mw_put(self, endpoint: str, payload: str, headers: dict = {}):
        url = self.base_url + '/' + endpoint
        if not headers:
            headers = self.headers
        response = requests.request("PUT", url, headers=headers, data=payload)
        return response

    def delete(self, endpoint: str, headers: dict = {}):
        url = self.base_url + endpoint
        if not headers:
            headers = self.headers
        results = requests.delete(url=url, headers=headers)
        return results

    def update(self, endpoint: str, payload: dict = {}, headers: dict = {}):
        url = self.base_url + endpoint
        if not headers:
            headers = self.headers
        results = requests.put(
            url=url, data=json.dumps(payload), headers=headers)
        return results

    def mw_remove(self, endpoint: str, headers: dict = {}):
        url = self.base_url + '/' + endpoint
        if  not headers:
            headers = self.headers
        response = requests.request("DELETE", url, headers=headers, data={})
        return response

    def create(self, endpoint: str, payload: dict, headers: dict = {}, files=[]):
        url = self.base_url + endpoint
        if not headers:
            headers = self.headers
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        return response

    def get_token(self, email: str, password: str) -> str:
        token: str = generate_token.generate_token(email, password)
        return token

    def get_admin_token(self) -> str:
        return generate_token.generate_token(self.admin_email, self.admin_password)

    def create_basic_headers(self, token: str) -> dict:
        headers = {"Authorization": "Bearer " + token }
        return headers

    def fetch_all_questions_with_query(self, query: str = ""):
        try:
            header: dict = self.create_basic_headers(token=self.get_admin_token())
            payload: dict = json.loads("{\"query\":\"\",\"variables\":{}}")
            response = self.mw_get(f"question/fetch/all?{query}", headers=header,  payload=payload)
            return response
        except Exception as error:
            pass

    def fetch_all_questions(self):
        try:
            header: dict = self.create_basic_headers(token=self.get_admin_token())
            payload: dict = json.loads("{\"query\":\"\",\"variables\":{}}")
            return self.mw_get(f"question/fetch/all", headers=header,  payload=payload)
        except Exception as error:
            pass

    def count_dict_values(self, response_dict: dict, key: str, value) -> int:
        count : int = 0
        try:
            for item in response_dict["data"]:
                if item[key] == value:
                    count += 1
            return count
        except Exception as error:
            pass
        return count
