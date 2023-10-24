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
def test_update_staar_question(get_admin_token):
    req: Requester = Requester()
    random_data: dict = common.get_staar_random_payload_data()
    json_random_data: str = json.dumps(random_data)
    staar_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = 'STAAR' LIMIT 1")
    sql_classic_uuid: str = staar_classic[0][0]
    sql_classic_question_type: str = staar_classic[0][4]
    sql_classic_question: str = staar_classic[0][6]
    sql_classic_status: str = staar_classic[0][8]

    payload = {'data': '{"question_type": "STAAR", "update_note": "'+ random_data['random_question_content'] +'", "grade_level": 3, "release_date": "2023-05", "category": "' + random_data['random_category'] + '","keywords": ["math"], "student_expectations": ["'+ random_data['random_student_expectation'] +'"],"response_type": "'+ random_data['random_response_type'] +'","question_content": "'+ random_data['random_question_content'] + '","question_img": "","options": [{"letter": "' + random_data['random_letter'] + '","content": "'+ random_data['random_question_content'] +'","image": "","unit": "pounds","is_answer": true},{"letter": "' + random_data['random_letter'] + '","content": "option b","image": "","unit": "pounds","is_answer": false}]}'}

    header: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/update/staar/{sql_classic_uuid}"
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}\\tests\\images", "image_01.jpg")
    # time.sleep(1)
    response = requests.request("PUT", url, headers=header, data=payload, files=upload_file)
    questions: dict = json.loads(response.text)
    time.sleep(1)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(questions['detail']).is_equal_to("Successfully updated")
    assert_that(questions['question_uuid']).is_equal_to(sql_classic_uuid)
    sql_staar_updated: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{sql_classic_uuid}'")
    sql_updated_uuid: str = sql_staar_updated[0][0]
    sql_updated_question_type: str = sql_staar_updated[0][4]
    sql_updated_response_type: str = sql_staar_updated[0][5]
    sql_updated_question: str = sql_staar_updated[0][6]
    sql_updated_status: str = sql_staar_updated[0][8]

    # time.sleep(1)
    assert_that(sql_updated_uuid).is_equal_to(sql_classic_uuid)
    assert_that(sql_updated_question_type).is_equal_to(sql_classic_question_type)
    assert_that(sql_updated_response_type).is_equal_to(random_data['random_response_type'])
    assert_that(sql_updated_question).is_not_equal_to(sql_classic_question)
    assert_that(sql_updated_status).is_equal_to(sql_classic_status)

@pytest.mark.tc_002
def test_update_staar_question_invalid_uuid(get_admin_token):
    req: Requester = Requester()
    random_data: dict = common.get_staar_random_payload_data()
    json_random_data: str = json.dumps(random_data)
    staar_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = 'STAAR' LIMIT 1")
    sql_classic_invalid_uuid: str = staar_classic[0][0]  + "XYZ"

    payload = {'data': '{"question_type": "STAAR", "update_note": "'+ random_data['random_question_content'] +'", "grade_level": 3, "release_date": "2023-05", "category": "' + random_data['random_category'] + '","keywords": ["math"], "student_expectations": ["'+ random_data['random_student_expectation'] +'"],"response_type": "'+ random_data['random_response_type'] +'","question_content": "'+ random_data['random_question_content'] + '","question_img": "","options": [{"letter": "' + random_data['random_letter'] + '","content": "'+ random_data['random_question_content'] +'","image": "","unit": "pounds","is_answer": true},{"letter": "' + random_data['random_letter'] + '","content": "option b","image": "","unit": "pounds","is_answer": false}]}'}

    header: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/update/staar/{sql_classic_invalid_uuid}"
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}\\tests\\images", "image_01.jpg")
    response = requests.request("PUT", url, headers=header, data=payload, files=upload_file)
    questions: dict = json.loads(response.text)
    # time.sleep(1)
    assert_that(response.status_code).is_equal_to(400)
    assert_that(questions['detail']).is_equal_to("Invalid uuid")