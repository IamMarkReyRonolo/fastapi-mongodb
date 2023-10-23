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
from lib.mw_sql import execute_query



@fixture(scope="module")
def get_admin_token():    
    token = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")


@pytest.mark.tc_001
def test_fetch_staar_question_history_by_uuid(get_admin_token):
    req: Requester = Requester()      
    sql_staar_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = 'STAAR' LIMIT 1")        
    headers: dict = req.create_basic_headers(token=get_admin_token)    
    sql_uuid: str = sql_staar_returned[0][0]
    url: str = f"{req.base_url}/question/fetch/history/{sql_uuid}"      
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['history'][0]['question_uuid']).is_equal_to(sql_uuid)
    assert_that(len(questions['history'])).is_greater_than(0)
    pass

@pytest.mark.tc_002
def test_fetch_staar_question_history_by_invalid_uuid(get_admin_token):
    req: Requester = Requester()      
    sql_staar_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = 'STAAR' LIMIT 1")        
    headers: dict = req.create_basic_headers(token=get_admin_token)    
    sql_uuid: str = sql_staar_returned[0][0] + "123"
    url: str = f"{req.base_url}/question/fetch/history/{sql_uuid}"          
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    json_response: dict = json.loads(response.text)    
    assert_that(json_response['detail']).is_equal_to("Invalid uuid")