from pytest import fixture
import pdb, requests
import os, sys, json
from assertpy import assert_that
import random
import time

CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)

import logging as logger, pytest
import lib.common as common
import lib.generate_token as generate_token
from lib.requester import Requester
from lib.mw_sql import execute_query
from faker import Faker

fake = Faker()

@fixture(scope="module")
def get_admin_token():
    token = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")


@pytest.mark.tc_001
def test_pending_questions(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'")
    sql_pending_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_pending_questions)

@pytest.mark.tc_002
def test_approved_questions(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'")
    sql_approved_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_approved_questions)

@pytest.mark.tc_003
def test_rejected_questions(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'")
    sql_rejected_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_rejected_questions)

@pytest.mark.tc_004
def test_reported_questions(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'")
    sql_rejected_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_rejected_questions)

@pytest.mark.tc_005
def test_staar_type_pending_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_006
def test_pending_status_staar_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    url: str = f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_007
def test_college_level_type_pending_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_008
def test_pending_status_college_level_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    url: str = f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_009
def test_pending_status_mathworld_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_010
def test_mathworld_type_pending_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_011
def test_approved_status_college_level_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    url: str = f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_012
def test_college_level_type_approved_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_013
def test_approved_status_mathworld_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_014
def test_mathworld_type_approved_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_015
def test_rejected_status_mathworld_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_016
def test_mathworld_type_rejected_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_017
def test_rejected_status_college_level_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_018
def test_college_level_type_rejected_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_019
def test_rejected_status_staar_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_020
def test_staar_type_rejected_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_021
def test_reported_status_staar_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    url: str = \
    f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_022
def test_staar_type_reported_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_023
def test_reported_status__type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_024
def test_college_level_type_reported_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_025
def test_reported_status_mathworld_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "mathworld"
    question_status: str = "Reported"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_026
def test_mathworld_type_reported_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    url: str = \
          f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_028
def test_ore_response_pending_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_029
def test_approved_status_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_030
def test_ore_response_approved_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_031
def test_rejected_status_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_032
def test_ore_response_rejected_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_033
def test_reported_status_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_034
def test_ore_response_reported_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_035
def test_pending_status_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_036
def test_ror_response_pending_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Pending"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_037
def test_pending_status_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_038
def test_mc_response_pending_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Pending"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_039
def test_pending_status_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_038
def test_cb_response_pending_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Pending"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)
# --------
@pytest.mark.tc_039
def test_approved_status_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_040
def test_ror_response_approved_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_041
def test_approved_status_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_042
def test_mc_response_approved_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_043
def test_rejected_status_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_044
def test_ror_response_rejected_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_045
def test_reported_status_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_046
def test_ror_response_reported_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_047
def test_rejected_status_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_048
def test_mc_response_rejected_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_049
def test_reported_status_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_050
def test_mc_response_reported_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_051
def test_rejected_status_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_052
def test_cb_response_rejected_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_053
def test_cb_response_reported_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_054
def test_reported_status_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_055
def test_pending_status_staar_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_056
def test_approved_status_staar_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_057
def test_rejected_status_staar_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_058
def test_reported_status_staar_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_059
def test_pending_status_college_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_060
def test_approved_status_college_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_061
def test_rejected_status_college_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_062
def test_reported_status_college_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_063
def test_pending_status_mathworld_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_064
def test_approved_status_mathworld_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_065
def test_rejected_status_mathworld_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_066
def test_reported_status_mathworld_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_067
def test_pending_status_college_type_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_068
def test_approved_status_college_type_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_069
def test_rejected_status_college_type_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_070
def test_reported_status_college_type_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_071
def test_pending_status_mathworld_type_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_072
def test_approved_status_mathworld_type_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_073
def test_rejected_status_mathworld_type_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_074
def test_reported_status_mathworld_type_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_075
def test_pending_status_staar_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_076
def test_approved_status_staar_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_077
def test_rejected_status_staar_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_078
def test_reported_status_staar_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_079
def test_pending_status_college_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_080
def test_approved_status_college_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_081
def test_rejected_status_college_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_082
def test_reported_status_college_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_083
def test_pending_status_mathworld_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_084
def test_approved_status_mathworld_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_085
def test_rejected_status_mathworld_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_086
def test_reported_status_mathworld_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_087
def test_pending_status_staar_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_088
def test_approved_status_staar_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_089
def test_rejected_status_staar_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_090
def test_reported_status_staar_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_091
def test_pending_status_college_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_092
def test_approved_status_college_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_093
def test_rejected_status_college_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_094
def test_reported_status_college_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_095
def test_pending_status_mathworld_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_096
def test_approved_status_mathworld_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_097
def test_rejected_status_mathworld_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

@pytest.mark.tc_098
def test_reported_status_mathworld_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported    "
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}'\
          AND response_type = '{response_type}' AND question_type = '{question_type}'")
    sql_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions['total']).is_greater_than_or_equal_to(sql_questions)

# --------------------------------------------page 1--------------------------------------------------------------------

@pytest.mark.tc_099
def test_pending_questions_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_num = 1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_100
def test_approved_questions_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_101
def test_rejected_questions_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_102
def test_reported_questions_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    # assert questions['data'] != []

@pytest.mark.tc_103
def test_staar_type_pending_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = \
    f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_104
