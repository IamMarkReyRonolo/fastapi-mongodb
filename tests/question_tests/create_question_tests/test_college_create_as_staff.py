from pytest import fixture
import pdb, requests
import os, sys, json

CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)

import logging as logger, pytest
import lib.common as common
import lib.generate_token as generate_token
from lib.requester import Requester

print("\n---- Setup Test ----\n")
@fixture(scope="module")
def get_staff_token():
    token = generate_token.generate_token(email="staffABC@gmail.com", password="Staff123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")

@pytest.mark.tc_001
def test_all_fields(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()
    # STAAR, College Level, Mathworld
    payload = {'data': '{ \
        "question_type": "College Level", \
        "classification": "SAT", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    # upload_file: list = []  # blank list
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_002
def test_question_type_eq_STAAR(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "STAAR", \
        "classification": "SAT", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question type must match to the endpoint use: College Level"

@pytest.mark.tc_003
def test_question_type_eq_Mathworld(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "Mathworld", \
        "classification": "SAT", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question type must match to the endpoint use: College Level"

@pytest.mark.tc_004
def test_question_type_eq_Blank(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "", \
        "classification": "SAT", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question_type is required"

@pytest.mark.tc_005
def test_question_type_college_level_with_whitespace(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level ", \
        "classification": "SAT", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_006
def test_question_type_numeric(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "1", \
        "classification": "SAT", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question type must match to the endpoint use: College Level"

@pytest.mark.tc_007
def test_question_type_special_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "@@@@", \
        "classification": "SAT", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question type must match to the endpoint use: College Level"

@pytest.mark.tc_008
def test_classification_numeric(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "1", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_009
def test_classification_type_blank_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": " ", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_010
def test_classification_type_TSI(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "TSI", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_011
def test_classification_type_ACT(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "ACT", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_012
def test_classification_type_ACT_with_whitespace(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "ACT ", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_013
def test_classification_type_invalid_special_symbol(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "@@@", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_014
def test_classification_blank(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "classification is required"

@pytest.mark.tc_015
def test_classification_eq_neg_5(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "-5", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_016
def test_classification_eq_neg_15(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "-15", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_017
def test_classification_invalid_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "!", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_018
def test_add_2_types_of_classifications(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT ACT", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_019
def test_add_2_SAT_with_whitespace(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT ", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"

@pytest.mark.tc_020
def test_add_2_TSI_with_whitespace(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "TSI ", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_021
def test_add_2_ACT_with_whitespace(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "ACT ", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_022
def test_classification_malformed(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "000000000000", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_023
def test_classification_type_college_level(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "college level", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_024
def test_classification_type_STAAR(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "STAAR", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_025
def test_classification_type_Mathworld(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "Mathworld", \
        "test_code": "123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_026
def test_test_code_whitespace(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "123456 ", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "test code must not exceed 6 characters"

@pytest.mark.tc_027
def test_test_code_neg_123456(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "-123456", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "test code must not exceed 6 characters"


@pytest.mark.tc_028
def test_test_code_special_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "@@@", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_029
def test_test_code_type_a(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "abc", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_030
def test_test_code_type_alpha_numeric(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "a1", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_031
def test_test_code_type_blank(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": " ", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_032
def test_test_code_str_0(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "0", \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_033
def test_test_code_type_neg_5(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": -5, \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "test code must be a string"


@pytest.mark.tc_034
def test_test_code_special_char(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": $#@, \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Invalid Payload"


@pytest.mark.tc_035
def test_test_code_empty(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": , \
        "keywords": ["2"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Invalid Payload"


@pytest.mark.tc_036
def test_keywords_str_55(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["55"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True



@pytest.mark.tc_037
def test_keywords_str_neg_123(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["-123"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_038
def test_keywords_str_abc(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["abc"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True

    
@pytest.mark.tc_039
def test_keywords_list_strings(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["mabra", "science", "english", "writing", "reading"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_040
def test_keywords_list_alpha_num(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science",3, "english", "writing", "reading", 5], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "all values in keywords must be string"


@pytest.mark.tc_041
def test_keywords_empty_list(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": [], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "keywords must not be empty"


@pytest.mark.tc_042
def test_keywords_missing(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keyword_missing": ["missing","english"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "keywords is required"

@pytest.mark.tc_043
def test_keywords_all_num(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": [3,1,3,2,1], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "all values in keywords must be string"


@pytest.mark.tc_044
def test_keywords_blank_entry(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math", "science", "english", "", "algegra", "geometry"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "a value in keywords should not be an empty string"


@pytest.mark.tc_045
def test_keywords_long_value(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra",], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Invalid Payload"

@pytest.mark.tc_046
def test_keywords_list_60_value(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["Math","Math","Math","Math","Math","Math",\
        "Math","Math","Math","Math","Math","Math","Math","Math",\
        "Math","Math","Math","Math","Math","Math","Math","Math",\
        "Math","Math","Math","Math","Math","Math","Math","Math",\
        "Math","Math","Math","Math","Math","Math","Math","Math",\
        "Math","Math","Math","Math","Math","Math","Math","Math",\
        "Math","Math","Math","Math","Math","Math","Math","Math",\
        "Math","Math","Math","Math","Math","Math"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"


@pytest.mark.tc_047
def test_response_type_blank(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "response_type is required"


@pytest.mark.tc_048
def test_response_type_blank_char(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": " ", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "response_type should not be an empty string"


@pytest.mark.tc_049
def test_response_type_not_ore(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Open Response", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"

@pytest.mark.tc_050
def test_response_type_is_ore(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_051
def test_response_type_is_ror(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Range Open Response", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True




@pytest.mark.tc_052
def test_response_type_not_ror(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Range Open", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"


@pytest.mark.tc_053
def test_response_type_mc(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Multiple Choice", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_054
def test_response_type_not_mc(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Multiple", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"


@pytest.mark.tc_055
def test_response_type_cb(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Checkbox", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_056
def test_response_type_not_cb(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Check box", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"


@pytest.mark.tc_057
def test_response_type_numeric(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "12", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"


@pytest.mark.tc_058
def test_response_type_spec_char(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "$$##@@", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"


@pytest.mark.tc_059
def test_question_content(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Open Response Exact", \
        "question_content": "this is a test", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "this is a test", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_060
def test_question_content_blank(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Open Response Exact", \
        "question_content": "", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "this is a test", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question_content is required"


@pytest.mark.tc_061
def test_question_content_missing(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Open Response Exact", \
        "missing_question_content": "this is a test", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "this is a test", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question_content is required"


@pytest.mark.tc_062
def test_question_content_lines_10(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Open Response Exact", \
        "question_content": "This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "this is a test", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question content should not exceed 1000 characters"


@pytest.mark.tc_063
def test_question_content_1000_char(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()
    char_limit: str = common.get_random_char(1000)
    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + char_limit + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "this is a test", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_064
def test_question_content_999_char(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()
    char_limit: str = common.get_random_char(999)
    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + char_limit + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "this is a test", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_065
def test_question_content_1001_char(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()
    char_limit: str = common.get_random_char(1001)
    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Open Response Exact", \
        "question_content": "' + char_limit + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "this is a test", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question content should not exceed 1000 characters"


@pytest.mark.tc_066
def test_question_content_blank_chars(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()
    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Open Response Exact", \
        "question_content": "    ", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "this is a test", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question content should not be empty"


@pytest.mark.tc_067
def test_question_content_content_numeric(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()
    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Open Response Exact", \
        "question_content": 3, \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "this is a test", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question content must be a string"


@pytest.mark.tc_068
def test_question_content_spec_char(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()
    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Open Response Exact", \
        "question_content": ")($@#@#)()", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "this is a test", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_069
def test_question_img(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()
    question_img: str = f"{CURRENT_DIR}\\tests\\images\\image_01.jpg"
    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Open Response Exact", \
        "question_content": ")($@#@#)()", \
        "question_img": "' + question_img + '", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "this is a test", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "missing_question_img is required"


@pytest.mark.tc_070
def test_question_img(get_staff_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/college/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()
    question_img: str = f"{CURRENT_DIR}\\tests\\images\\image_01.jpg"
    payload = {'data': '{ \
        "question_type": "college level", \
        "classification": "SAT", \
        "test_code": "12345", \
        "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
        "response_type": "Open Response Exact", \
        "question_content": "this is a test", \
        "missing_question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "this is a test", \
            "image": "", \
            "unit": "pound", \
            "is_answer": true \
            } \
        ] \
        }'}
        
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "missing_question_img is required"



    
