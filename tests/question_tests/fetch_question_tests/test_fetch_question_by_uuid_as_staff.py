from pytest import fixture
import pdb, requests
import os, sys, json
from assertpy import assert_that
import re

CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)

import logging as logger, pytest
import lib.common as common
import lib.generate_token as generate_token
from lib.requester import Requester
from lib.mw_sql import execute_query

@fixture(scope="module")
def get_staff_token():
    print("\n---- Setup Test ----\n")
    token = generate_token.generate_token(email="staffABC@gmail.com", password="Staff123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")

@pytest.mark.tc_001  # stats = Pending
def test_question_fetch_by_uuid_status_pending(get_staff_token):
    req: Requester = Requester()    
    headers: dict = req.create_basic_headers(token=get_staff_token)
    question_status: str = "Pending"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}' LIMIT 1")
    sql_response_uuid: str = questions_returned[0][0]
    url: str = f"{req.base_url}/question/fetch/{sql_response_uuid}"    
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    question: dict = json.loads(response.text)
    assert question['Question']['uuid'] == questions_returned[0][0]
    

@pytest.mark.tc_002 # status = Rejected
def test_question_fetch_by_uuid_status_rejected(get_staff_token):
    req: Requester = Requester()    
    headers: dict = req.create_basic_headers(token=get_staff_token)
    question_status: str = "Rejected"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}' LIMIT 1")
    sql_response_uuid: str = questions_returned[0][0]
    url: str = f"{req.base_url}/question/fetch/{sql_response_uuid}"    
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    question: dict = json.loads(response.text)
    assert question['Question']['uuid'] == questions_returned[0][0]

@pytest.mark.tc_003  # status = Approved 
def test_question_fetch_by_uuid_status_approved(get_staff_token):
    req: Requester = Requester()    
    headers: dict = req.create_basic_headers(token=get_staff_token)
    question_status: str = "Approved"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}' LIMIT 1")
    sql_response_uuid: str = questions_returned[0][0]
    url: str = f"{req.base_url}/question/fetch/{sql_response_uuid}"    
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    question: dict = json.loads(response.text)
    assert question['Question']['uuid'] == questions_returned[0][0]

@pytest.mark.tc_004  # status = Approved 
def test_question_fetch_by_uuid_status_reported(get_staff_token):
    req: Requester = Requester()    
    headers: dict = req.create_basic_headers(token=get_staff_token)
    question_status: str = "Reported"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}' LIMIT 1")
    sql_response_uuid: str = questions_returned[0][0]
    url: str = f"{req.base_url}/question/fetch/{sql_response_uuid}"      
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    question: dict = json.loads(response.text)
    assert question['Question']['uuid'] == questions_returned[0][0]

@pytest.mark.tc_005  # invalid uuid format
def test_question_fetch_by_invalid_uuid_format(get_staff_token):
    req: Requester = Requester()    
    headers: dict = req.create_basic_headers(token=get_staff_token)
    question_status: str = "Reported"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}' LIMIT 1")
    sql_response_uuid: str = questions_returned[0][0] + "dd"
    url: str = f"{req.base_url}/question/fetch/{sql_response_uuid}"      
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 404
    question_response: dict = json.loads(response.text)
    assert_that(question_response['detail']).is_equal_to('Question Not Found.')

@pytest.mark.tc_006  # invalid uuid data
def test_question_fetch_by_invalid_uuid_data(get_staff_token):
    req: Requester = Requester()    
    headers: dict = req.create_basic_headers(token=get_staff_token)
    question_status: str = "Reported"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}' LIMIT 1")
    sql_response_uuid: str = re.sub(r'\d+', 'z', questions_returned[0][0])
    url: str = f"{req.base_url}/question/fetch/{sql_response_uuid}"      
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 404
    question_response: dict = json.loads(response.text)
    assert_that(question_response['detail']).is_equal_to('Question Not Found.')

@pytest.mark.tc_007 # invalid token 
def test_question_fetch_by_uuid_invalid_token(get_staff_token):
    req: Requester = Requester()    
    invalid_token: str = re.sub(r"\d+", "zz", get_staff_token)
    headers: dict = req.create_basic_headers(token=invalid_token)
    question_status: str = "Reported"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}' LIMIT 1")
    sql_response_uuid: str = questions_returned[0][0]
    url: str = f"{req.base_url}/question/fetch/{sql_response_uuid}"      
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 403
    question_response: dict = json.loads(response.text)
    assert_that(question_response['detail']).is_equal_to('Invalid token or expired token.')
    