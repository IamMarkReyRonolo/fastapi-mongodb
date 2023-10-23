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



@fixture(scope="module")
def get_staff_token():
    token = generate_token.generate_token(email="staffABC@gmail.com", password="Staff123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")


@pytest.mark.tc_001
def test_all_fields(get_staff_token):
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
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_002
def test_blank_question_type(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "question_type is required"


@pytest.mark.tc_003
def test_invalid_question_type_mathworld(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
        "question_type": "mathworld", \
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
    assert response.status_code == 400
    assert json_response['detail'] == "question type must match to the endpoint use: STAAR"

@pytest.mark.tc_004
def test_question_type_blank_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "  ", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.3(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "question type must match to the endpoint use: STAAR"

@pytest.mark.tc_005
def test_question_type_college_level(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "college level", \
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
    assert response.status_code == 400
    assert json_response['detail'] == "question type must match to the endpoint use: STAAR"

@pytest.mark.tc_006
def test_question_type_numeric(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": 1, \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "question_type must be a string"

@pytest.mark.tc_007
def test_question_type_special_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "@@@@", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "question type must match to the endpoint use: STAAR"


@pytest.mark.tc_008
def test_grade_level_eq_0(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 0, \
      "release_date": "2024-02", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "invalid grade level: should only be between 3 to 12"

@pytest.mark.tc_009
def test_grade_level_eq_13(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 13, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "invalid grade level: should only be between 3 to 12"

@pytest.mark.tc_010
def test_grade_level_eq_12(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 12, \
      "release_date": "2024-02", \
      "category": "3", \
      "keywords": ["math"], \
      "student_expectations": ["A.3(A)"], \
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
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_011
def test_grade_level_eq_neg_3(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": -3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "invalid grade level: should only be between 3 to 12"

@pytest.mark.tc_012
def test_grade_level_eq_neg_12(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": -12, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "invalid grade level: should only be between 3 to 12"


@pytest.mark.tc_013
def test_grade_level_eq_neg_13(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": -13, \
      "release_date": "2024-02", \
      "category": "3", \
      "keywords": ["math"], \
      "student_expectations": ["A.3(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "invalid grade level: should only be between 3 to 12"

@pytest.mark.tc_014
def test_grade_level_eq_neg_0(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": -0, \
      "release_date": "2024-02", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "invalid grade level: should only be between 3 to 12"

@pytest.mark.tc_015
def test_grade_level_str_3(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": "3", \
      "release_date": "2024-02", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "grade level must be an integer"

@pytest.mark.tc_016
def test_grade_level_str_12(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": "12", \
      "release_date": "2024-02", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "grade level must be an integer"

@pytest.mark.tc_017
def test_grade_level_blank(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": , \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "Invalid Payload"

@pytest.mark.tc_018
def test_grade_level_eq_1(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 1, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert response.text == '{"detail":"invalid grade level: should only be between 3 to 12"}'

@pytest.mark.tc_019
def test_grade_level_special_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": @, \
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
    assert response.status_code == 400
    assert json_response['detail'] == 'Invalid Payload'

@pytest.mark.tc_020
def test_grade_level_blank_str(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": "", \
      "release_date": "2024-02", \
      "category": "3", \
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
    assert response.status_code == 400
    assert response.text == '{"detail":"grade_level is required"}'

@pytest.mark.tc_021
def test_release_date_current(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_current_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "' + yyyy_mm + '", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.3(A)"], \
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
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_022
def test_release_date_future(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_future_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "' + yyyy_mm + '", \
      "category": "3", \
      "keywords": ["math"], \
      "student_expectations": ["A.3(A)"], \
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
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_023
def test_release_date_past(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "' + yyyy_mm + '", \
      "category": "3", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_024
def test_release_date_mm_yyyy(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "03-2024", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid format: format accepted xxxx-xx | year-month"

@pytest.mark.tc_025
def test_release_date_mmyyyy(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "032024", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid format: format accepted xxxx-xx | year-month"

@pytest.mark.tc_026
def test_release_date_mm_bs_yyyy(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "03\2024", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid format: format accepted xxxx-xx | year-month"


@pytest.mark.tc_027
def test_release_date_yyyy_bs_mm(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2023\03", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.3(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "Invalid Payload"

@pytest.mark.tc_028
def test_release_date_blank(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "release_date is required"


@pytest.mark.tc_029
def test_release_date_invalid_month(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-15", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid - date should not be in future"

@pytest.mark.tc_030
def test_release_date_leap_year(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.3(A)"], \
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
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_031
def test_release_date_leap_year_with_day(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-31-02", \
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
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid format: format accepted xxxx-xx | year-month"


@pytest.mark.tc_032
def test_release_date_invalid_leap_year(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2023-31-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid format: format accepted xxxx-xx | year-month"

@pytest.mark.tc_033
def test_release_date_blank_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "   ", \
      "category": "2", \
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
    assert response.status_code == 400
    assert json_response['detail'] == "release date should not be empty"

@pytest.mark.tc_034
def test_release_date_malformed(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "00000000000", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid format: format accepted xxxx-xx | year-month"


@pytest.mark.tc_035
def test_release_date_missing(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "somthing else": "00000000000", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "release_date is required"

@pytest.mark.tc_036
def test_release_date_us_format(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "03-12-2024", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid format: format accepted xxxx-xx | year-month"

@pytest.mark.tc_037
def test_question_type_missing(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "something_else": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "question_type is required"

@pytest.mark.tc_038
def test_grade_level_missing(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "something": 3, \
      "release_date": "2024-03", \
      "category": "2", \
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
    assert response.status_code == 400
    assert json_response['detail'] == "grade_level is required"


@pytest.mark.tc_039
def test_release_date_numeric(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": 2024-03, \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    assert response.status_code == 400
    assert json_response['detail'] == "Invalid Payload"

# category
@pytest.mark.tc_040
def test_category_numeric(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": 1, \
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
    assert response.status_code == 400
    assert json_response['detail'] == "category must be a string"


@pytest.mark.tc_041
def test_category_numeric_string(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_042
def test_category_missing(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "something else": "1", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "category is required"

@pytest.mark.tc_043
def test_category_eq_math(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "math", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Valid category is from 1 to 5"



@pytest.mark.tc_044
def test_category_eq_science(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "science", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Valid category is from 1 to 5"



@pytest.mark.tc_045
def test_category_eq_english(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "english", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Valid category is from 1 to 5"


@pytest.mark.tc_046
def test_category_eq_blank(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "category is required"


@pytest.mark.tc_047
def test_category_eq_blank_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "  ", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "category should not be empty"


@pytest.mark.tc_048
def test_category_eq_special_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "!@#$%^*(*(*))", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Valid category is from 1 to 5"



@pytest.mark.tc_049
def test_category_eq_neg_num(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "-13232", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Valid category is from 1 to 5"



@pytest.mark.tc_050
def test_keywords_list_strings(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "1", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["A.2(A)"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_051
def test_keywords_list_alpha_num(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science",3, "english", "writing", "reading", 5], \
      "student_expectations": ["A.2(A)"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "all values in keywords must be string"


@pytest.mark.tc_052
def test_keywords_list_special_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science","@@", "english", "writing", "reading", "#@#@"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_053
def test_keywords_empty_list(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": [], \
      "student_expectations": ["A.2(A)"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "keywords must not be empty"


@pytest.mark.tc_054
def test_keywords_missing(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keyword_missing": ["math", "english"], \
      "student_expectations": ["A.2(A)"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "keywords is required"


@pytest.mark.tc_055
def test_keywords_all_num(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": [3, 1, 5, 4, 8, 9], \
      "student_expectations": ["a.1(A)"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "all values in keywords must be string"


@pytest.mark.tc_056
def test_keywords_blank_entry(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math", "science", "english", "", "algegra", "geometry"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "a value in keywords should not be an empty string"


@pytest.mark.tc_057
def test_keywords_long_value(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra",], \
      "student_expectations": ["A.2(A)"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Invalid Payload"


@pytest.mark.tc_058
def test_keywords_list_50_value(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["Math","Math","Math","Math","Math","Math",\
        "Math","Math","Math","Math","Math","Math","Math","Math",\
        "Math","Math","Math","Math","Math","Math","Math","Math",\
        "Math","Math","Math","Math","Math","Math","Math","Math",\
        "Math","Math","Math","Math","Math","Math","Math","Math",\
        "Math","Math","Math","Math","Math","Math","Math","Math",\
        "Math","Math","Math","Math",], \
      "student_expectations": ["A,2(A)"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Invalid Payload"


@pytest.mark.tc_059
def test_student_expectations_num_str(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["A.2(A)"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_060
def test_student_expectations_special_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["@"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Invalid student expectations"



@pytest.mark.tc_061
def test_student_expectations_list_str_num(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["31", "2.1", "3.3"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Invalid student expectations"



@pytest.mark.tc_062
def test_student_expectations_list_num_num(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": [31, 2.1], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "student_expectations must be a string"


@pytest.mark.tc_063
def test_student_expectations_list_str_spec_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["31", @], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Invalid Payload"


@pytest.mark.tc_064
def test_student_expectations_list_num_str(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": [31, "2.1"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "student_expectations must be a string"


@pytest.mark.tc_065
def test_student_expectations_list_empty(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": [], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "student_expectations must not be empty"


@pytest.mark.tc_066
def test_student_expectations_list_missing(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "missing_student_expectations": ["2.1", "2.3", "4.5"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "student_expectations is required"


@pytest.mark.tc_067
def test_student_expectations_list_blank_strs(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["", "", ""], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "student_expectations should not be an empty string"

@pytest.mark.tc_068
def test_response_type_blank(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": [A.1(A)], \
      "response_type": , \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Invalid Payload"


@pytest.mark.tc_069
def test_response_type_blank_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["2.3", "4.3", "3.3"], \
      "response_type": "", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "response_type is required"

@pytest.mark.tc_070
def test_response_type_missing(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["A.1(A)", "A.1(B)", "A.2(A)"], \
      "missing_response_type": "Open Response Exact", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "response_type is required"

@pytest.mark.tc_071
def test_response_type_not_ore(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["A.1(A)", "A.2(A)", "A.1(B)"], \
      "response_type": "Open Response", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"

@pytest.mark.tc_072
def test_response_type_is_ore(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["A.1(A)", "A.1(B)", "A.2(C)"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_073
def test_response_type_is_ror(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["A.1(A)", "A.2(A)", "A.1(B)"], \
      "response_type": "Range Open Response", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_074
def test_response_type_not_ror(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["A.1(A)", "A.2(B)", "A.2(B)"], \
      "response_type": "Range Open", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"

@pytest.mark.tc_075
def test_response_type__mc(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["A.1(A)", "A.2(B)", "A.1(B)"], \
      "response_type": "Multiple Choice", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_076
def test_response_type__not_mc(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["A.1(A)", "A.1(B)", "A.2(B)"], \
      "response_type": "Multiple", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"

@pytest.mark.tc_077
def test_response_type_cb(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["A.1(A)", "A.2(A)", "A.1(B)"], \
      "response_type": "Checkbox", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_078
def test_response_type_not_cb(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["A.1(A)", "A.2(B)", "A.1(B)"], \
      "response_type": "Check box", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"

@pytest.mark.tc_079
def test_response_type_numeric(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["A.1(A)", "A.2(B)", "A.1(B)"], \
      "response_type": 1, \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "response_type must be a string"

@pytest.mark.tc_080
def test_response_type_spec_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-03", \
      "category": "2", \
      "keywords": ["math","algebra", "science", "english", "writing", "reading"], \
      "student_expectations": ["A.1(A)", "A.1(B)", "A.2(A)"], \
      "response_type": "@@@@@", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"

@pytest.mark.tc_081
def test_question_content(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_082
def test_question_content_blank(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.1(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": "", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question_content is required"

@pytest.mark.tc_083
def test_question_content_missing(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.1(A)"], \
      "response_type": "Open Response Exact", \
      "missing_question_content": "this is a test", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question_content is required"

@pytest.mark.tc_084
def test_question_content_lines_10(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.1(A)"], \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'question content should not exceed 1000 characters'


@pytest.mark.tc_085
def test_question_content_1000_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1000)
    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.1(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": "' + char_limit + '", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_086
def test_question_content_999_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(999)
    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": "' + char_limit + '", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True


@pytest.mark.tc_087
def test_question_content_1001_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.1(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": "' + char_limit + '", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question content should not exceed 1000 characters"

@pytest.mark.tc_088
def test_question_content_blank_chars(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": "   ", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'question content should not be empty'

@pytest.mark.tc_089
def test_question_content_numeric(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.1(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": 5, \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'question content must be a string'

@pytest.mark.tc_090
def test_question_content_spec_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.1(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": "!#$!@#$@#f", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_091
def test_question_img(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    question_img: str = f"{CURRENT_DIR}\\tests\\images\\image_01.jpg"
    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.1(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": "this is a test", \
      "question_img": "' + question_img + '", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'Invalid Payload'

@pytest.mark.tc_092
def test_question_img_missing(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    question_img: str = f"{CURRENT_DIR}\\tests\\images\\image_01.jpg"
    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.1(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": "this is a test", \
      "missing_question_img": "", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'missing_question_img is required'


@pytest.mark.tc_093
def test_question_img_blank_char(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    question_img: str = f"{CURRENT_DIR}\\tests\\images\\image_01.jpg"
    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.1(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": "this is a test", \
      "question_img": "   ", \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'invalid image insertion: image must be added through the Form, not in payload.'


@pytest.mark.tc_094
def test_question_img_numeric(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    question_img: str = f"{CURRENT_DIR}\\tests\\images\\image_01.jpg"
    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(B)"], \
      "response_type": "Open Response Exact", \
      "question_content": "this is a test", \
      "question_img": 1, \
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
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'image must be a string'


@pytest.mark.tc_095
def test_options_single(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    question_img: str = f"{CURRENT_DIR}\\tests\\images\\image_01.jpg"
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
        } \
      ] \
    }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_096
def test_options_group_10(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    question_img: str = f"{CURRENT_DIR}\\tests\\images\\image_01.jpg"
    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        } \
      ] \
    }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_097
def test_options_group_60(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    question_img: str = f"{CURRENT_DIR}\\tests\\images\\image_01.jpg"
    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        },\
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        }, \
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
        }, \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        } \
      ] \
    }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request(
        "POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_098
def test_options_letter_blank(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": "this is a test", \
      "question_img": "", \
      "options": [ \
        { \
          "letter": "", \
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
    assert response.status_code == 400
    assert json_response['detail'] == 'letter is required'


@pytest.mark.tc_099
def test_options_content_blank(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.1(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": "this is a test", \
      "question_img": "", \
      "options": [ \
        { \
          "letter": "b", \
          "content": "", \
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
    assert response.status_code == 400
    assert json_response['detail'] == 'content is required'

@pytest.mark.tc_100
def test_options_image_blank(get_staff_token):
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
          "letter": "b", \
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
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_101
def test_options_unit_blank(get_staff_token):
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
          "letter": "b", \
          "content": "this is a test", \
          "image": "", \
          "unit": "", \
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
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_102
def test_options_is_answer_numeric(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": "this is a test", \
      "question_img": "", \
      "options": [ \
        { \
          "letter": "b", \
          "content": "this is a test", \
          "image": "", \
          "unit": "", \
          "is_answer": true \
        }, \
        { \
          "letter": "b", \
          "content": "option b", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": 1 \
        } \
      ] \
    }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'is_answer should be type boolean'


@pytest.mark.tc_103
def test_options_is_answer_blank_str(get_staff_token):
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
          "letter": "b", \
          "content": "this is a test", \
          "image": "", \
          "unit": "", \
          "is_answer": "" \
        }, \
        { \
          "letter": "b", \
          "content": "option b", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": "" \
        } \
      ] \
    }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'is_answer is required'


@pytest.mark.tc_104
def test_options_is_answer_true(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": "this is a test", \
      "question_img": "", \
      "options": [ \
        { \
          "letter": "b", \
          "content": "this is a test", \
          "image": "", \
          "unit": "", \
          "is_answer": true \
        }, \
        { \
          "letter": "b", \
          "content": "option b", \
          "image": "", \
          "unit": "pounds", \
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

@pytest.mark.tc_105
def test_options_is_answer_false(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": "this is a test", \
      "question_img": "", \
      "options": [ \
        { \
          "letter": "b", \
          "content": "this is a test", \
          "image": "", \
          "unit": "", \
          "is_answer": false \
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
    assert common.is_valid_uuid(json_response['question_uuid']) == True

@pytest.mark.tc_106
def test_options_is_answer_both_missing(get_staff_token):
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
          "letter": "b", \
          "content": "this is a test", \
          "image": "", \
          "unit": "", \
          "missing_is_answer": false \
        }, \
        { \
          "letter": "b", \
          "content": "option b", \
          "image": "", \
          "unit": "pounds", \
          "missing_is_answer": false \
        } \
      ] \
    }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'is_answer is required in option object'


@pytest.mark.tc_107
def test_options_is_answer_single_missing(get_staff_token):
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
          "letter": "b", \
          "content": "this is a test", \
          "image": "", \
          "unit": "", \
          "is_answer": false \
        }, \
        { \
          "letter": "b", \
          "content": "option b", \
          "image": "", \
          "unit": "pounds", \
          "missing_is_answer": false \
        } \
      ] \
    }'}

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'is_answer is required in option object'


@pytest.mark.tc_108
def test_options_unit_missing(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(B)"], \
      "response_type": "Open Response Exact", \
      "question_content": "this is a test", \
      "question_img": "", \
      "options": [ \
        { \
          "letter": "b", \
          "content": "this is a test", \
          "image": "", \
          "missing_unit": "", \
          "is_answer": false \
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
    assert response.status_code == 400
    assert json_response['detail'] == 'missing_unit is required'

@pytest.mark.tc_109
def test_options_content_1000_char(get_staff_token):
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
          "content": "' + common.get_random_char(1000) + '", \
          "image": "", \
          "unit": "pounds", \
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

@pytest.mark.tc_110
def test_options_invalid_option_image(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(B)"], \
      "response_type": "Open Response Exact", \
      "question_content": "this is a test", \
      "question_img": "", \
      "options": [ \
        { \
          "letter": "a", \
          "content": "' + common.get_random_char(1000) + '", \
          "image": "' + str(upload_file) + '", \
          "unit": "pounds", \
          "is_answer": true \
        } \
      ] \
    }'}

    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'invalid option image insertion: image must be added through the Form, not in payload.'

@pytest.mark.tc_111
def test_options_invalid_question_image(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.1(A)"], \
      "response_type": "Open Response Exact", \
      "question_content": "this is a test", \
      "question_img": "' + str(upload_file) + '", \
      "options": [ \
        { \
          "letter": "a", \
          "content": "' + common.get_random_char(1000) + '", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": true \
        } \
      ] \
    }'}

    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'invalid image insertion: image must be added through the Form, not in payload.'

@pytest.mark.tc_112
def test_options_is_answer_True(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "1", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(B)"], \
      "response_type": "Open Response Exact", \
      "question_content": "this is a test", \
      "question_img": "", \
      "options": [ \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": True \
        } \
      ] \
    }'}

    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'Invalid Payload'

@pytest.mark.tc_113
def test_options_is_answer_False(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/question/staar/create"
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")

    payload = {'data': '{ \
      "question_type": "STAAR", \
      "grade_level": 3, \
      "release_date": "2024-02", \
      "category": "2", \
      "keywords": ["math"], \
      "student_expectations": ["A.2(B)"], \
      "response_type": "Open Response Exact", \
      "question_content": "this is a test", \
      "question_img": "", \
      "options": [ \
        { \
          "letter": "a", \
          "content": "this is a test", \
          "image": "", \
          "unit": "pounds", \
          "is_answer": False \
        } \
      ] \
    }'}

    response = requests.request("POST", url, headers=header, data=payload, files=upload_file)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'Invalid Payload'

