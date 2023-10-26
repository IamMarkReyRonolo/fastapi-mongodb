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
from payloads.valid_question_payloads import get_valid_successful_mathworld_payload

@fixture(scope="module")
def get_admin_token():
    print("\n---- Setup Test ----\n")
    token = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")

#===========================test 1=========================================================
@pytest.mark.tc_001
def test_all_fields(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_mathworld_payload()

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"

#===============================test 2 =========================================================
@pytest.mark.tc_002
def test_grade_level_eq_12(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_mathworld_payload()
    payload['grade_level'] = 12


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"


#=========================================test 3=======================================================
@pytest.mark.tc_003
def test_blank_question_type(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_mathworld_payload()
    payload['question_type'] = ""

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==  "question_type is required"



#========================================test 5============================================
@pytest.mark.tc_005
def test_question_type_empty_string(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_mathworld_payload()
    payload['question_type'] = " "

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==  "question_type is required"



#===============================test 7==========================================================

@pytest.mark.tc_007
def test_invalid_question_type_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_mathworld_payload()
    payload['question_type'] = "9"

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid question type"

#===============================test 8=====================================================

@pytest.mark.tc_008
def test_invalid_question_type_includes_empty_string(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_mathworld_payload()
    payload['question_type'] = "Math World"

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==  "invalid question type"

#==================================test 9================================================

@pytest.mark.tc_009
def test_invalid_question_type_with_leading_white_space(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_mathworld_payload()
    payload['question_type'] = "   MathWorld"

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] ==  "Successfully Added Question"

#==================================test 10========================================================

@pytest.mark.tc_010
def test_invalid_question_type_with_trailing_white_space(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_mathworld_payload()
    payload['question_type'] = "MathWorld    "

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] ==  "Successfully Added Question"

    #=========================test 11========================================================

@pytest.mark.tc_011
def test_invalid_question_type_with_special_characters(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_mathworld_payload()
    payload['question_type'] = "$$$$"

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==  "invalid question type"

#===============================test 12========================================================

@pytest.mark.tc_012
def test_invalid_grade_level_out_of_range_higher(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 20, \
        "teks_code": "A.1", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==  "invalid grade level: should only be between 3 to 12"

#============================test 13===================================================

@pytest.mark.tc_013
def test_invalid_grade_level_out_of_range_lower(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 1, \
        "teks_code": "A.1", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==  "invalid grade level: should only be between 3 to 12"

#==========================test 14=========================================================

@pytest.mark.tc_014
def test_invalid_grade_level_leading_zero(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 09, \
        "teks_code": "A.1", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Payload"

#==========================test 15=================================================

@pytest.mark.tc_015
def test_invalid_grade_level_nonInteger(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 10.6, \
        "teks_code": "A.1", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "grade level must be an integer"

#============================test 16====================================================

@pytest.mark.tc_016
def test_invalid_grade_level_empty(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": "", \
        "teks_code": "A.1", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "grade_level is required"

#==========================test 17==========================================================

@pytest.mark.tc_017
def test_invalid_grade_level_non_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": "abc", \
        "teks_code": "A.1", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "grade level must be an integer"

#============================test 18 ==========================================================

@pytest.mark.tc_018
def test_invalid_grade_level_special_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": "$$", \
        "teks_code": "A.1", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "grade level must be an integer"

#=========================test 19===============================================

@pytest.mark.tc_019
def test_invalid_grade_level_negative_integer(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": -11, \
        "teks_code": "A.1", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==    "invalid grade level: should only be between 3 to 12"

#=================================test 20=====================================================

@pytest.mark.tc_020
def test_invalid_grade_level_valid_but_string(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": "11", \
        "teks_code": "A.1", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "grade level must be an integer"

#=============================test 21============================================

@pytest.mark.tc_021
def test_invalid_grade_level_blank(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": , \
        "teks_code": "A.1", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Payload"

#==================================test 22 ===================================================

@pytest.mark.tc_022
def test_invalid_teks_code_out_of_range(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.25", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Teks Code"

#=====================================test 23 ============================================


@pytest.mark.tc_023
def test_invalid_teks_code_non_A(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "X.1", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Teks Code"

#==========================test 24===================================================


@pytest.mark.tc_024
def test_invalid_teks_code_mallformed(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.05", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Teks Code"

#===========================test 25==============================================


@pytest.mark.tc_025
def test_invalid_teks_code_multiple_periods(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A..5", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Teks Code"

#==============================test 26==================================================


@pytest.mark.tc_026
def test_invalid_teks_code_no_period(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A5", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Teks Code"

#=========================================test 27========================================


@pytest.mark.tc_027
def test_invalid_teks_code_missing_letter(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": ".5", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Teks Code"

#===============================test 28==================================


@pytest.mark.tc_028
def test_invalid_teks_white_space(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A .5", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Teks Code"

#======================================test 29=====================================


@pytest.mark.tc_029
def test_invalid_teks_code_multiple_A(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "AAA.5", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Teks Code"

#===============================test 30=======================================


@pytest.mark.tc_030
def test_invalid_teks_leading_zero(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.05", \
        "subject": "Algebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Teks Code"

#=================================test 31============================================


@pytest.mark.tc_031
def test_missing_subject(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": , \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Payload"

#=================================test 32=================================================


@pytest.mark.tc_032
def test_empty_subject(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": " ", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "subject should not be empty"

#=====================================test 33=================================================


@pytest.mark.tc_033
def test_subject_with_special_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "A%%%%$$ra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Subject"

#=============================test 34=======================================================


@pytest.mark.tc_034
def test_subject_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "12345", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Subject"

#===============================test 35=============================================


@pytest.mark.tc_035
def test_subject_not_AlgebraI(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Calculus", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Subject"

#=================================test 36=========================================


@pytest.mark.tc_036
def test_malformed_subject(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "ALgeBrA I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Subject"

#=================================test 37====================================


@pytest.mark.tc_037
def test_subject_integer(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": 12, \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "subject must be a string"

#=================================test 38=====================================


@pytest.mark.tc_038
def test_subject_with_white_spaces(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "A l g e b r a I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Subject"

#==========================test 39=====================================================


@pytest.mark.tc_039
def test_subject_incorrect_spelling(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Allgebra I", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Subject"

#===========================test 40===================================


@pytest.mark.tc_040
def test_subject_all_small_case(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "algebra i", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Subject"

#=============================test 41====================================


@pytest.mark.tc_041
def test_subject_algebra_1(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra 1", \
        "topic": "quantity", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Subject"

#=================================test 42==============================================


@pytest.mark.tc_042
def test_missing_topic(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": , \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Payload"

#================================test 43==============================================


@pytest.mark.tc_043
def test_empty_topic(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": " ", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "topic should not be empty"

#================================test 44==========================================


@pytest.mark.tc_044
def test_numeric_topic(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": 12345, \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "topic must be a string"

#=====================================test 45=====================================


@pytest.mark.tc_045
def test_topic_with_special_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "$$$$$$", \
        "category": "1", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] ==   "Successfully Added Question"

#=====================================test 46==============================================


@pytest.mark.tc_046
def test_category_out_of_range(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "20", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Valid category is from 1 to 5"

#==========================test 47================================================


@pytest.mark.tc_047
def test_category_negative(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": -5, \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "category must be a string"

#==============================test 48============================================


@pytest.mark.tc_048
def test_category_non_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "math", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Valid category is from 1 to 5"

#=================================test 49===========================================


@pytest.mark.tc_049
def test_category_special_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "$5", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Valid category is from 1 to 5"

#=================================test 50============================================


@pytest.mark.tc_050
def test_category_zero(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "0", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Valid category is from 1 to 5"

#==============================test 51=======================================


@pytest.mark.tc_051
def test_category_blank(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": , \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Payload"

#==================================test 52==================================


@pytest.mark.tc_052
def test_category_empty(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": " ", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "category should not be empty"

#==============================test 53=======================================


@pytest.mark.tc_053
def test_category_malformed(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "00004", \
        "keywords": ["happy"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Valid category is from 1 to 5"

#===============================test 54======================================


@pytest.mark.tc_054
def test_keywords_missing(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "4", \
        "keywords": , \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Payload"

#===============================test 55============================================

@pytest.mark.tc_055
def test_keywords_empty(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": [" "], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "a value in keywords should not be an empty string"

#==================================test 56=========================================

@pytest.mark.tc_056
def test_keywords_special_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["$$$##$$$"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] ==   "Successfully Added Question"

#=================================test 57=========================================


@pytest.mark.tc_057
def test_student_expectation_missing(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": , \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Payload"

#==================================test 58=====================================


@pytest.mark.tc_058
def test_student_expectation_empty(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": [" "], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "student_expectations should not be an empty string"

#====================================test 59=======================================


@pytest.mark.tc_059
def test_student_expectation_malformed(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["X.2(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid student expectations"

#======================================test 60==========================================


@pytest.mark.tc_060
def test_student_expectation_out_of_range_letteral(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.1(Z)"], \
        "difficulty": "easy", \
        "points": 2, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid student expectations"

#===================================test 61=================================================


@pytest.mark.tc_061
def test_student_expectation_out_of_range_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.25(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid student expectations"

#=====================================test 62=========================================


@pytest.mark.tc_062
def test_student_expectation_special_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["$.1(%)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid student expectations"

#==============================test 63=======================================


@pytest.mark.tc_063
def test_student_expectation_non_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["Linear"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid student expectations"

#===============================test 64=====================================


@pytest.mark.tc_064
def test_student_expectation_multiple_periods(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A...1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid student expectations"

#===============================test 65===================================


@pytest.mark.tc_065
def test_student_expectation_multiple_A(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["AAAA.1(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid student expectations"

#====================================test 66============================================


@pytest.mark.tc_066
def test_student_expectation_leading_zero(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.01(A)"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid student expectations"

#==================================test 67====================================


@pytest.mark.tc_067
def test_student_expectation_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": [1,2], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "student_expectations must be a string"

#================================test 68==========================================


@pytest.mark.tc_068
def test_student_expectation_in_string(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": "A.1(A)", \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "student_expectations must be a list"

#=================================test 69=======================================


@pytest.mark.tc_069
def test_student_expectation_missing_letters(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.1"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid student expectations"

#===================================test 70==========================================


@pytest.mark.tc_070
def test_student_expectation_missing_parenthesis(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.1A"], \
        "difficulty": "easy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid student expectations"

#====================================test 71====================================

@pytest.mark.tc_071
def test_difficulty_missing(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": , \
        "points": 2, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Invalid Payload"

#==================================test 72 ========================================


@pytest.mark.tc_072
def test_difficulty_empty(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": " ", \
        "points": 2, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "invalid difficulty level"

#====================================test 73=================================================


@pytest.mark.tc_073
def test_difficulty_invalid(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "Algebra I", \
        "points": 2, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "invalid difficulty level"

#================================test 74=============================================

@pytest.mark.tc_074
def test_difficulty_special_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "$$$$$$$$$", \
        "points": 2, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "invalid difficulty level"

#===========================test 75================================================


@pytest.mark.tc_075
def test_difficulty_spelling(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "Easssy", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "invalid difficulty level"

#==================================test 76=========================================


@pytest.mark.tc_076
def test_difficulty_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "12345", \
        "points": 2, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "invalid difficulty level"

#===============================test 77======================================


@pytest.mark.tc_077
def test_difficulty_white_spaces(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "  ea  s y", \
        "points": 2, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "invalid difficulty level"

#=========================================test 78================================


@pytest.mark.tc_078
def test_difficulty_incompatible_points_easy(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "easy", \
        "points": 5, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Difficulty level is incompatible with points assigned."

#===================================test 79================================

@pytest.mark.tc_079
def test_difficulty_incompatible_points_hard(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "hard", \
        "points": 1, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "Difficulty level is incompatible with points assigned."

#=========================================test 80=======================================


@pytest.mark.tc_080
def test_points_missing(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "hard", \
        "points": " ", \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "points must be an integer"

#===========================test 81===========================================


@pytest.mark.tc_081
def test_points_negative(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "hard", \
        "points": -2, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "invalid points value: should only be between 1 to 3"

#====================================test 82=======================================

@pytest.mark.tc_082
def test_points_non_integer(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": ["A.1(A)"], \
        "difficulty": "hard", \
        "points": 2.5, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "points must be an integer"

#=======================================================================================
@pytest.mark.tc_083
def test_student_expectation_dict_format(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"


    


    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 11, \
        "teks_code": "A.5", \
        "subject": "Algebra I", \
        "topic": "Equations", \
        "category": "5", \
        "keywords": ["Linear"], \
        "student_expectations": [{"A":"1"}], \
        "difficulty": "hard", \
        "points": 2.5, \
        "response_type": "Open Response Exact", \
        "question_content": "' + question1 + '", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "a", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + unit + '", \
            "is_answer": true \
            } \
        ] \
        }'}


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] ==   "student_expectations must be a string"



