def test_pending_status_staar_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_105
def test_college_level_type_pending_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_106
def test_pending_status_college_level_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_107
def test_pending_status_mathworld_type_Page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_108
def test_mathworld_type_pending_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}&question_type={question_type}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_109
def test_approved_status_college_level_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&page_num={page_num}&question_status={question_status}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_110
def test_college_level_type_approved_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_111
def test_approved_status_mathworld_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_112
def test_mathworld_type_approved_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_113
def test_rejected_status_mathworld_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_114
def test_mathworld_type_rejected_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = \
    f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_115
def test_rejected_status_college_level_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_116
def test_college_level_type_rejected_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_117
def test_rejected_status_staar_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = \
    f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_118
def test_staar_type_rejected_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_119
def test_reported_status_staar_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_120
def test_staar_type_reported_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_121
def test_reported_status__type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_122
def test_college_level_type_reported_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_123
def test_reported_status_mathworld_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_num: int = 1    
    create_response: dict = common.create_a_mathworld_question('admin')
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)    
    url: str = f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_124
def test_mathworld_type_reported_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_num: int = 1
    create_response: dict = common.create_a_mathworld_question('admin')
    update_response = common.update_question_status(create_response['question_uuid'], question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_125
def test_pending_status_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_126
def test_ore_response_pending_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_127
def test_approved_status_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_128
def test_ore_response_approved_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_129
def test_rejected_status_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_130
def test_ore_response_rejected_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_131
def test_reported_status_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_132
def test_ore_response_reported_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_133
def test_pending_status_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_134
def test_ror_response_pending_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_135
def test_pending_status_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_136
def test_mc_response_pending_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_137
def test_pending_status_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_138
def test_cb_response_pending_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
# --------
@pytest.mark.tc_139
def test_approved_status_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_140
def test_ror_response_approved_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_141
def test_approved_status_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_142
def test_mc_response_approved_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_143
def test_rejected_status_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_144
def test_ror_response_rejected_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_145
def test_reported_status_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_146
def test_ror_response_reported_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_147
def test_rejected_status_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_148
def test_mc_response_rejected_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_149
def test_reported_status_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 1
    url: str =\
         f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_150
def test_mc_response_reported_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_151
def test_rejected_status_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_152
def test_cb_response_rejected_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_153
def test_cb_response_reported_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_154
def test_reported_status_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_155
def test_pending_status_staar_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_156
def test_approved_status_staar_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_157
def test_rejected_status_staar_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_158
def test_reported_status_staar_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_159
def test_pending_status_college_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_160
def test_approved_status_college_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_161
def test_rejected_status_college_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_162
def test_reported_status_college_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_163
def test_pending_status_mathworld_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_164
def test_approved_status_mathworld_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_165
def test_rejected_status_mathworld_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_166
def test_reported_status_mathworld_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    page_num: int = 1
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_167
def test_pending_status_college_type_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_168
def test_approved_status_college_type_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_169
def test_rejected_status_college_type_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_170
def test_reported_status_college_type_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_171
def test_pending_status_mathworld_type_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_172
def test_approved_status_mathworld_type_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_173
def test_rejected_status_mathworld_type_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_174
def test_reported_status_mathworld_type_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_new_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 1
    mathworld_response: dict = common.create_a_mathworld_question("admin", response_type)
    qustion_uuid: str = mathworld_response['question_uuid']
    mathworld_status = common.update_question_status(qustion_uuid, question_new_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_new_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_175
def test_pending_status_staar_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_176
def test_approved_status_staar_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_177
def test_rejected_status_staar_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_178
def test_reported_status_staar_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_179
def test_pending_status_college_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

def test_approved_status_college_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    mathworld_response: dict = common.create_a_mathworld_question("admin", response_type)
    qustion_uuid: str = mathworld_response['question_uuid']
    mathworld_status = common.update_question_status(qustion_uuid, response_type)    
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_181
def test_rejected_status_college_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_182
def test_reported_status_college_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_183
def test_pending_status_mathworld_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    create_response: dict = common.create_a_mathworld_question('admin', response_type)
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['data'] != []
    assert questions['page'] == page_num    

@pytest.mark.tc_184
def test_approved_status_mathworld_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_185
def test_rejected_status_mathworld_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_186
def test_reported_status_mathworld_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    mathworld_response = common.create_a_mathworld_question("admin", response_type)
    time.sleep(1)
    mathworld_status = common.update_question_status(mathworld_response['question_uuid'], question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_187
def test_pending_status_staar_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_188
def test_approved_status_staar_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_189
def test_rejected_status_staar_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.key
@pytest.mark.tc_190
def test_reported_status_staar_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num    

@pytest.mark.tc_191
def test_pending_status_college_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_192
def test_approved_status_college_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_193
def test_rejected_status_college_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 1
    create_response = common.create_a_college_question("admin", response_type)
    assert_that(create_response['detail']).is_equal_to('Successfully Added Question')
    update_response = common.update_question_status(create_response['question_uuid'], question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_194
def test_reported_status_college_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_195
def test_pending_status_mathworld_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_196
def test_approved_status_mathworld_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_197
def test_rejected_status_mathworld_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.key
@pytest.mark.tc_198
def test_reported_status_mathworld_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 1
    mathworld_response = common.create_a_mathworld_question("admin", response_type)
    mathworld_status = common.update_question_status(mathworld_response['question_uuid'], question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

# ------------------------ page_num = 100 ------------------------

@pytest.mark.tc_199
def test_pending_questions_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_num = 100
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_200
def test_approved_questions_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    page_num: int = 100
    mathworld_response = common.create_a_mathworld_question("admin")
    mathworld_status = common.update_question_status(mathworld_response['question_uuid'], question_status)
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_201
def test_rejected_questions_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    page_num: int = 100
    create_response: dict = common.create_a_mathworld_question('admin')
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)
    url: str = f"{req.base_url}/question/fetch/all?question_status='{question_status}'&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num    

@pytest.mark.tc_202
def test_reported_questions_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_203
def test_staar_type_pending_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = \
    f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_204
def test_pending_status_staar_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_205
def test_college_level_type_pending_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_206
def test_pending_status_college_level_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_207
def test_pending_status_mathworld_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = 100
    create_response: dict = common.create_a_mathworld_question('admin')
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type='{question_type}'&question_status='{question_status}'&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_208
def test_mathworld_type_pending_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status='{question_status}'&page_num={page_num}&question_type='{question_type}'"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_209
def test_approved_status_college_level_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&page_num={page_num}&question_status={question_status}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_210
def test_college_level_type_approved_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_211
def test_approved_status_mathworld_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = 100
    create_response: dict = common.create_a_mathworld_question('admin')
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type='{question_type}'&question_status='{question_status}'&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_212
def test_mathworld_type_approved_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    create_response: dict = common.create_a_mathworld_question('admin')
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_213
def test_rejected_status_mathworld_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_214
def test_mathworld_type_rejected_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str =\
         f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_215
def test_rejected_status_college_level_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str =\
         f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == 100
    assert questions['data'] == []

@pytest.mark.tc_216
def test_college_level_type_rejected_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_217
def test_rejected_status_staar_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = \
    f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_218
def test_staar_type_rejected_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_219
def test_reported_status_staar_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?uestion_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_220
def test_staar_type_reported_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_221
def test_reported_status__type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_222
def test_college_level_type_reported_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_223
def test_reported_status_mathworld_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "mathworld"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_224
def test_mathworld_type_reported_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status='{question_status}'&question_type='{question_type}'&page_num={page_num}"
    create_response: dict = common.create_a_mathworld_question('admin')
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_225
def test_pending_status_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_226
def test_ore_response_pending_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_227
def test_approved_status_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_228
def test_ore_response_approved_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_229
def test_rejected_status_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_230
def test_ore_response_rejected_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_231
def test_reported_status_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_232
def test_ore_response_reported_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_233
def test_pending_status_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_235
def test_pending_status_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_236
def test_mc_response_pending_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_237
def test_pending_status_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_238
def test_cb_response_pending_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
# --------
@pytest.mark.tc_239
def test_approved_status_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_240
def test_ror_response_approved_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_241
def test_approved_status_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_242
def test_mc_response_approved_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data']== []

@pytest.mark.tc_243
def test_rejected_status_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_244
def test_ror_response_rejected_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_245
def test_reported_status_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_246
def test_ror_response_reported_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_247
def test_rejected_status_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_248
def test_mc_response_rejected_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_249
def test_reported_status_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_250
def test_mc_response_reported_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_251
def test_rejected_status_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_252
def test_cb_response_rejected_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_253
def test_cb_response_reported_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num    

@pytest.mark.tc_254
def test_reported_status_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num    

@pytest.mark.tc_255
def test_pending_status_staar_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_256
def test_approved_status_staar_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_257
def test_rejected_status_staar_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_258
def test_reported_status_staar_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_259
def test_pending_status_college_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    common.create_a_college_question('admin', response_type)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_260
def test_approved_status_college_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_261
def test_rejected_status_college_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_262
def test_reported_status_college_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_263
def test_pending_status_mathworld_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    create_response: dict = common.create_a_mathworld_question('admin', response_type)
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status='{question_status}'&question_type='{question_type}'&response_type='{response_type}'&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_264
def test_approved_status_mathworld_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_265
def test_rejected_status_mathworld_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_266
def test_reported_status_mathworld_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    page_num: int = 100
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_267
def test_pending_status_college_type_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_268
def test_approved_status_college_type_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_269
def test_rejected_status_college_type_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_270
def test_reported_status_college_type_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_271
def test_pending_status_mathworld_type_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_272
def test_approved_status_mathworld_type_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_273
def test_rejected_status_mathworld_type_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.key
@pytest.mark.tc_274
def test_reported_status_mathworld_type_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 100
    mathworld_response: dict = common.create_a_mathworld_question("admin", response_type)
    mathworld_status = common.update_question_status(mathworld_response['question_uuid'], question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_275
def test_pending_status_staar_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_276
def test_approved_status_staar_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_277
def test_rejected_status_staar_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_278
def test_reported_status_staar_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_279
def test_pending_status_college_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_280
def test_approved_status_college_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_281
def test_rejected_status_college_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_282
def test_reported_status_college_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_283
def test_pending_status_mathworld_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_284
def test_approved_status_mathworld_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_285
def test_rejected_status_mathworld_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_286
def test_reported_status_mathworld_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_287
def test_pending_status_staar_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_288
def test_approved_status_staar_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_289
def test_rejected_status_staar_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 100
    create_response: dict = common.create_a_mathworld_question('admin', response_type)
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_290
def test_reported_status_staar_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 100
    create_response: dict = common.create_a_mathworld_question('admin', response_type)
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_291
def test_pending_status_college_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 100
    create_response: dict = common.create_a_mathworld_question('admin', response_type)
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status='{question_status}'&question_type='{question_type}'&response_type='{response_type}'&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_292
def test_approved_status_college_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_293
def test_rejected_status_college_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_294
def test_reported_status_college_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_295
def test_pending_status_mathworld_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_296
def test_approved_status_mathworld_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

@pytest.mark.tc_297
def test_rejected_status_mathworld_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 100
    create_response: dict = common.create_a_mathworld_question('admin')
    time.sleep(2)
    update_response = common.update_question_status(create_response['question_uuid'], question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_298
def test_reported_status_mathworld_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] == []

# ------------- page_num = 0 ---------------------------------------------------------------------------------------------------------

@pytest.mark.tc_299
def test_pending_questions_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_num = 0
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_300
def test_approved_questions_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    page_num: int = 0
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_301
def test_rejected_questions_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_302
def test_reported_questions_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_303
def test_staar_type_pending_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = \
    f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_304
def test_pending_status_staar_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_305
def test_college_level_type_pending_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_306
def test_pending_status_college_level_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_307
def test_pending_status_mathworld_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = \
         f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_308
def test_mathworld_type_pending_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}&question_type={question_type}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_309
def test_approved_status_college_level_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&page_num={page_num}&question_status={question_status}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_310
def test_college_level_type_approved_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_311
def test_approved_status_mathworld_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_312
def test_mathworld_type_approved_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_313
def test_rejected_status_mathworld_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == 100
    assert questions['data'] != []

@pytest.mark.tc_314
def test_mathworld_type_rejected_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_315
def test_rejected_status_college_level_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_316
def test_college_level_type_rejected_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_317
def test_rejected_status_staar_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = \
    f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_318
def test_staar_type_rejected_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_319
def test_reported_status_staar_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_320
def test_staar_type_reported_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_321
def test_reported_status__type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_322
def test_college_level_type_reported_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_323
def test_reported_status_mathworld_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "mathworld"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_324
def test_mathworld_type_reported_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_325
def test_pending_status_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_326
def test_ore_response_pending_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_327
def test_approved_status_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_328
def test_ore_response_approved_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_329
def test_rejected_status_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_330
def test_ore_response_rejected_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_331
def test_reported_status_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_332
def test_ore_response_reported_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_333
def test_pending_status_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_334
def test_ror_response_pending_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_335
def test_pending_status_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_336
def test_mc_response_pending_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_337
def test_pending_status_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_338
def test_cb_response_pending_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"
# --------
@pytest.mark.tc_339
def test_approved_status_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_340
def test_ror_response_approved_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_341
def test_approved_status_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_342
def test_mc_response_approved_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_343
def test_rejected_status_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_344
def test_ror_response_rejected_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_345
def test_reported_status_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_346
def test_ror_response_reported_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_347
def test_rejected_status_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = \
         f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_348
def test_mc_response_rejected_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_349
def test_reported_status_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_350
def test_mc_response_reported_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_351
def test_rejected_status_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_352
def test_cb_response_rejected_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_353
def test_cb_response_reported_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_354
def test_reported_status_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_355
def test_pending_status_staar_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_356
def test_approved_status_staar_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_357
def test_rejected_status_staar_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_358
def test_reported_status_staar_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_359
def test_pending_status_college_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_360
def test_approved_status_college_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_361
def test_rejected_status_college_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_362
def test_reported_status_college_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_363
def test_pending_status_mathworld_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_364
def test_approved_status_mathworld_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_365
def test_rejected_status_mathworld_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_366
def test_reported_status_mathworld_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    page_num: int = 0
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_367
def test_pending_status_college_type_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_368
def test_approved_status_college_type_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_369
def test_rejected_status_college_type_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_370
def test_reported_status_college_type_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_371
def test_pending_status_mathworld_type_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_372
def test_approved_status_mathworld_type_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_373
def test_rejected_status_mathworld_type_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_374
def test_reported_status_mathworld_type_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_375
def test_pending_status_staar_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_376
def test_approved_status_staar_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_377
def test_rejected_status_staar_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_378
def test_reported_status_staar_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_379
def test_pending_status_college_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_380
def test_approved_status_college_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_381
def test_rejected_status_college_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_382
def test_reported_status_college_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_383
def test_pending_status_mathworld_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_384
def test_approved_status_mathworld_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_385
def test_rejected_status_mathworld_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_386
def test_reported_status_mathworld_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_387
def test_pending_status_staar_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_388
def test_approved_status_staar_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_389
def test_rejected_status_staar_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_390
def test_reported_status_staar_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_391
def test_pending_status_college_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_392
def test_approved_status_college_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_393
def test_rejected_status_college_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_394
def test_reported_status_college_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_395
def test_pending_status_mathworld_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_396
def test_approved_status_mathworld_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_397
def test_rejected_status_mathworld_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_398
def test_reported_status_mathworld_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

# -------------------------------------------- page_num = empty -------------------------------------------------------

@pytest.mark.tc_399
def test_pending_questions_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_num = ""
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_400
def test_approved_questions_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    page_num: str = ""
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_401
def test_rejected_questions_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_402
def test_reported_questions_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_403
def test_staar_type_pending_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = \
    f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_404
def test_pending_status_staar_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_405
def test_college_level_type_pending_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_406
def test_pending_status_college_level_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_407
def test_pending_status_mathworld_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_408
def test_mathworld_type_pending_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}&question_type={question_type}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_409
def test_approved_status_college_level_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&page_num={page_num}&question_status={question_status}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_410
def test_college_level_type_approved_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_411
def test_approved_status_mathworld_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_412
def test_mathworld_type_approved_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_413
def test_rejected_status_mathworld_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_414
def test_mathworld_type_rejected_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_415
def test_rejected_status_college_level_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_416
def test_college_level_type_rejected_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_417
def test_rejected_status_staar_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = \
    f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_418
def test_staar_type_rejected_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = \
         f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_419
def test_reported_status_staar_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_420
def test_staar_type_reported_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_421
def test_reported_status__type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_422
def test_college_level_type_reported_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_423
def test_reported_status_mathworld_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "mathworld"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_424
def test_mathworld_type_reported_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_425
def test_pending_status_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_426
def test_ore_response_pending_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_427
def test_approved_status_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_428
def test_ore_response_approved_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_429
def test_rejected_status_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_430
def test_ore_response_rejected_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_431
def test_reported_status_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_432
def test_ore_response_reported_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_433
def test_pending_status_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_434
def test_ror_response_pending_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_435
def test_pending_status_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_436
def test_mc_response_pending_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_437
def test_pending_status_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_438
def test_cb_response_pending_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"
# --------
@pytest.mark.tc_439
def test_approved_status_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_440
def test_ror_response_approved_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_441
def test_approved_status_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_442
def test_mc_response_approved_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_443
def test_rejected_status_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_444
def test_ror_response_rejected_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_445
def test_reported_status_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_446
def test_ror_response_reported_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_447
def test_rejected_status_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_448
def test_mc_response_rejected_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_449
def test_reported_status_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_450
def test_mc_response_reported_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_451
def test_rejected_status_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_452
def test_cb_response_rejected_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_453
def test_cb_response_reported_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_454
def test_reported_status_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_455
def test_pending_status_staar_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_456
def test_approved_status_staar_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_457
def test_rejected_status_staar_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_458
def test_reported_status_staar_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_459
def test_pending_status_college_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_460
def test_approved_status_college_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_461
def test_rejected_status_college_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_462
def test_reported_status_college_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_463
def test_pending_status_mathworld_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_464
def test_approved_status_mathworld_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_465
def test_rejected_status_mathworld_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_466
def test_reported_status_mathworld_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    page_num: str = ""
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_467
def test_pending_status_college_type_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_468
def test_approved_status_college_type_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_469
def test_rejected_status_college_type_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_470
def test_reported_status_college_type_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_471
def test_pending_status_mathworld_type_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_472
def test_approved_status_mathworld_type_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_473
def test_rejected_status_mathworld_type_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_474
def test_reported_status_mathworld_type_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_475
def test_pending_status_staar_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_476
def test_approved_status_staar_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_477
def test_rejected_status_staar_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_478
def test_reported_status_staar_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_479
def test_pending_status_college_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_480
def test_approved_status_college_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_481
def test_rejected_status_college_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_482
def test_reported_status_college_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_483
def test_pending_status_mathworld_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_484
def test_approved_status_mathworld_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_485
def test_rejected_status_mathworld_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_486
def test_reported_status_mathworld_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_487
def test_pending_status_staar_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_488
def test_approved_status_staar_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_489
def test_rejected_status_staar_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_490
def test_reported_status_mathworld_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_491
def test_pending_status_college_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_492
def test_approved_status_college_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_493
def test_rejected_status_college_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_494
def test_reported_status_college_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_495
def test_pending_status_mathworld_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_496
def test_approved_status_mathworld_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_497
def test_rejected_status_mathworld_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"

@pytest.mark.tc_498
def test_reported_status_mathworld_type_cb_response_page_empyt(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert questions['detail'][0]['msg'] == "value is not a valid integer"


# ------------------------------ page_num = negative ---------------------------------

@pytest.mark.tc_499
def test_pending_questions_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_num: int = -1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_500
def test_approved_questions_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    page_num: int = -1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_501
def test_rejected_questions_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_502
def test_reported_questions_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_503
def test_staar_type_pending_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = \
    f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_504
def test_pending_status_staar_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_505
def test_college_level_type_pending_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_506
def test_pending_status_college_level_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_507
def test_pending_status_mathworld_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_508
def test_mathworld_type_pending_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}&question_type={question_type}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_509
def test_approved_status_college_level_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&page_num={page_num}&question_status={question_status}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_510
def test_college_level_type_approved_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    time.sleep(1)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_511
def test_approved_status_mathworld_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_512
def test_mathworld_type_approved_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_513
def test_rejected_status_mathworld_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = \
         f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_514
def test_mathworld_type_rejected_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_515
def test_rejected_status_college_level_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_516
def test_college_level_type_rejected_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_517
def test_rejected_status_staar_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = \
    f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_518
def test_staar_type_rejected_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_519
def test_reported_status_staar_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_520
def test_staar_type_reported_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_521
def test_reported_status__type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_522
def test_college_level_type_reported_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_523
def test_reported_status_mathworld_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "mathworld"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_524
def test_mathworld_type_reported_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_525
def test_pending_status_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_526
def test_ore_response_pending_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_527
def test_approved_status_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_528
def test_ore_response_approved_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_529
def test_rejected_status_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_530
def test_ore_response_rejected_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_531
def test_reported_status_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_532
def test_ore_response_reported_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_533
def test_pending_status_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_534
def test_ror_response_pending_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_535
def test_pending_status_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_536
def test_mc_response_pending_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_537
def test_pending_status_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_538
def test_cb_response_pending_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"
# --------
@pytest.mark.tc_539
def test_approved_status_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_540
def test_ror_response_approved_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_541
def test_approved_status_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_542
def test_mc_response_approved_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_543
def test_rejected_status_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_544
def test_ror_response_rejected_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_545
def test_reported_status_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_546
def test_ror_response_reported_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_547
def test_rejected_status_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_548
def test_mc_response_rejected_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_549
def test_reported_status_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_550
def test_mc_response_reported_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_551
def test_rejected_status_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_552
def test_cb_response_rejected_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_553
def test_cb_response_reported_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_554
def test_reported_status_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_555
def test_pending_status_staar_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_556
def test_approved_status_staar_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_557
def test_rejected_status_staar_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_558
def test_reported_status_staar_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_559
def test_pending_status_college_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_560
def test_approved_status_college_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_561
def test_rejected_status_college_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_562
def test_reported_status_college_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_563
def test_pending_status_mathworld_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_564
def test_approved_status_mathworld_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_565
def test_rejected_status_mathworld_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_566
def test_reported_status_mathworld_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    page_num: int = -1
    response_type: str = "Open Response Exact"
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_567
def test_pending_status_college_type_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_568
def test_approved_status_college_type_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_569
def test_rejected_status_college_type_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_570
def test_reported_status_college_type_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_571
def test_pending_status_mathworld_type_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_572
def test_approved_status_mathworld_type_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_573
def test_rejected_status_mathworld_type_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_574
def test_reported_status_mathworld_type_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_575
def test_pending_status_staar_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_576
def test_approved_status_staar_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_577
def test_rejected_status_staar_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_578
def test_reported_status_staar_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_579
def test_pending_status_college_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_580
def test_approved_status_college_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_581
def test_rejected_status_college_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_582
def test_reported_status_college_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_583
def test_pending_status_mathworld_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_584
def test_approved_status_mathworld_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_585
def test_rejected_status_mathworld_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_586
def test_reported_status_mathworld_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_587
def test_pending_status_staar_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_588
def test_approved_status_staar_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_589
def test_rejected_status_staar_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_590
def test_reported_status_staar_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_591
def test_pending_status_college_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_592
def test_approved_status_college_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_593
def test_rejected_status_college_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_594
def test_reported_status_college_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_595
def test_pending_status_mathworld_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_596
def test_approved_status_mathworld_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_597
def test_rejected_status_mathworld_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

@pytest.mark.tc_598
def test_reported_status_mathworld_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == "Page number should not be equal or less than to 0"

# ----------------------------------page size = 1 --------------------------------------------

@pytest.mark.tc_600
def test_pending_question_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_size: int = 1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_602
def test_approved_questions_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    page_size: int = 1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_603
def test_rejected_question_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_604
def test_reported_questions_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_605
def test_staar_type_pending_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_size = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_606
def test_pending_status_staar_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_607
def test_college_level_type_pending_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_608
def test_pending_status_college_level_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_609
def test_pending_status_mathworld_type_size_1(get_admin_token):
    req:Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_610
def test_mathworld_type_pending_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_611
def test_approved_status_college_level_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_size: int = 1
    url: str =\
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_612
def test_college_level_type_approved_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_size: int = 1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_613
def test_approved_status_mathworld_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_size: int = 1
    url: str = f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_614
def test_mathworld_type_approved_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_615
def test_rejected_status_mathworld_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_616
def test_mathworld_type_rejected_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_617
def test_rejected_status_college_level_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_618
def test_college_level_type_rejected_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_619
def test_rejected_status_staar_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_620
def test_staar_type_rejected_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_621
def test_reported_status_staar_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_622
def test_staar_type_reported_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_623
def test_reported_status__type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = \
    f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_624
def test_college_level_type_reported_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_625
def test_reported_status_mathworld_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_size: int = 1
    create_response: dict = common.create_a_mathworld_question('admin')
    update_response = common.update_question_status(create_response['question_uuid'], question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size
    assert questions['data'] != []

@pytest.mark.tc_626
def test_mathworld_type_reported_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_size: int = 1
    create_response: dict = common.create_a_mathworld_question('admin')
    time.sleep(1)
    update_response = common.update_question_status(create_response['question_uuid'], question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_628
def test_ore_response_pending_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = \
          f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_629
def test_approved_status_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_630
def test_ore_response_approved_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_size: int = 1
    url: str \
        = f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_631
def test_rejected_status_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = \
          f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_632
def test_ore_response_rejected_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = \
         f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_633
def test_reported_status_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_634
def test_ore_response_reported_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_635
def test_pending_status_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_636
def test_ror_response_pending_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_637
def test_pending_status_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_638
def test_mc_response_pending_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_639
def test_pending_status_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_638
def test_cb_response_pending_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = \
    f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size
# --------
@pytest.mark.tc_639
def test_approved_status_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_640
def test_ror_response_approved_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_641
def test_approved_status_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_642
def test_mc_response_approved_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_643
def test_rejected_status_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_644
def test_ror_response_rejected_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_645
def test_reported_status_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_646
def test_ror_response_reported_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_647
def test_rejected_status_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_648
def test_mc_response_rejected_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_649
def test_reported_status_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_650
def test_mc_response_reported_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_651
def test_rejected_status_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_652
def test_cb_response_rejected_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_653
def test_cb_response_reported_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_654
def test_reported_status_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_655
def test_pending_status_staar_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_656
def test_approved_status_staar_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_657
def test_rejected_status_staar_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_658
def test_reported_status_staar_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_659
def test_pending_status_college_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_660
def test_approved_status_college_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_661
def test_rejected_status_college_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_662
def test_reported_status_college_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_663
def test_pending_status_mathworld_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_664
def test_approved_status_mathworld_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_665
def test_rejected_status_mathworld_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_666
def test_reported_status_mathworld_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    common.create_a_mathworld_question('admin', response_type)
    common.update_question_status('admin', question_status)
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_667
def test_pending_status_college_type_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_668
def test_approved_status_college_type_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_669
def test_rejected_status_college_type_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_670
def test_reported_status_college_type_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_671
def test_pending_status_mathworld_type_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_672
def test_approved_status_mathworld_type_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_673
def test_rejected_status_mathworld_type_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_674
def test_reported_status_mathworld_type_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_size: int = 1
    mathworld_response: dict = common.create_a_mathworld_question("admin", response_type)
    mathworld_status = common.update_question_status(mathworld_response['question_uuid'], question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_675
def test_pending_status_staar_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_676
def test_approved_status_staar_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_677
def test_rejected_status_staar_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_678
def test_reported_status_staar_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_679
def test_pending_status_college_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_680
def test_approved_status_college_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_size

@pytest.mark.tc_681
def test_rejected_status_college_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_682
def test_reported_status_college_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_683
def test_pending_status_mathworld_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    create_response: dict = common.create_a_mathworld_question('admin', response_type)
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_684
def test_approved_status_mathworld_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_685
def test_rejected_status_mathworld_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_687
def test_pending_status_staar_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_688
def test_approved_status_staar_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_689
def test_rejected_status_staar_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.key
@pytest.mark.tc_690
def test_reported_status_staar_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_size

@pytest.mark.tc_691
def test_pending_status_college_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_size: int = 1
    create_response: dict = common.create_a_college_question('admin', response_type)
    update_response = common.update_question_status(create_response['question_uuid'], question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_692
def test_approved_status_college_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_693
def test_rejected_status_college_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_694
def test_reported_status_college_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_695
def test_pending_status_mathworld_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_696
def test_approved_status_mathworld_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_697
def test_rejected_status_mathworld_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

@pytest.mark.tc_698
def test_reported_status_mathworld_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    create_response: dict = common.create_a_mathworld_question('admin', response_type)
    update_response = common.update_question_status(create_response['question_uuid'], question_status)
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size

# --------------------------------------------page 1--------------------------------------------------------------------

@pytest.mark.tc_699
def test_pending_questions_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_num = 1
    page_size: int = 1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_700
def test_approved_questions_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_701
def test_rejected_questions_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    page_num: int = 1
    page_size:int = 1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_702
def test_reported_questions_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_num={page_num}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_703
def test_staar_type_pending_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_size: int = 1
    page_num: int = 1
    url: str = \
    f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_704
def test_pending_status_staar_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_705
def test_college_level_type_pending_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_706
def test_pending_status_college_level_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_707
def test_pending_status_mathworld_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = \
    f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_708
def test_mathworld_type_pending_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_709
def test_approved_status_college_level_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&page_num={page_num}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_710
def test_college_level_type_approved_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_711
def test_approved_status_mathworld_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_712
def test_mathworld_type_approved_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_713
def test_rejected_status_mathworld_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = 1
    create_response: dict = common.create_a_mathworld_question('admin')
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_714
def test_mathworld_type_rejected_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []

@pytest.mark.tc_715
def test_rejected_status_college_level_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_716
def test_college_level_type_rejected_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_717
def test_rejected_status_staar_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = \
    f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_718
def test_staar_type_rejected_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_size: int = 1
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['page'] == page_size

@pytest.mark.tc_719
def test_reported_status_staar_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_720
def test_staar_type_reported_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_721
def test_reported_status__type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_722
def test_college_level_type_reported_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_723
def test_reported_status_mathworld_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    mathworld_response: dict = common.create_a_mathworld_question("admin")
    question_uuid: str = mathworld_response['question_uuid']
    mathworld_status = common.update_question_status(question_uuid, question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['count'] == page_size
    assert questions['data'] != []

@pytest.mark.key
@pytest.mark.tc_724
def test_mathworld_type_reported_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    mathworld_response: dict = common.create_a_mathworld_question("admin")
    question_uuid = mathworld_response['question_uuid']
    mathworld_status = common.update_question_status(question_uuid, question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_725
def test_pending_status_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_726
def test_ore_response_pending_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size


@pytest.mark.tc_727
def test_approved_status_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_728
def test_ore_response_approved_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_729
def test_rejected_status_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_730
def test_ore_response_rejected_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_731
def test_reported_status_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_732
def test_ore_response_reported_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_733
def test_pending_status_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_734
def test_ror_response_pending_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_735
def test_pending_status_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_736
def test_mc_response_pending_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_737
def test_pending_status_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_738
def test_cb_response_pending_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size
# --------
@pytest.mark.tc_739
def test_approved_status_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_740
def test_ror_response_approved_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_741
def test_approved_status_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_742
def test_mc_response_approved_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_743
def test_rejected_status_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_size: int = 1
    page_num: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_744
def test_ror_response_rejected_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_745
def test_reported_status_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_746
def test_ror_response_reported_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_747
def test_rejected_status_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_748
def test_mc_response_rejected_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_749
def test_reported_status_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_750
def test_mc_response_reported_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_751
def test_rejected_status_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_752
def test_cb_response_rejected_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_753
def test_cb_response_reported_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_754
def test_reported_status_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_755
def test_pending_status_staar_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_756
def test_approved_status_staar_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_757
def test_rejected_status_staar_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_758
def test_reported_status_staar_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_759
def test_pending_status_college_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_760
def test_approved_status_college_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_761
def test_rejected_status_college_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_762
def test_reported_status_college_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_763
def test_pending_status_mathworld_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_764
def test_approved_status_mathworld_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_765
def test_rejected_status_mathworld_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_766
def test_reported_status_mathworld_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    page_num: int = 1
    response_type: str = "Open Response Exact"
    page_size: int = 1
    count: int = 1
    create_response: dict = common.create_a_mathworld_question('staff', response_type)
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == count

@pytest.mark.tc_767
def test_pending_status_college_type_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_768
def test_approved_status_college_type_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_769
def test_rejected_status_college_type_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_770
def test_reported_status_college_type_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_771
def test_pending_status_mathworld_type_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_772
def test_approved_status_mathworld_type_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_773
def test_rejected_status_mathworld_type_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_774
def test_reported_status_mathworld_type_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 1
    page_size: int = 1
    time.sleep(1)
    mathworld_response: dict = common.create_a_mathworld_question("admin", response_type) 
    question_uuid = mathworld_response['question_uuid']  
    mathworld_status = common.update_question_status(question_uuid, question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_775
def test_pending_status_staar_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_776
def test_approved_status_staar_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_777
def test_rejected_status_staar_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_778
def test_reported_status_staar_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_779
def test_pending_status_college_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_780
def test_approved_status_college_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    create_response: dict = common.create_a_mathworld_question('admin', response_type)
    time.sleep(1)
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)    
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num    
    assert questions['count'] == 0

@pytest.mark.tc_781
def test_rejected_status_college_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_782
def test_reported_status_college_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_783
def test_pending_status_mathworld_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    page_count: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    create_response: dict = common.create_a_mathworld_question('admin', response_type)
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)    
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    # assert questions['count'] == page_count
    assert questions['data'] != []
    
@pytest.mark.tc_784
def test_approved_status_mathworld_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_785
def test_rejected_status_mathworld_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size
    
@pytest.mark.tc_787
def test_pending_status_staar_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['page'] == page_size

@pytest.mark.tc_788
def test_approved_status_staar_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_789
def test_rejected_status_staar_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.key
@pytest.mark.tc_790
def test_reported_status_staar_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    create_response: dict = common.create_a_staar_question('admin', response_type)
    question_uuid: str = create_response['question_uuid']
    update_response = common.update_question_status(question_uuid, question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_791
def test_pending_status_college_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_792
def test_approved_status_college_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size:int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_793
def test_rejected_status_college_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_794
def test_reported_status_college_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    create_response: dict = common.create_a_college_question('admin', response_type)
    update_response = common.update_question_status(create_response['question_uuid'], question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_795
def test_pending_status_mathworld_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_796
def test_approved_status_mathworld_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_797
def test_rejected_status_mathworld_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

@pytest.mark.tc_798
def test_reported_status_mathworld_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    create_response: dict = common.create_a_mathworld_question('admin', response_type)
    update_response = common.update_question_status(create_response['question_uuid'], question_status)
    url: str = \
        f"{req.base_url}/question/fetch/all?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['page'] == page_num
    assert questions['data'] != []
    assert questions['count'] == page_size

    # ----------------------------------- page_size max -----------------------------------

@pytest.mark.tc_799
def test_pending_question_size_2(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_size: int = 2
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size
    assert len(questions['data']) == page_size

@pytest.mark.tc_800
def test_pending_question_size_large(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_size: int = 500
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions['count'] == page_size
    assert len(questions['data']) == page_size

@pytest.mark.tc_801
def test_pending_question_size_zero(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_size: int = 0
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == 'Page size should not be equal or less than to 0'

@pytest.mark.tc_802
def test_pending_question_size_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_size: int = -1
    url: str = f"{req.base_url}/question/fetch/all?question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions['detail'] == 'Page size should not be equal or less than to 0'
