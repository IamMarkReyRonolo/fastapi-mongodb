from pytest import fixture
import pdb, requests
import os, sys, json
from assertpy import assert_that

CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)

import logging as logger, pytest
import lib.common as common
import lib.generate_token as generate_token
from lib.requester import Requester

@fixture(scope="module")
def get_staff_token():
    token = generate_token.generate_token(email="staffABC@gmail.com", password="Staff123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")


global global_question_uuid

@pytest.mark.tc_001
def test_history_create(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.1(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": "this is a test", \
      "question_img": "", \
      "options": [ \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
        { \
          "letter": "b", \
          "content": "option b", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": false \
        } \
      ] \
    }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    global_question_uuid = json_response['question_uuid']
    get_history_url: str = f"{req.base_url}/question/fetch/history/{json_response['question_uuid']}"
    response = requests.request("GET", get_history_url, headers=header)
    json_response = json.loads(response.text)    
    assert_that(response.status_code).is_equal_to(200)
    assert_that(json_response['history'][0]['title']).is_equal_to("Create")
    assert_that(json_response['history'][0]['details']).is_equal_to("Created a STAAR question.")
    

