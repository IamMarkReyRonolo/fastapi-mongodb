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
from lib.mw_sql import execute_query
from lib.common import get_random_question, get_current_yyyy_mm, get_random_payload_data
import random
from assertpy import assert_that



@fixture(scope="module")
def get_staff_token():
    token = generate_token.generate_token(email="staffABC@gmail.com", password="Staff123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")

# ---------------------------------------
# Test Cases: Mathworld Status Update as Admin
# Author: Yshmael Ammonraheem
# Status: Approved, Pending, Rejected, Reported
# Question Type: Mathworld, Mathworld, Mathworld
# ----------------------------------------
# Pending -> Approved
# Pending -> Rejected
# Pending -> Reported
# ----------------------------------------
@pytest.mark.tc_001
def test_status_pending_to_approved(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    update_status: str = 'Approved'
    question_type: str = "Mathworld"
    header: dict = req.create_basic_headers(token=get_staff_token)
    create_url = f"{req.base_url}/question/mathworld/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()
    teks_code = common.get_random_tek_code()
    unit = common.get_random_unit()

    payload = {'data': '{ \
        "question_type": "Mathworld", \
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

    patch_payload = json.dumps({
      "status": f"{update_status}",
      "update_note": f"{random_data['random_sentence']}",
      "reviewed_by": f"{random_data['random_name']}",
      "reviewed_at": f"{random_data['current_datetime']}"
    })

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    classic_response = requests.request("POST", create_url, headers=header, data=payload, files=upload_file)
    json_classic_response = json.loads(classic_response.text)
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{json_classic_response['question_uuid']}'")
    classic_status : str = questions_returned[0][8]
    assert_that(classic_status).is_equal_to("Pending")
    patch_url: str = f"{req.base_url}/question/update/question_status/{json_classic_response['question_uuid']}"
    patch_response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
    json_patch_response = json.loads(patch_response.text)

    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(json_patch_response['data']['status']).is_equal_to('Approved')
    assert_that(json_patch_response['data']['question_type']).is_equal_to_ignoring_case(question_type)

# ---------------------------------------------------------------------------------

@pytest.mark.tc_002
def test_status_pending_to_reported(get_staff_token):
    req = Requester()
    create_url = f"{req.base_url}/question/mathworld/create"
    random_data: dict = common.get_random_payload_data()
    update_status: str = 'Reported'
    question_type: str = "Mathworld"
    header: dict = req.create_basic_headers(token=get_staff_token)

    question1 = common.get_random_question()
    question2 = common.get_random_question()
    teks_code = common.get_random_tek_code()
    unit = common.get_random_unit()

    payload = {'data': '{ \
        "question_type": "Mathworld", \
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

    patch_payload = json.dumps({
      "status": f"{update_status}",
      "update_note": f"{random_data['random_sentence']}",
      "reviewed_by": f"{random_data['random_name']}",
      "reviewed_at": f"{random_data['current_datetime']}"
    })

    upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    classic_response = requests.request("POST", create_url, headers=header, data=payload, files=upload_file)
    json_classic_response = json.loads(classic_response.text)
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{json_classic_response['question_uuid']}'")
    classic_status : str = questions_returned[0][8]
    assert_that(classic_status).is_equal_to("Pending")
    patch_url: str = f"{req.base_url}/question/update/question_status/{json_classic_response['question_uuid']}"
    patch_response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
    json_patch_response = json.loads(patch_response.text)

    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(json_patch_response['data']['status']).is_equal_to('Reported')
    assert_that(json_patch_response['data']['question_type']).is_equal_to_ignoring_case(question_type)


# ---------------------------------------------------------------------------------
# Approved -> Pending
# Rejected -> Pending
# Reported -> Pending
# Pending -> Pending
# ---------------------------------------------------------------------------------

@pytest.mark.tc_004
def test_status_approved_to_pending(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = 'Approved'
    update_status: str = 'Pending'
    question_type: str = "Mathworld"
    approved_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = '{question_type}' AND status = '{current_status}' LIMIT 1")
    sql_classic_uuid: str = approved_classic[0][0]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps({
      "status": f"{update_status}",
      "update_note": f"{random_data['random_sentence']}",
      "reviewed_by": f"{random_data['random_name']}",
      "reviewed_at": f"{random_data['current_datetime']}"
    })

    patch_url: str = f"{req.base_url}/question/update/question_status/{sql_classic_uuid}"
    patch_response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
    json_patch_response = json.loads(patch_response.text)

    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{sql_classic_uuid}'")
    status_updated : str = questions_returned[0][8]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response['data']['status']).is_equal_to(update_status)

@pytest.mark.tc_005
def test_status_rejected_to_pending(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = 'Rejected'
    update_status: str = 'Pending'
    question_type: str = "Mathworld"
    approved_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = '{question_type}' AND status = '{current_status}' LIMIT 1")
    sql_classic_uuid: str = approved_classic[0][0]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps({
      "status": f"{update_status}",
      "update_note": f"{random_data['random_sentence']}",
      "reviewed_by": f"{random_data['random_name']}",
      "reviewed_at": f"{random_data['current_datetime']}"
    })

    patch_url: str = f"{req.base_url}/question/update/question_status/{sql_classic_uuid}"
    patch_response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
    json_patch_response = json.loads(patch_response.text)

    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{sql_classic_uuid}'")
    status_updated : str = questions_returned[0][8]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response['data']['status']).is_equal_to(update_status)

@pytest.mark.tc_005
def test_status_reported_to_pending(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = 'Reported'
    update_status: str = 'Pending'
    question_type: str = "Mathworld"
    approved_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = '{question_type}' AND status = '{current_status}' LIMIT 1")
    sql_classic_uuid: str = approved_classic[0][0]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps({
      "status": f"{update_status}",
      "update_note": f"{random_data['random_sentence']}",
      "reviewed_by": f"{random_data['random_name']}",
      "reviewed_at": f"{random_data['current_datetime']}"
    })

    patch_url: str = f"{req.base_url}/question/update/question_status/{sql_classic_uuid}"
    patch_response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
    json_patch_response = json.loads(patch_response.text)

    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{sql_classic_uuid}'")
    status_updated : str = questions_returned[0][8]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response['data']['status']).is_equal_to(update_status)


# ---------------------------------------------------------------------------------
# Approved -> Approved
# Rejected -> Approved
# Reported -> Approved
# Pending -> Approved
# ---------------------------------------------------------------------------------

@pytest.mark.tc_006
def test_status_approved_to_approved(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = 'Approved'
    update_status: str = 'Approved'
    question_type: str = "Mathworld"
    approved_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = '{question_type}' AND status = '{current_status}' LIMIT 1")
    sql_classic_uuid: str = approved_classic[0][0]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps({
      "status": f"{update_status}",
      "update_note": f"{random_data['random_sentence']}",
      "reviewed_by": f"{random_data['random_name']}",
      "reviewed_at": f"{random_data['current_datetime']}"
    })

    patch_url: str = f"{req.base_url}/question/update/question_status/{sql_classic_uuid}"
    patch_response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
    json_patch_response = json.loads(patch_response.text)

    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{sql_classic_uuid}'")
    status_updated : str = questions_returned[0][8]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response['data']['status']).is_equal_to(update_status)

@pytest.mark.tc_007
def test_status_rejected_to_approved(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = 'Rejected'
    update_status: str = 'Approved'
    question_type: str = "Mathworld"
    approved_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = '{question_type}' AND status = '{current_status}' LIMIT 1")
    sql_classic_uuid: str = approved_classic[0][0]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps({
      "status": f"{update_status}",
      "update_note": f"{random_data['random_sentence']}",
      "reviewed_by": f"{random_data['random_name']}",
      "reviewed_at": f"{random_data['current_datetime']}"
    })

    patch_url: str = f"{req.base_url}/question/update/question_status/{sql_classic_uuid}"
    patch_response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
    json_patch_response = json.loads(patch_response.text)

    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{sql_classic_uuid}'")
    updated_status : str = questions_returned[0][8]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(updated_status)
    assert_that(json_patch_response['data']['status']).is_equal_to(update_status)

# ---------------------------------------------------------------------------------
# Approved -> Reported
# Rejected -> Reported
# Reported -> Reported
# Pending -> Reported
# ---------------------------------------------------------------------------------

@pytest.mark.tc_008
def test_status_approved_to_reported(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = 'Approved'
    update_status: str = 'Approved'
    question_type: str = "Mathworld"
    approved_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = '{question_type}' AND status = '{current_status}' LIMIT 1")
    sql_classic_uuid: str = approved_classic[0][0]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps({
      "status": f"{update_status}",
      "update_note": f"{random_data['random_sentence']}",
      "reviewed_by": f"{random_data['random_name']}",
      "reviewed_at": f"{random_data['current_datetime']}"
    })

    patch_url: str = f"{req.base_url}/question/update/question_status/{sql_classic_uuid}"
    patch_response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
    json_patch_response = json.loads(patch_response.text)

    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{sql_classic_uuid}'")
    updated_status : str = questions_returned[0][8]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(updated_status).is_equal_to('Approved')
    assert_that(json_patch_response['data']['status']).is_equal_to(update_status)

@pytest.mark.tc_009
def test_status_rejected_to_reported(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = 'Rejected'
    update_status: str = 'Reported'
    question_type: str = "Mathworld"
    approved_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = '{question_type}' AND status = '{current_status}' LIMIT 1")
    sql_classic_uuid: str = approved_classic[0][0]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps({
      "status": f"{update_status}",
      "update_note": f"{random_data['random_sentence']}",
      "reviewed_by": f"{random_data['random_name']}",
      "reviewed_at": f"{random_data['current_datetime']}"
    })

    patch_url: str = f"{req.base_url}/question/update/question_status/{sql_classic_uuid}"
    patch_response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
    json_patch_response = json.loads(patch_response.text)

    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{sql_classic_uuid}'")
    status_updated : str = questions_returned[0][8]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response['data']['status']).is_equal_to(update_status)

@pytest.mark.tc_010
def test_status_reported_to_approved(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = 'Pending'
    update_status: str = 'Approved'
    question_type: str = "Mathworld"
    approved_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = '{question_type}' AND status = '{current_status}' LIMIT 1")
    sql_classic_uuid: str = approved_classic[0][0]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps({
      "status": f"{update_status}",
      "update_note": f"{random_data['random_sentence']}",
      "reviewed_by": f"{random_data['random_name']}",
      "reviewed_at": f"{random_data['current_datetime']}"
    })

    patch_url: str = f"{req.base_url}/question/update/question_status/{sql_classic_uuid}"
    patch_response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
    json_patch_response = json.loads(patch_response.text)

    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{sql_classic_uuid}'")
    status_updated : str = questions_returned[0][8]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response['data']['status']).is_equal_to(update_status)

@pytest.mark.tc_011
def test_status_pending_to_pending(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = 'Pending'
    update_status: str = 'Approved'
    question_type: str = "Mathworld"
    approved_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = '{question_type}' AND status = '{current_status}' LIMIT 1")
    sql_classic_uuid: str = approved_classic[0][0]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps({
      "status": f"{update_status}",
      "update_note": f"{random_data['random_sentence']}",
      "reviewed_by": f"{random_data['random_name']}",
      "reviewed_at": f"{random_data['current_datetime']}"
    })

    patch_url: str = f"{req.base_url}/question/update/question_status/{sql_classic_uuid}"
    patch_response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
    json_patch_response = json.loads(patch_response.text)

    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{sql_classic_uuid}'")
    status_updated : str = questions_returned[0][8]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response['data']['status']).is_equal_to(update_status)

# ---------------------------------------------------------------------------------
# Approved -> Rejected
# Rejected -> Rejected
# Reported -> Rejected
# Pending -> Rejected
# ---------------------------------------------------------------------------------

@pytest.mark.tc_012
def test_status_approved_to_rejected(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = 'Approved'
    update_status: str = 'Rejected'
    question_type: str = "Mathworld"
    approved_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = '{question_type}' AND status = '{current_status}' LIMIT 1")
    sql_classic_uuid: str = approved_classic[0][0]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps({
      "status": f"{update_status}",
      "update_note": f"{random_data['random_sentence']}",
      "reviewed_by": f"{random_data['random_name']}",
      "reviewed_at": f"{random_data['current_datetime']}"
    })

    patch_url: str = f"{req.base_url}/question/update/question_status/{sql_classic_uuid}"
    patch_response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
    json_patch_response = json.loads(patch_response.text)

    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{sql_classic_uuid}'")
    status_updated : str = questions_returned[0][8]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response['data']['status']).is_equal_to(update_status)

@pytest.mark.tc_013
def test_status_rejected_to_rejected(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = 'Rejected'
    update_status: str = 'Rejected'
    question_type: str = "Mathworld"
    approved_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = '{question_type}' AND status = '{current_status}' LIMIT 1")
    sql_classic_uuid: str = approved_classic[0][0]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps({
      "status": f"{update_status}",
      "update_note": f"{random_data['random_sentence']}",
      "reviewed_by": f"{random_data['random_name']}",
      "reviewed_at": f"{random_data['current_datetime']}"
    })

    patch_url: str = f"{req.base_url}/question/update/question_status/{sql_classic_uuid}"
    patch_response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
    json_patch_response = json.loads(patch_response.text)

    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{sql_classic_uuid}'")
    status_updated : str = questions_returned[0][8]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response['data']['status']).is_equal_to(update_status)

@pytest.mark.tc_014
def test_status_reported_to_rejected(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = 'Reported'
    update_status: str = 'Rejected'
    question_type: str = "Mathworld"
    approved_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = '{question_type}' AND status = '{current_status}' LIMIT 1")
    sql_classic_uuid: str = approved_classic[0][0]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps({
      "status": f"{update_status}",
      "update_note": f"{random_data['random_sentence']}",
      "reviewed_by": f"{random_data['random_name']}",
      "reviewed_at": f"{random_data['current_datetime']}"
    })

    patch_url: str = f"{req.base_url}/question/update/question_status/{sql_classic_uuid}"
    patch_response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
    json_patch_response = json.loads(patch_response.text)

    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{sql_classic_uuid}'")
    status_updated : str = questions_returned[0][8]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response['data']['status']).is_equal_to(update_status)

@pytest.mark.tc_015
def test_status_pending_to_rejected(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = 'Pending'
    update_status: str = 'Rejected'
    question_type: str = "Mathworld"
    approved_classic: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE question_type = '{question_type}' AND status = '{current_status}' LIMIT 1")
    sql_classic_uuid: str = approved_classic[0][0]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps({
      "status": f"{update_status}",
      "update_note": f"{random_data['random_sentence']}",
      "reviewed_by": f"{random_data['random_name']}",
      "reviewed_at": f"{random_data['current_datetime']}"
    })

    patch_url: str = f"{req.base_url}/question/update/question_status/{sql_classic_uuid}"
    patch_response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
    json_patch_response = json.loads(patch_response.text)

    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE uuid = '{sql_classic_uuid}'")
    status_updated : str = questions_returned[0][8]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response['data']['status']).is_equal_to(update_status)