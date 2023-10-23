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
def get_admin_token():
    token = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")

@pytest.mark.tc_001
def test_delete_staar(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    create_url = f"{req.base_url}/question/staar/create"

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
    # Create Question
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    create_response = requests.request("POST", create_url, headers=header, data=payload, files=upload_file)
    json_create_response: dict = json.loads(create_response.text)
    assert json_create_response['detail'] == "Successfully Added Question"

    # Delete Question
    question_uuid: str =  json_create_response['question_uuid']
    delete_url: str = f"{req.base_url}/question/delete/{question_uuid}"
    del_response = requests.request("DELETE", delete_url, headers=header)
    del_json_response: dict = json.loads(del_response.text)
    assert del_response.status_code == 200
    assert del_json_response['detail'] == "Successfully deleted"

    # Fetch Question
    fetch_url: str = f"{req.base_url}/question/fetch/{question_uuid}"
    fetch_response = requests.request("GET", fetch_url, headers=header)
    json_fetch_response: dict = json.loads(fetch_response.text)
    assert fetch_response.status_code == 404
    assert json_fetch_response['detail'] == "Question Not Found."

@pytest.mark.tc_002
def test_delete_invalid_staar_uuid(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    create_url = f"{req.base_url}/question/staar/create"

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
    # Create Question
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    create_response = requests.request("POST", create_url, headers=header, data=payload, files=upload_file)
    json_create_response: dict = json.loads(create_response.text)
    assert json_create_response['detail'] == "Successfully Added Question"

    # Delete Question Attempt
    invalid_question_uuid: str =  common.replace_numbers_with_zero(json_create_response['question_uuid'])
    delete_url: str = f"{req.base_url}/question/delete/{invalid_question_uuid}"
    del_response = requests.request("DELETE", delete_url, headers=header)
    del_json_response: dict = json.loads(del_response.text)
    assert del_response.status_code == 404
    assert del_json_response['detail'] == "Question Not Found."

    # Fetch Question
    fetch_url: str = f"{req.base_url}/question/fetch/{json_create_response['question_uuid']}"
    fetch_response = requests.request("GET", fetch_url, headers=header)
    json_fetch_response: dict = json.loads(fetch_response.text)
    assert fetch_response.status_code == 200
    assert common.is_valid_uuid(json_fetch_response['Question']['uuid']) == True

@pytest.mark.tc_003
def test_delete_mathworld(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/mathworld/create"
    question1: str = common.get_random_question()
    question2: str = common.get_random_question()
    teks_code: str = common.get_random_tek_code()
    unit: str = common.get_random_unit()

    header: dict = req.create_basic_headers(token=get_admin_token)
    create_url: str = f"{req.base_url}/question/mathworld/create"

    payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 3, \
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

    # Create Question
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    create_response: requests.models.Response = \
        requests.request("POST", create_url, headers=header, data=payload, files=upload_file)
    json_create_response: dict = json.loads(create_response.text)
    assert json_create_response['detail'] == "Successfully Added Question"

    # Delete Question
    question_uuid: str =  json_create_response['question_uuid']
    delete_url: str = f"{req.base_url}/question/delete/{question_uuid}"
    del_response: requests.models.Response = \
          requests.request("DELETE", delete_url, headers=header)
    del_json_response: dict = json.loads(del_response.text)
    assert del_response.status_code == 200
    assert del_json_response['detail'] == "Successfully deleted"

    # Fetch Question
    fetch_url: str = f"{req.base_url}/question/fetch/{question_uuid}"
    fetch_response = requests.request("GET", fetch_url, headers=header)
    json_fetch_response: dict = json.loads(fetch_response.text)
    assert fetch_response.status_code == 404
    assert json_fetch_response['detail'] == "Question Not Found."

@pytest.mark.tc_004
def test_delete_invalid_mathworld_uuid(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    create_url: str = f"{req.base_url}/question/staar/create"

    header: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/mathworld/create"
    question1: str = common.get_random_question()
    question2: str = common.get_random_question()
    teks_code: str = common.get_random_tek_code()
    unit: str = common.get_random_unit()

    header: dict = req.create_basic_headers(token=get_admin_token)
    create_url: str = f"{req.base_url}/question/mathworld/create"
    payload: dict = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 3, \
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

    # Create Question
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    create_response: requests.models.Response = \
        requests.request("POST", create_url, headers=header, data=payload, files=upload_file)
    json_create_response: dict = json.loads(create_response.text)
    assert json_create_response['detail'] == "Successfully Added Question"

    # Delete Question Attempt
    invalid_question_uuid: str =  common.replace_numbers_with_zero(json_create_response['question_uuid'])
    delete_url: str = f"{req.base_url}/question/delete/{invalid_question_uuid}"
    del_response: requests.models.Response = requests.request("DELETE", delete_url, headers=header)
    del_json_response: dict = json.loads(del_response.text)
    assert del_response.status_code == 404
    assert del_json_response['detail'] == "Question Not Found."

    # Fetch Question
    fetch_url: str = f"{req.base_url}/question/fetch/{json_create_response['question_uuid']}"
    fetch_response: requests.Response = requests.request("GET", fetch_url, headers=header)
    json_fetch_response: dict = json.loads(fetch_response.text)
    assert fetch_response.status_code == 200
    assert common.is_valid_uuid(json_fetch_response['Question']['uuid']) == True

@pytest.mark.tc_005
def test_delete_college(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    create_url = f"{req.base_url}/question/college/create"
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

    # Create Question
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    create_response = requests.request("POST", create_url, headers=header, data=payload, files=upload_file)
    json_create_response: dict = json.loads(create_response.text)
    assert json_create_response['detail'] == "Successfully Added Question"

    # Delete Question
    question_uuid: str =  json_create_response['question_uuid']
    delete_url: str = f"{req.base_url}/question/delete/{question_uuid}"
    del_response = requests.request("DELETE", delete_url, headers=header)
    del_json_response: dict = json.loads(del_response.text)
    assert del_response.status_code == 200
    assert del_json_response['detail'] == "Successfully deleted"

    # Fetch Question
    fetch_url: str = f"{req.base_url}/question/fetch/{question_uuid}"
    fetch_response = requests.request("GET", fetch_url, headers=header)
    json_fetch_response: dict = json.loads(fetch_response.text)
    assert fetch_response.status_code == 404
    assert json_fetch_response['detail'] == "Question Not Found."

@pytest.mark.tc_006
def test_delete_invalid_college_uuid(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    create_url: str = f"{req.base_url}/question/college/create"

    header: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/college/create"
    question1: str = common.get_random_question()
    question2: str = common.get_random_question()
    teks_code: str = common.get_random_tek_code()
    unit: str = common.get_random_unit()

    header: dict = req.create_basic_headers(token=get_admin_token)
    create_url: str = f"{req.base_url}/question/mathworld/create"
    payload: dict = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 3, \
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

    # Create Question
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    create_response: requests.models.Response = \
        requests.request("POST", create_url, headers=header, data=payload, files=upload_file)
    json_create_response: dict = json.loads(create_response.text)
    assert json_create_response['detail'] == "Successfully Added Question"

    # Delete Question Attempt
    invalid_question_uuid: str =  common.replace_numbers_with_zero(json_create_response['question_uuid'])
    delete_url: str = f"{req.base_url}/question/delete/{invalid_question_uuid}"
    del_response: requests.models.Response = requests.request("DELETE", delete_url, headers=header)
    del_json_response: dict = json.loads(del_response.text)
    assert del_response.status_code == 404
    assert del_json_response['detail'] == "Question Not Found."

    # Fetch Question
    fetch_url: str = f"{req.base_url}/question/fetch/{json_create_response['question_uuid']}"
    fetch_response: requests.Response = requests.request("GET", fetch_url, headers=header)
    json_fetch_response: dict = json.loads(fetch_response.text)
    assert fetch_response.status_code == 200
    assert common.is_valid_uuid(json_fetch_response['Question']['uuid']) == True

@pytest.mark.tc_007
def test_unauthorized_delete(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    create_url: str = f"{req.base_url}/question/college/create"

    header: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/college/create"
    question1: str = common.get_random_question()
    question2: str = common.get_random_question()
    teks_code: str = common.get_random_tek_code()
    unit: str = common.get_random_unit()

    header: dict = req.create_basic_headers(token=get_admin_token)
    create_url: str = f"{req.base_url}/question/mathworld/create"
    payload: dict = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 3, \
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

    # Create Question
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    create_response: requests.models.Response = \
        requests.request("POST", create_url, headers=header, data=payload, files=upload_file)
    json_create_response: dict = json.loads(create_response.text)
    assert json_create_response['detail'] == "Successfully Added Question"

    # Delete Question Attempt
    invalid_question_uuid: str =  common.replace_numbers_with_zero(json_create_response['question_uuid'])
    delete_url: str = f"{req.base_url}/question/delete/{invalid_question_uuid}"
    header.update( {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.2yJkYXRhIjoiaEFJN3JhU0ppR2htcGFCYW5HQUd1azUxMjk1bXdMcCtaTlZuV21xb1pvbERCK1BaZXFHTFMzTEdCTWdRYVJLR3QrOE9XVS95NDREdTNBRUtKeDU0emtic0VjRzN6UFhKN2U4ZllmZi9NY0NYRFMrZGJvdjJvL1V4NWlDVm9PV2NYQWZPemNvamgrUXBPL0JXMkJYeGZLMFR5ZzR3ZE13PSo2cEorTk9Kb3NYQ2lWMFR1Q3ZpNEJ3PT0qKzR5WWJUWGVQSHRHMkpPZGVyWHJOUT09Knl2VEhycGxHRmcvUDlTenE1OWpRZHc9PSJ9.eb2Tccc-65rXGn-O4bxq2_Sbr2iVwhR3rcCxIxVvAYI'})
    del_response: requests.models.Response = \
        requests.request("DELETE", delete_url, headers=header)
    del_json_response: dict = json.loads(del_response.text)
    assert del_response.status_code == 403
    assert del_json_response['detail'] == "Invalid token or expired token."
