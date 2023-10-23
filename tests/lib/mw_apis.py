import string, random, json, os, sys

import requests
CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
from random import random
import logging as logger
from apiclient import APIClient
from tests.lib.requester import Requester
from requester import Requester
from generate_token import get_token
from uuid import UUID
import uuid
from faker import Faker
from json_compare import Jcompare
import tests.lib
import datetime
import random
import string
import lib.generate_token as generate_token
import lib.common as common
from datetime import datetime

def get_admin_token() -> str:
    token: str = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    return token

def get_staff_token() -> str:
    token: str = generate_token.generate_token(email="staffABC@gmail.com", password="Staff123!")
    return token

def create_a_staar_question(member_type: str, response_type: str = "Open Response Exact") -> dict:
    try:
        req = Requester()
        user_token: str = get_admin_token() if member_type == "admin" else get_staff_token()
        random_data: dict = common.get_staar_random_payload_data()
        header: dict = req.create_basic_headers(token=user_token)
        url: str = f"{req.base_url}/question/staar/create"
        payload: dict = {'data': '{"question_type": "STAAR", "update_note": "'+ random_data['random_question_content'] +'", "grade_level": 3, "release_date": "2023-05", "category": "' + random_data['random_category'] + '","keywords": ["math"], "student_expectations": ["'+ random_data['random_student_expectation'] +'"],"response_type": "' + response_type + '","question_content": "'+ random_data['random_question_content'] + '","question_img": "","options": [{"letter": "' + random_data['random_letter'] + '","content": "'+ random_data['random_question_content'] +'","image": "","unit": "pounds","is_answer": true},{"letter": "' + random_data['random_letter'] + '","content": "option b","image": "","unit": "pounds","is_answer": false}]}'}
        response = requests.request("POST", url, headers=header, data=payload)
        new_staar_questions: dict = json.loads(response.text)
    except Exception as e:
        return { "error": -1, "message": e}
    return new_staar_questions

def create_a_mathworld_question(member_type: str, response_type: str = "Open Response Exact") -> dict:
    try:
        req = Requester()
        user_token: str = get_admin_token() if member_type == "admin" else get_staff_token()
        random_data: dict = common.get_random_payload_data()
        header: dict = req.create_basic_headers(token=user_token)
        question2: str = common.get_random_question()
        url: str = f"{req.base_url}/question/mathworld/create"
        upload_file: list = []

        random_payload: dict = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 3, \
        "teks_code": "' + random_data['random_teks_code'] +'", \
        "subject": "' +  random_data['random_subject'] +'", \
        "topic": "' + random_data['random_topic'] +'", \
        "category": "' + random_data['random_category'] +'", \
        "keywords": ["happy"], \
        "student_expectations": ["' + random_data['random_student_expectations'] +'"], \
        "difficulty": "' + random_data['random_difficulty'] +'", \
        "points": 2, \
        "response_type": "' + response_type  +'", \
        "question_content": "' + random_data['random_question_content'] +'", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "' + random_data['random_letter'] +'", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + random_data['random_unit'] + '", \
            "is_answer": true \
            } \
        ] \
        }'}
        upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
        response = requests.request("POST", url, headers=header, data=random_payload, files=upload_file)
        json_response: dict = json.loads(response.text)
        return json_response
    except Exception as e:
        return { "error": -1, "message": e}

def create_a_college_question(member_type: str, response_type: str = "Open Response Exact") -> dict:
    try:
        req = Requester()
        user_token: str = get_admin_token() if member_type == "admin" else get_staff_token()
        random_data: dict = common.get_random_payload_data()
        header: dict = req.create_basic_headers(token=user_token)
        question2: str = common.get_random_question()
        url: str = f"{req.base_url}/question/college/create"
        upload_file: list = []

        random_payload: dict = {'data': '{ \
                "question_type": "College Level", \
                "classification": "' + random_data['random_classification'] +'", \
                "test_code": "123456", \
                "keywords": ["2"], \
                "response_type": "' + response_type + '", \
                "question_content": "' + question2 + '", \
                "question_img": "", \
                "options": [ \
                    { \
                    "letter": "' + random_data['random_letter'] + '", \
                    "content": "' + question2 + '", \
                    "image": "", \
                    "unit": "' + random_data['random_unit'] + '", \
                    "is_answer": true \
                    } \
                ] \
                }'}

        upload_file: list = []
        response = requests.request("POST", url, headers=header, data=random_payload, files=upload_file)
        json_response: dict = json.loads(response.text)
        return json_response
    except Exception as e:
        return { "error": -1, "message": e}

def update_question_status(uuid: str = "", status: str = "Pending") -> dict:
    try:
        req = Requester()
        user_token: str = get_admin_token()
        header: dict = req.create_basic_headers(token=user_token)
        random_data: dict = common.get_random_payload_data()
        patch_url: str = f"{req.base_url}/question/update/question_status/{uuid}"
        patch_payload: str = json.dumps({
            "status":  status,
            "update_note": f"{random_data['random_sentence']}",
            "reviewed_by": f"{random_data['random_name']}",
            "reviewed_at": f"{random_data['current_datetime']}"
    })
        patch_response: requests.Response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
        json_patch_response: dict = json.loads(patch_response.text)
        return json_patch_response
    except Exception as e:
        return { "error": -1, "message": e}

def register_staff_member() -> dict:
    req:Requester = Requester()
    user_token: str = get_admin_token()
    random_data: dict = json.loads(common.create_fake_register())
    payload: dict = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "'+ random_data['password'] +'", "repeat_password": "'+ random_data['password'] +'", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=user_token)
    url: str = f"{req.base_url}/staff/register"
    response: requests.Response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response: dict  = json.loads(response.text)
    return json_response
