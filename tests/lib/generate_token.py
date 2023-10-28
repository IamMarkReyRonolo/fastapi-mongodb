import pdb, sys, os, string, random, json, pytest, requests
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
WORKING_DIR = os.path.abspath(CURRENT_DIR)
PARENT_DIR = os.path.join(CURRENT_DIR, '..')
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)

import logging as logger
from lib.fake_data import create_member_data
from lib.requester import Requester


base_url = "http://127.0.0.1:8000"

def get_token() -> dict:     # type: ignore
    req = Requester()     
    member_data = create_member_data()
    response: object = req.post(endpoint='/member/create', payload = member_data)      # type: ignore
    headers = {}
    if response.status_code == 201:   
        url = "http://127.0.0.1:8000/member/login"
        payload={'username': member_data['email'],'password': member_data['mw_password']}                
        response = requests.request("POST", url, headers=headers, data=payload)
        if  response.status_code == 200:
            token_info: dict = json.loads(response.content.decode("utf-8"))
            token_info.update({"email": member_data['email']})
            return token_info
        
def generate_token(email: str = "", password: str = "")-> str:
    try: 
        payload = json.dumps({
            "email": f"{email}",
            "password": f"{password}"
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f"{base_url}" + "/v1/team_accounts/login", data=payload, headers=headers)
        if response.status_code == 200:
            token_info: dict = json.loads(response.content.decode("utf-8"))
            return token_info['access_token']
        else:
            return "-1"
    except Exception as e:
        logger.error(f"Error in generate_token: {e}")
        return "-1"