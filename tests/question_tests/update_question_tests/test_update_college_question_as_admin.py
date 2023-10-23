from pytest import fixture
import pdb, requests
import os, sys, json
from faker import Faker
import random
from assertpy import assert_that
import uuid
import time

CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)

import logging as logger, pytest
import lib.common as common
from lib.common import get_random_question
import lib.generate_token as generate_token
from lib.requester import Requester
from lib.mw_sql import execute_query

faker = Faker()


@fixture(scope="module")
def get_admin_token():    
    token = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")


@pytest.mark.tc_001
def test_update_college_question(get_admin_token):
    req: Requester = Requester()      
    random_data: dict = common.get_random_payload_data()    
    college_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = 'College Level' LIMIT 1")          
    sql_classic_uuid: str = college_classic[0][0]
    sql_classic_question_type: str = college_classic[0][4]    
    sql_classic_response_type: str = college_classic[0][5]
    sql_classic_question: str = college_classic[0][6]    
    sql_classic_status: str = college_classic[0][8]
    random_payload = {'data': '{ "question_type": "College Level", "classification": "' + random_data['random_classification'] + '", "update_note": "' + random_data['random_question_content'] + '", "test_code": "123456", "keywords": ["' + random_data['random_topic'] + '"], "response_type": "' + random_data['random_response_type'] + '", "question_content": "' + random_data['random_question_content'] + '", "question_img": "","options": [{"letter": "' + random_data['random_letter'] + '","content": "' + random_data['random_question_content'] + '","image": "","unit": "' + random_data['random_unit'] + '","is_answer": true}]}'} 
    header: dict = req.create_basic_headers(token=get_admin_token) 
    
    url: str = f"{req.base_url}/question/update/college/{sql_classic_uuid}" 
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}\\tests\\images", "image_01.jpg")     
    time.sleep(1)      
    response = requests.request("PUT", url, headers=header, data=random_payload, files=upload_file)  
    updated_response: dict = json.loads(response.text)  
    assert_that(response.status_code).is_equal_to(200)
    assert_that(updated_response['detail']).is_equal_to("Successfully updated")    
    assert_that(updated_response['question_uuid']).is_equal_to(sql_classic_uuid)
    sql_college_updated: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{sql_classic_uuid}'")  
    sql_updated_uuid: str = sql_college_updated[0][0]
    sql_updated_question_type: str = sql_college_updated[0][4]    
    sql_updated_response_type: str = sql_college_updated[0][5]
    sql_updated_question: str = sql_college_updated[0][6]
    sql_updated_status: str = sql_college_updated[0][8]

    assert_that(sql_updated_uuid).is_equal_to(sql_classic_uuid)
    assert_that(sql_updated_question_type).is_equal_to(sql_classic_question_type)
    assert_that(sql_updated_response_type).is_equal_to(random_data['random_response_type'])
    assert_that(sql_updated_question).is_not_equal_to(sql_classic_question)
    assert_that(sql_updated_status).is_equal_to(sql_classic_status)


@pytest.mark.tc_002
def test_update_college_question_invalid_uuid(get_admin_token):
    req: Requester = Requester()      
    random_data: dict = common.get_random_payload_data()    
    college_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = 'College Level' LIMIT 1")          
    sql_classic_invalid_uuid: str = college_classic[0][0]+ "123"    
    random_payload = {'data': '{ "question_type": "College Level", \
                      "classification": "' + random_data['random_classification'] + '", \
                      "update_note": "' + random_data['random_question_content'] + '", \
                      "test_code": "123456", \
                      "keywords": ["' + random_data['random_topic'] + '"], \
                      "response_type": "' + random_data['random_response_type'] + '", \
                      "question_content": "' + random_data['random_question_content'] + '", \
                      "question_img": "",\
                      "options": [{"letter": "' + random_data['random_letter'] + '",\
                        "content": "' + random_data['random_question_content'] + '", \
                        "image": "", \
                        "unit": "' + random_data['random_unit'] + '", \
                        "is_answer": true}]}'}

    header: dict = req.create_basic_headers(token=get_admin_token) 
    
    url: str = f"{req.base_url}/question/update/college/{sql_classic_invalid_uuid}" 
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}\\tests\\images", "image_01.jpg")           
    response = requests.request("PUT", url, headers=header, data=random_payload, files=upload_file)  
    updated_response: dict = json.loads(response.text)  
    time.sleep(1)
    assert_that(response.status_code).is_equal_to(400)
    assert_that(updated_response['detail']).is_equal_to("Invalid uuid")        