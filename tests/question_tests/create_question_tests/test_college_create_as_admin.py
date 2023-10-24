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
from payloads.college_question_payloads import get_valid_successful_college_payload

print("\n---- Setup Test ----\n")
@fixture(scope="module")
def get_admin_token():
    token = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")

@pytest.mark.tc_001
def test_successful_request(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"

@pytest.mark.tc_004
def test_question_type_eq_Blank(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['question_type'] = '' # make the question type blank

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question_type is required"

@pytest.mark.tc_005
def test_question_type_college_level_with_whitespace(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['question_type'] = "College Level  " # add trailing white spaces

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"

@pytest.mark.tc_006
def test_question_type_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload['question_type'] = "2" # make the question type numeric
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid question type"

@pytest.mark.tc_007
def test_question_type_special_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    

    payload = get_valid_successful_college_payload()
    payload['question_type'] = "@@@@"

    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid question type"

@pytest.mark.tc_008
def test_classification_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    

    payload = get_valid_successful_college_payload()
    payload['classification'] = "2"

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_009
def test_classification_type_blank_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload['classification'] = ''

    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "classification is required"

@pytest.mark.tc_010
def test_classification_type_TSI(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['classification'] = 'TSI'

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"

@pytest.mark.tc_011
def test_classification_type_ACT(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['classification'] = 'ACT'

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"

@pytest.mark.tc_012
def test_classification_type_ACT_with_whitespace(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload['classification'] = 'ACT '

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"

@pytest.mark.tc_013
def test_classification_type_invalid_special_symbol(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload['classification'] = "@@@"

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400

@pytest.mark.tc_014
def test_classification_blank(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload['classification'] = ""

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "classification is required"

@pytest.mark.tc_015
def test_classification_eq_neg_5(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['classification'] = "-5"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_016
def test_classification_eq_neg_15(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload['classification'] = "-15"

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_017
def test_classification_invalid_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['classification'] = "!"

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_018
def test_add_2_types_of_classifications(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload['classification'] = "SAT ACT"

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_019
def test_add_2_SAT_with_whitespace(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload['classification'] = "SAT  "

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"
    

@pytest.mark.tc_020
def test_add_2_TSI_with_whitespace(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['classification'] = "TSI  "
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"

@pytest.mark.tc_021
def test_add_2_ACT_with_whitespace(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['classification'] = "ACT  "
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"

@pytest.mark.tc_022
def test_classification_malformed(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['classification'] = "0000000"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_023
def test_classification_type_college_level(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['classification'] = "college level"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_024
def test_classification_type_STAAR(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['classification'] = "STAAR"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_025
def test_classification_type_Mathworld(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['classification'] = "Mathworld"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid classification type"

@pytest.mark.tc_026
def test_test_code_whitespace(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload['test_code'] = "123456 "

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "test code must not exceed 6 characters"

@pytest.mark.tc_027
def test_test_code_neg_123456(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['test_code'] = "-123456"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "test code must not exceed 6 characters"

@pytest.mark.tc_028
def test_test_code_special_char(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['test_code'] = "@@@"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"


@pytest.mark.tc_029
def test_test_code_type_a(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['test_code'] = "abc"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"



@pytest.mark.tc_030
def test_test_code_type_alpha_numeric(get_admin_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['test_code'] = "a1"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"



@pytest.mark.tc_031
def test_test_code_type_blank(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['test_code'] = ""

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "test_code is required"


@pytest.mark.tc_032
def test_test_code_str_0(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['test_code'] = "0"

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"



@pytest.mark.tc_033
def test_test_code_type_neg_5(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload['test_code'] = -5

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "test code must be a string"



@pytest.mark.tc_036
def test_keywords_str_55(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['keywords'] = ["55"]

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"




@pytest.mark.tc_037
def test_keywords_str_neg_123(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['keywords'] = ["-123"]

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"



@pytest.mark.tc_038
def test_keywords_str_abc(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['keywords'] = ["abc"]

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"

    
@pytest.mark.tc_039
def test_keywords_list_strings(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload['keywords'] = ["mabra", "science", "english", "writing", "reading"]
        
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"


@pytest.mark.tc_040
def test_keywords_list_alpha_num(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload['keywords'] = ["math","algebra", "science",3, "english", "writing", "reading", 5]
        
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "all values in keywords must be string"


@pytest.mark.tc_041
def test_keywords_empty_list(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['keywords'] = []

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "keywords must not be empty"


@pytest.mark.tc_042
def test_keywords_missing(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    del payload["keywords"] 
        
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "keywords is required"

@pytest.mark.tc_043
def test_keywords_all_num(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload['keywords'] = [3,1,3,2,1]
        
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "all values in keywords must be string"


@pytest.mark.tc_044
def test_keywords_blank_entry(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['keywords'] = ["math", "science", "english", "", "algegra", "geometry"]
        
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "a value in keywords should not be an empty string"


@pytest.mark.tc_045
def test_keywords_long_value(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['keywords'] = ["math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra_math_algebra",]
        
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"

@pytest.mark.tc_046
def test_keywords_list_60_value(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload['keywords'] = ["Math","Math","Math","Math","Math","Math",
        "Math","Math","Math","Math","Math","Math","Math","Math",
        "Math","Math","Math","Math","Math","Math","Math","Math",
        "Math","Math","Math","Math","Math","Math","Math","Math",
        "Math","Math","Math","Math","Math","Math","Math","Math",
        "Math","Math","Math","Math","Math","Math","Math","Math",
        "Math","Math","Math","Math","Math","Math","Math","Math",
        "Math","Math","Math","Math","Math","Math"]
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"


@pytest.mark.tc_047
def test_response_type_blank(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload["response_type"] = ""
        
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "response_type is required"


@pytest.mark.tc_048
def test_response_type_blank_char(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload["response_type"] = " "

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "response_type should not be an empty string"


@pytest.mark.tc_049
def test_response_type_not_ore(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload["response_type"] = "Open Response"
        
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"

@pytest.mark.tc_050
def test_response_type_is_ore(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload["response_type"] = "Open Response Exact"
        
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"


@pytest.mark.tc_051
def test_response_type_is_ror(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload["response_type"] = "Range Open Response"
        
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"




@pytest.mark.tc_052
def test_response_type_not_ror(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload["response_type"] = "Range Open"

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"


@pytest.mark.tc_053
def test_response_type_mc(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload["response_type"] = "Multiple Choice"
        
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"


@pytest.mark.tc_054
def test_response_type_not_mc(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload["response_type"] = "Multiple"

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"


@pytest.mark.tc_055
def test_response_type_cb(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload["response_type"] = "Checkbox"
        
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"


@pytest.mark.tc_056
def test_response_type_not_cb(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload["response_type"] = "Check box"

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"


@pytest.mark.tc_057
def test_response_type_numeric(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload["response_type"] = "123"

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"


@pytest.mark.tc_058
def test_response_type_spec_char(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload["response_type"] = "$$##@@"

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "invalid response type"


@pytest.mark.tc_059
def test_question_content(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload["question_content"] = "this is a test"
    
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"


@pytest.mark.tc_060
def test_question_content_blank(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
        
    payload = get_valid_successful_college_payload()
    payload["question_content"] = ""


    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question_content is required"


@pytest.mark.tc_061
def test_question_content_missing(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    del payload["question_content"]

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question_content is required"


@pytest.mark.tc_062
def test_question_content_lines_10(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload["question_content"] = "This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit \
               This is a long string to provide a paragraph just to test if qustion content has a limit"
        
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question content should not exceed 1000 characters"


@pytest.mark.tc_063
def test_question_content_1000_char(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    char_limit: str = common.get_random_char(1000)
    payload = get_valid_successful_college_payload()
    payload["question_content"] = char_limit

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"


@pytest.mark.tc_064
def test_question_content_999_char(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    char_limit: str = common.get_random_char(999)
    payload = get_valid_successful_college_payload()
    payload["question_content"] = char_limit

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"


@pytest.mark.tc_065
def test_question_content_1001_char(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    char_limit: str = common.get_random_char(1001)
    payload = get_valid_successful_college_payload()
    payload["question_content"] = char_limit

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question content should not exceed 1000 characters"


@pytest.mark.tc_066
def test_question_content_blank_chars(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload["question_content"] = "     "
        
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question content should not be empty"


@pytest.mark.tc_067
def test_question_content_content_numeric(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()
    payload["question_content"] = 3

    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    assert json_response['detail'] == "question content must be a string"


@pytest.mark.tc_068
def test_question_content_spec_char(get_admin_token):    
    req = Requester()
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()
    payload["question_content"] = ")($@#@#)()"
        
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response['detail'] == "Successfully Added Question"



    
