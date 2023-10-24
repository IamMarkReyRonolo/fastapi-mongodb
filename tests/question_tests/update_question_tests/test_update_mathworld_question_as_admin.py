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
def test_update_mathworld_question(get_admin_token):
    req: Requester = Requester()
    random_data: dict = common.get_mathworld_random_payload_data()
    mathworld_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = 'Mathworld' LIMIT 1")
    sql_classic_uuid: str = mathworld_classic[0][0]
    sql_classic_question_type: str = mathworld_classic[0][4]
    sql_classic_question: str = mathworld_classic[0][6]
    sql_classic_status: str = mathworld_classic[0][8]

    random_payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 3, \
        "teks_code": "A.1", \
        "subject": "Algebra I", \
        "topic": "' + random_data['random_topic'] + '", \
        "category": "' + random_data['random_category'] + '", \
        "keywords": ["happy"], \
        "student_expectations": ["' + random_data['random_student_expectations'] + '"], \
        "difficulty": "'+ random_data['random_difficulty'] + '", \
        "points": 2, \
        "response_type": "' + random_data['random_response_type'] + '", \
        "question_content": "'+ random_data['random_question_content'] + '", \
        "question_img": "", \
        "update_note": "'+ random_data['random_question_content'] + '", \
        "options": [ \
            { \
            "letter": "' + random_data['random_letter']+ '", \
            "content": "' + random_data['random_question_content'] + '", \
            "image": "", \
            "unit": "' + random_data['random_unit'] + '", \
            "is_answer": true \
            } \
        ] \
        }'}

    header: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/update/mathworld/{sql_classic_uuid}"
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}\\tests\\images", "image_01.jpg")
    response = requests.request("PUT", url, headers=header, data=random_payload, files=upload_file)
    updated_response: dict = json.loads(response.text)
    time.sleep(2)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(updated_response['detail']).is_equal_to("Successfully updated")
    assert_that(updated_response['question_uuid']).is_equal_to(sql_classic_uuid)
    sql_mathworld_updated: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{sql_classic_uuid}'")

    sql_updated_uuid: str = sql_mathworld_updated[0][0]
    sql_updated_question_type: str = sql_mathworld_updated[0][4]
    sql_updated_response_type: str = sql_mathworld_updated[0][5]
    sql_updated_question: str = sql_mathworld_updated[0][6]
    sql_updated_status: str = sql_mathworld_updated[0][8]
    # time.sleep(1)
    assert_that(sql_updated_uuid).is_equal_to(sql_classic_uuid)
    assert_that(sql_updated_question_type).is_equal_to(sql_classic_question_type)
    assert_that(sql_updated_response_type).is_equal_to(random_data['random_response_type'])
    assert_that(sql_updated_question).is_not_equal_to(sql_classic_question)
    assert_that(sql_updated_status).is_equal_to(sql_classic_status)


@pytest.mark.tc_002
def test_update_mathworld_question_invalid_uuid(get_admin_token):
    req: Requester = Requester()
    random_data: dict = common.get_mathworld_random_payload_data()
    mathworld_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = 'Mathworld' LIMIT 1")
    sql_classic_invalid_uuid: str = mathworld_classic[0][0] + "333"

    random_payload = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 3, \
        "teks_code": "' + "20344" + '", \
        "subject": "' + random_data['random_subject'] + '", \
        "topic": "' + random_data['random_topic'] + '", \
        "category": "' + random_data['random_category'] + '", \
        "keywords": ["happy"], \
        "student_expectations": ["' + random_data['random_student_expectations'] + '"], \
        "difficulty": "'+ random_data['random_difficulty'] + '", \
        "points": 2, \
        "response_type": "' + random_data['random_response_type'] + '", \
        "question_content": "'+ random_data['random_question_content'] + '", \
        "question_img": "", \
        "update_note": "'+ random_data['random_question_content'] + '", \
        "options": [ \
            { \
            "letter": "' + random_data['random_letter']+ '", \
            "content": "' + random_data['random_question_content'] + '", \
            "image": "", \
            "unit": "' + random_data['random_unit'] + '", \
            "is_answer": true \
            } \
        ] \
        }'}

    header: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/update/mathworld/{sql_classic_invalid_uuid}"
    upload_file: list = common.set_image_file(f"{CURRENT_DIR}\\tests\\images", "image_01.jpg")
    response = requests.request("PUT", url, headers=header, data=random_payload, files=upload_file)
    updated_response: dict = json.loads(response.text)
    time.sleep(1)
    assert_that(response.status_code).is_equal_to(400)
    assert_that(updated_response['detail']).is_equal_to("Invalid Teks Code")