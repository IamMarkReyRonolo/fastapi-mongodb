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
from payloads.valid_question_payloads import get_valid_successful_staar_payload


@fixture(scope="module")
def get_admin_token():
    token = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")

@pytest.mark.tc_001
def test_all_fields(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()

    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    


@pytest.mark.tc_002
def test_blank_question_type(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['question_type'] = ""

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question_type is required"


@pytest.mark.tc_005
def test_question_type_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['question_type'] = "1"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid question type"


@pytest.mark.tc_007
def test_grade_level_eq_0(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['grade_level'] = 0


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid grade level: should only be between 3 to 12"

@pytest.mark.tc_008
def test_grade_level_eq_13(get_admin_token):
  req = Requester()
  header: dict = req.create_basic_headers(token=get_admin_token)
  url = f"{req.base_url}/v1/questions/create"

  payload = get_valid_successful_staar_payload()
  payload['grade_level'] = 13

    
  response = requests.request("POST", url, headers=header, json=payload)
  json_response = json.loads(response.text)
  assert response.status_code == 400
  assert json_response['detail'] == "invalid grade level: should only be between 3 to 12"

@pytest.mark.tc_009
def test_grade_level_eq_12(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['grade_level'] = 12
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    

@pytest.mark.tc_010
def test_grade_level_eq_neg_3(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['grade_level'] = -3
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid grade level: should only be between 3 to 12"

@pytest.mark.tc_011
def test_grade_level_eq_neg_12(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['grade_level'] = -12
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid grade level: should only be between 3 to 12"


@pytest.mark.tc_012
def test_grade_level_eq_neg_13(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['grade_level'] = -13
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid grade level: should only be between 3 to 12"

@pytest.mark.tc_013
def test_grade_level_eq_neg_0(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['grade_level'] = -0
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid grade level: should only be between 3 to 12"

@pytest.mark.tc_014
def test_grade_level_str_3(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['grade_level'] = "3"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "grade level must be an integer"

@pytest.mark.tc_015
def test_grade_level_str_12(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['grade_level'] = "12"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "grade level must be an integer"

@pytest.mark.tc_016
def test_grade_level_blank(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    del payload['grade_level']
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "grade_level is required"

@pytest.mark.tc_020
def test_grade_level_eq_1(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['grade_level'] = 1
    
    response = requests.request("POST", url, headers=header, json=payload)
    assert response.status_code == 400
    assert response.text == '{"detail":"invalid grade level: should only be between 3 to 12"}'

@pytest.mark.tc_021
def test_grade_level_special_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['grade_level'] = '@'
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'grade level must be an integer'

@pytest.mark.tc_022
def test_grade_level_blank_str(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['grade_level'] = ''
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "grade_level is required"

@pytest.mark.tc_023
def test_release_date_current(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_current_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['release_date'] = f"{f'{yyyy_mm}'}"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    


@pytest.mark.tc_024
def test_release_date_future(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_future_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['release_date'] = f"{f'{yyyy_mm}'}"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    

@pytest.mark.tc_025
def test_release_date_past(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['release_date'] = f"{f'{yyyy_mm}'}"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    


@pytest.mark.tc_025
def test_release_date_mm_yyyy(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['release_date'] = "03-2024"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid format: format accepted xxxx-xx | year-month"

@pytest.mark.tc_026
def test_release_date_mmyyyy(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['release_date'] = "032024"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid format: format accepted xxxx-xx | year-month"

@pytest.mark.tc_027
def test_release_date_mm_bs_yyyy(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['release_date'] = "03/2024"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid format: format accepted xxxx-xx | year-month"


@pytest.mark.tc_028
def test_release_date_yyyy_bs_mm(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['release_date'] = "2023\03"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid format: format accepted xxxx-xx | year-month"

@pytest.mark.tc_029
def test_release_date_blank(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['release_date'] = ""
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "release_date is required"


@pytest.mark.tc_030
def test_release_date_invalid_month(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['release_date'] = "2024-15"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid - date should not be in future"

@pytest.mark.tc_031
def test_release_date_leap_year(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['release_date'] = "2024-02"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    

@pytest.mark.tc_032
def test_release_date_leap_year_with_day(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['release_date'] = "2024-31-02"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid format: format accepted xxxx-xx | year-month"


@pytest.mark.tc_033
def test_release_date_invalid_leap_year(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['release_date'] = "2023-31-02"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid format: format accepted xxxx-xx | year-month"

@pytest.mark.tc_034
def test_release_date_blank_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['release_date'] = "   "
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "release date should not be empty"

@pytest.mark.tc_035
def test_release_date_malformed(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['release_date'] = "00000000000"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid format: format accepted xxxx-xx | year-month"


@pytest.mark.tc_036
def test_release_date_missing(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    
    payload = get_valid_successful_staar_payload()
    del payload['release_date']
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "release_date is required"

@pytest.mark.tc_037
def test_release_date_us_format(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['release_date'] = '03-12-2024'
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "release date invalid format: format accepted xxxx-xx | year-month"

@pytest.mark.tc_038
def test_question_type_missing(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    del payload['question_type']
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question_type is required"

@pytest.mark.tc_039
def test_grade_level_missing(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    del payload['grade_level']

    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "grade_level is required"


@pytest.mark.tc_040
def test_release_date_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['release_date'] = 202403
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "release date must be a string"

# category
@pytest.mark.tc_041
def test_category_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['category'] = 1
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "category must be a string"


@pytest.mark.tc_042
def test_category_numeric_string(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['category'] = "1"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    


@pytest.mark.tc_043
def test_category_missing(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    del payload['category']
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "category is required"

@pytest.mark.tc_044
def test_category_eq_math(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['category'] = "math"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Valid category is from 1 to 5"



@pytest.mark.tc_045
def test_category_eq_science(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['category'] = "science"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Valid category is from 1 to 5"



@pytest.mark.tc_045
def test_category_eq_english(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['category'] = "english"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Valid category is from 1 to 5"


@pytest.mark.tc_045
def test_category_eq_blank(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['category'] = ""
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "category is required"


@pytest.mark.tc_046
def test_category_eq_blank_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['category'] = "  "
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "category should not be empty"


@pytest.mark.tc_047
def test_category_eq_special_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['category'] = "!@#$%^*(*(*))"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Valid category is from 1 to 5"



@pytest.mark.tc_048
def test_category_eq_neg_num(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['category'] = "-13232"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Valid category is from 1 to 5"



@pytest.mark.tc_049
def test_keywords_list_strings(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['keywords'] = ["math","algebra", "science", "english", "writing", "reading"]
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    


@pytest.mark.tc_050
def test_keywords_list_alpha_num(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['keywords'] = ["math","algebra", "science",3, "english", "writing", "reading", 5]
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "all values in keywords must be string"


@pytest.mark.tc_051
def test_keywords_list_special_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['keywords'] = ["math","algebra", "science","@@", "english", "writing", "reading", "#@#@"]
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    


@pytest.mark.tc_052
def test_keywords_empty_list(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['keywords'] = []
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "keywords must not be empty"


@pytest.mark.tc_053
def test_keywords_missing(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    del payload['keywords']
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "keywords is required"


@pytest.mark.tc_054
def test_keywords_all_num(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['keywords'] = [3, 1, 5, 4, 8, 9]
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "all values in keywords must be string"


@pytest.mark.tc_055
def test_keywords_blank_entry(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['keywords'] = ["math", "science", "english", "", "algegra", "geometry"]
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "a value in keywords should not be an empty string"


@pytest.mark.tc_056
def test_keywords_long_value(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['keywords'] = ["math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra",]
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Max length of keyword reached"


@pytest.mark.tc_057
def test_keywords_list_50_value(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['keywords'] = ["Math","Math","Math","Math","Math","Math",
        "Math","Math","Math","Math","Math","Math","Math","Math",
        "Math","Math","Math","Math","Math","Math","Math","Math",
        "Math","Math","Math","Math","Math","Math","Math","Math",
        "Math","Math","Math","Math","Math","Math","Math","Math",
        "Math","Math","Math","Math","Math","Math","Math","Math",
        "Math","Math","Math","Math",]
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Max number of keywords reached"


@pytest.mark.tc_058
def test_student_expectations_num_str(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['student_expectations'] = ["A.1(A)"]
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    


@pytest.mark.tc_059
def test_student_expectations_special_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['student_expectations'] = ["@"]
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Invalid student expectations"



@pytest.mark.tc_060
def test_student_expectations_list_str_num(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['student_expectations'] = ["31", "2.1", "3.3"]
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Invalid student expectations"


@pytest.mark.tc_061
def test_student_expectations_list_num_num(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['student_expectations'] = [31, 2.1]
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "student_expectations must be a string"


@pytest.mark.tc_062
def test_student_expectations_list_str_spec_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['student_expectations'] = ["31", '@']
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "Invalid student expectations"


@pytest.mark.tc_063
def test_student_expectations_list_num_str(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['student_expectations'] = [31, "2.1"]
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "student_expectations must be a string"


@pytest.mark.tc_064
def test_student_expectations_list_empty(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['student_expectations'] = []
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "student_expectations must not be empty"


@pytest.mark.tc_065
def test_student_expectations_list_missing(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    del payload['student_expectations']
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "student_expectations is required"


@pytest.mark.tc_066
def test_student_expectations_list_blank_strs(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['student_expectations'] = ["", "", ""]
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "student_expectations should not be an empty string"

@pytest.mark.tc_067
def test_response_type_blank(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['response_type'] = ""
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "response_type is required"


@pytest.mark.tc_068
def test_response_type_blank_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['response_type'] = "  "
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "response_type should not be an empty string"

@pytest.mark.tc_069
def test_response_type_missing(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    del payload['response_type']
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "response_type is required"

@pytest.mark.tc_070
def test_response_type_not_ore(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['response_type'] = "Open Response"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"

@pytest.mark.tc_070
def test_response_type_is_ore(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['response_type'] = "Open Response Exact"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    


@pytest.mark.tc_071
def test_response_type_is_ror(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['response_type'] = "Range Open Response"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    

@pytest.mark.tc_072
def test_response_type_not_ror(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['response_type'] = "Range Open"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"

@pytest.mark.tc_073
def test_response_type__mc(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['response_type'] = "Multiple Choice"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    


@pytest.mark.tc_073
def test_response_type__not_mc(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['response_type'] = "Multiple"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"

@pytest.mark.tc_074
def test_response_type_cb(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['response_type'] = "Checkbox"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    

@pytest.mark.tc_075
def test_response_type_not_cb(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['response_type'] = "Check box"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"

@pytest.mark.tc_076
def test_response_type_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['response_type'] = 1
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "response_type must be a string"

@pytest.mark.tc_077
def test_response_type_spec_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['response_type'] = "@@@@@"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"

@pytest.mark.tc_078
def test_question_content(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['question_content'] = "this is a test"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    

@pytest.mark.tc_079
def test_question_content_blank(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['question_content'] = ""
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question_content is required"

@pytest.mark.tc_080
def test_question_content_missing(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    del payload['question_content']
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question_content is required"

@pytest.mark.tc_081
def test_question_content_lines_10(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())

    payload = get_valid_successful_staar_payload()
    payload['question_content'] = """This is a long string to provide a paragraph just to test if question content has a limit \
               This is a long string to provide a paragraph just to test if question content has a limit 
               This is a long string to provide a paragraph just to test if question content has a limit 
               This is a long string to provide a paragraph just to test if question content has a limit 
               This is a long string to provide a paragraph just to test if question content has a limit 
               This is a long string to provide a paragraph just to test if question content has a limit 
               This is a long string to provide a paragraph just to test if question content has a limit 
               This is a long string to provide a paragraph just to test if question content has a limit 
               This is a long string to provide a paragraph just to test if question content has a limit 
               This is a long string to provide a paragraph just to test if question content has a limit"""
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'question content should not exceed 1000 characters'


@pytest.mark.tc_081
def test_question_content_1000_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1000)
    payload = get_valid_successful_staar_payload()
    payload['question_content'] = f"{f'{char_limit}'}"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    

@pytest.mark.tc_082
def test_question_content_999_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(999)
    payload = get_valid_successful_staar_payload()
    payload['question_content'] = f"{f'{char_limit}'}"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    


@pytest.mark.tc_083
def test_question_content_1001_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    payload = get_valid_successful_staar_payload()
    payload['question_content'] = f"{f'{char_limit}'}"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question content should not exceed 1000 characters"

@pytest.mark.tc_084
def test_question_content_blank_chars(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    
    payload = get_valid_successful_staar_payload()
    payload['question_content'] = "   "
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'question content should not be empty'

@pytest.mark.tc_085
def test_question_content_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    
    payload = get_valid_successful_staar_payload()
    payload['question_content'] = 5
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'question content must be a string'

@pytest.mark.tc_086
def test_question_content_spec_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    payload = get_valid_successful_staar_payload()
    payload['question_content'] = "!#$!@#$@#f"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    

@pytest.mark.tc_087
def test_question_img(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    question_img: str = f"{CURRENT_DIR}\\tests\\images\\image_01.jpg"
    
    payload = get_valid_successful_staar_payload()
    payload['question_img'] = f"{f'{question_img}'}"
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'invalid image insertion: image must be added through the Form, not in payload.'

@pytest.mark.tc_088
def test_question_img_missing(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    question_img: str = f"{CURRENT_DIR}\\tests\\images\\image_01.jpg"
    
    payload = get_valid_successful_staar_payload()
    del payload['question_img']
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'question_img is required'


@pytest.mark.tc_089
def test_question_img_blank_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    question_img: str = f"{CURRENT_DIR}\\tests\\images\\image_01.jpg"
    
    payload = get_valid_successful_staar_payload()
    payload['question_img'] = "   "
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'invalid image insertion: image must be added through the Form, not in payload.'


@pytest.mark.tc_090
def test_question_img_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    question_img: str = f"{CURRENT_DIR}\\tests\\images\\image_01.jpg"
    payload = get_valid_successful_staar_payload()
    payload['question_img'] = 1
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'image must be a string'


@pytest.mark.tc_091
def test_options_single(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    question_img: str = f"{CURRENT_DIR}\\tests\\images\\image_01.jpg"
    payload = get_valid_successful_staar_payload()
    payload['options'] = [ 
        { 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        } 
      ] 
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    

@pytest.mark.tc_092
def test_options_group_10(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    question_img: str = f"{CURRENT_DIR}\\tests\\images\\image_01.jpg"
    payload = get_valid_successful_staar_payload()
    payload['options'] = [ 
        { 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, 
        { 
          "letter": "b", 
          "content": "option b", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": False 
        }, 
        { 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, 
         { 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, 
        { 
          "letter": "b", 
          "content": "option b", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": False 
        }, 
        { 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, 
        { 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, 
        { 
          "letter": "b", 
          "content": "option b", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, 
        { 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, 
         { 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, 
        { 
          "letter": "b", 
          "content": "option b", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, 
        { 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        } 
      ]
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    

@pytest.mark.tc_093
def test_options_group_60(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    yyyy_mm: str = str(common.get_past_yyyy_mm())
    char_limit: str = common.get_random_char(1001)
    question_img: str = f"{CURRENT_DIR}\\tests\\images\\image_01.jpg"
    
    payload = get_valid_successful_staar_payload()
    payload['options'] = [{ 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, { 
          "letter": "b", 
          "content": "option b", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": False 
        }] * 30
    
    response = requests.request(
        "POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    

@pytest.mark.tc_094
def test_options_letter_blank(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['options'] = [{ 
          "letter": "", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, { 
          "letter": "b", 
          "content": "option b", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": False 
        }]
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'letter is required'


@pytest.mark.tc_095
def test_options_content_blank(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['options'] = [{ 
          "letter": "a", 
          "content": "", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, { 
          "letter": "b", 
          "content": "", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": False 
        }]
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'content is required'

@pytest.mark.tc_096
def test_options_image_blank(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['options'] = [{ 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, { 
          "letter": "b", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": False 
        }]

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    

@pytest.mark.tc_097
def test_options_unit_blank(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['options'] = [{ 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "", 
          "is_answer": True 
        }, { 
          "letter": "b", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": False 
        }]
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    

@pytest.mark.tc_098
def test_options_is_answer_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['options'] = [{ 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, { 
          "letter": "b", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": 1 
        }]
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'is_answer should be type boolean'


@pytest.mark.tc_098
def test_options_is_answer_blank_str(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['options'] = [{ 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": "" 
        }, { 
          "letter": "b", 
          "content": "option b", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": "" 
        }]
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'is_answer is required'


@pytest.mark.tc_099
def test_options_is_answer_true(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['options'] = [{ 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, { 
          "letter": "b", 
          "content": "option b", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True
        }]

    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    

@pytest.mark.tc_100
def test_options_is_answer_false(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['options'] = [{ 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": False 
        }, { 
          "letter": "b", 
          "content": "option b", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": False
        }]

    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    

@pytest.mark.tc_101
def test_options_is_answer_both_missing(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['options'] = [{ 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds"
        }, { 
          "letter": "b", 
          "content": "option b", 
          "image": "", 
          "unit": "pounds"
        }]

    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'is_answer is required in option object'


@pytest.mark.tc_102
def test_options_is_answer_single_missing(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['options'] = [{ 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": False
        }, { 
          "letter": "b", 
          "content": "option b", 
          "image": "", 
          "unit": "pounds"
        }]

    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'is_answer is required in option object'


@pytest.mark.tc_103
def test_options_unit_missing(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['options'] = [{ 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "is_answer": False
        }, { 
          "letter": "b", 
          "content": "option b", 
          "image": "", 
          "is_answer": False
        }]
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == 'unit is required'

@pytest.mark.tc_104
def test_options_content_1000_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    payload['options'] = [{ 
          "letter": "a", 
          "content": f"{common.get_random_char(1000)}", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, { 
          "letter": "b", 
          "content": f"{common.get_random_char(1000)}", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True
        }]
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    
@pytest.mark.tc_107
def test_options_is_answer_True(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_staar_payload()
    payload['options'] = [{ 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True}]
    

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == 'Successfully Added Question'

@pytest.mark.tc_108
def test_options_is_answer_False(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    

    payload = get_valid_successful_staar_payload()
    payload['options'] = [{ 
          "letter": "a", 
          "content": "this is a test", 
          "image": "", 
          "unit": "pounds", 
          "is_answer": False}]

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == 'Successfully Added Question'