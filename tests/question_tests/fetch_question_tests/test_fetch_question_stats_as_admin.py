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
def test_fetch_question_total_statistics(get_admin_token):
    req: Requester = Requester()
    staar_returned: list = execute_query(
        f"SELECT COUNT(*) FROM mathworld.question WHERE question_type = 'STAAR' AND status = 'Approved'")
    num_of_staars: int = staar_returned[0][0]

    college_returned: list = execute_query(
        f"SELECT COUNT(*) FROM mathworld.question WHERE question_type = 'College Level' AND status = 'Approved'")
    num_of_colleges: int = college_returned[0][0]

    mathworld_returned: list = execute_query(
        f"SELECT COUNT(*) FROM mathworld.question WHERE question_type = 'MathWorld' AND status = 'Approved'")
    num_of_mathworlds: int = mathworld_returned[0][0]

    headers: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/fetch/question_statistics"
    response = requests.request("GET", url, headers=headers)
    json_response: dict = json.loads(response.text)
    assert response.status_code == 200
    questions_stats: dict = json.loads(response.text)
    total_stat: int = questions_stats['statistics']['staar_total_count'] + \
        questions_stats['statistics']['college_total_count'] + questions_stats['statistics']['mathworld_total_count']
    assert_that(total_stat).is_equal_to(questions_stats['statistics']['total'])

@pytest.mark.tc_002
def test_fetch_question_staar_total_count(get_admin_token):
    req: Requester = Requester()
    staar_returned: list = execute_query(
        f"SELECT COUNT(*) FROM mathworld.question WHERE question_type = 'STAAR' AND status = 'Approved'")
    num_of_staars: int = staar_returned[0][0]
    headers: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/fetch/question_statistics"
    response = requests.request("GET", url, headers=headers)
    questions_stats: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(questions_stats['statistics']['staar_total_count']).is_equal_to(num_of_staars)

@pytest.mark.tc_003
def test_fetch_question_college_total_count(get_admin_token):
    req: Requester = Requester()
    college_returned: list = execute_query(
        f"SELECT COUNT(*) FROM mathworld.question WHERE question_type = 'College Level' AND status = 'Approved'")
    num_of_college: int = college_returned[0][0]
    headers: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/fetch/question_statistics"
    response = requests.request("GET", url, headers=headers)
    questions_stats: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(questions_stats['statistics']['college_total_count']).is_equal_to(num_of_college)

@pytest.mark.tc_004
def test_fetch_question_mathworld_total_count(get_admin_token):
    req: Requester = Requester()
    mathworld_returned: list = execute_query(
        f"SELECT COUNT(*) FROM mathworld.question WHERE question_type = 'Mathworld' AND status = 'Approved'")
    num_of_mathword: int = mathworld_returned[0][0]
    headers: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/fetch/question_statistics"
    response = requests.request("GET", url, headers=headers)
    questions_stats: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(questions_stats['statistics']['mathworld_total_count']).is_equal_to(num_of_mathword)

@pytest.mark.tc_005
def test_fetch_question_stats_invalid_token(get_admin_token):
    req: Requester = Requester()
    mathworld_returned: list = execute_query(
        f"SELECT COUNT(*) FROM mathworld.question WHERE question_type = 'MathWorld' AND status = 'Approved'")
    num_of_mathword: int = mathworld_returned[0][0]
    headers: dict = req.create_basic_headers(token=get_admin_token + "x")
    url: str = f"{req.base_url}/question/fetch/question_statistics"
    response = requests.request("GET", url, headers=headers)
    questions_stats: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(403)
    assert_that(questions_stats['detail']).is_equal_to('Invalid token or expired token.')

@pytest.mark.tc_007
def test_fetch_question_stats_pending(get_admin_token):
    req: Requester = Requester()
    mathworld_returned: list = execute_query(
        f"SELECT COUNT(*) FROM mathworld.question WHERE question_type = 'MathWorld' AND status = 'Pending'")
    num_of_mathword: int = mathworld_returned[0][0]
    headers: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/fetch/question_statistics"
    response = requests.request("GET", url, headers=headers)
    questions_stats: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(questions_stats['statistics']['mathworld_total_count']).is_not_equal_to(num_of_mathword)

@pytest.mark.tc_008
def test_fetch_question_stats_rejected(get_admin_token):
    req: Requester = Requester()
    mathworld_returned: list = execute_query(
        f"SELECT COUNT(*) FROM mathworld.question WHERE question_type = 'MathWorld' AND status = 'Rejected'")
    num_of_mathword: int = mathworld_returned[0][0]
    headers: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/fetch/question_statistics"
    response = requests.request("GET", url, headers=headers)
    questions_stats: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(questions_stats['statistics']['mathworld_total_count']).is_not_equal_to(num_of_mathword)

@pytest.mark.tc_009
def test_fetch_question_stats_reported(get_admin_token):
    req: Requester = Requester()
    mathworld_returned: list = execute_query(
        f"SELECT COUNT(*) FROM mathworld.question WHERE question_type = 'MathWorld' AND status = 'Reported'")
    num_of_mathword: int = mathworld_returned[0][0]
    headers: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/fetch/question_statistics"
    response = requests.request("GET", url, headers=headers)
    questions_stats: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(questions_stats['statistics']['mathworld_total_count']).is_not_equal_to(num_of_mathword)

@pytest.mark.tc_011
def test_fetch_question_stats_college(get_admin_token):
    req: Requester = Requester()
    college_returned: list = execute_query(
        f"SELECT COUNT(*) FROM mathworld.question WHERE question_type = 'College Level' AND status = 'Rejected'")
    num_of_college: int = college_returned[0][0]
    headers: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/fetch/question_statistics"
    response = requests.request("GET", url, headers=headers)
    questions_stats: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(questions_stats['statistics']['mathworld_total_count']).is_not_equal_to(num_of_college)

@pytest.mark.tc_012
def test_fetch_question_stats_mathworld(get_admin_token):
    req: Requester = Requester()
    mathworld_returned: list = execute_query(
        f"SELECT COUNT(*) FROM mathworld.question WHERE question_type = 'MathWorld' AND status = 'Reported'")
    num_of_mathword: int = mathworld_returned[0][0]
    headers: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/question/fetch/question_statistics"
    response = requests.request("GET", url, headers=headers)
    questions_stats: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(questions_stats['statistics']['mathworld_total_count']).is_not_equal_to(num_of_mathword)
