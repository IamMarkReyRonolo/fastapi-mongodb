import string, random, json, os, sys

import requests
CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
from random import random
import logging as logger
from apiclient import APIClient
from tests.lib.requester import Requester
from requester import Requester
from generate_token import get_token
from uuid import UUID
import uuid
from faker import Faker
from json_compare import Jcompare
import tests.lib
import datetime
import random
import string
import lib.generate_token as generate_token
import lib.common as common
from datetime import datetime, timedelta

fake = Faker()
cp = Jcompare()

def create_a_member(payload):
    req = Requester()
    response: object = req.post('/member/create', payload)
    token: dict = get_token()
    headers: dict = { "Authorization": f"Bearer {token['access_token']}" }
    member: dict = json.loads(response.text)
    return member

def random_string(width):
    return ''.join(random.choice(string.ascii_uppercase + string.digits))

def create_header():
    token: dict = get_token()
    headers: dict = {   "Authorization": f"Bearer {token['access_token']}",
                        "Content-Type": "application/json"
                    }
    return headers

def set_image_file(file_path: str, file_name: str) -> list:
    image_file: list = []
    try:
        file_image_split: list = file_name.split(".")
        image_file: list = [
                (f'{file_image_split[0]}',(f'{file_name}',open(f'{tests.CURRENT_DIR}\\tests\\images\\{file_name}','rb'),f'image/{file_image_split[1]}'))
            ]
    except Exception as e:
        pass
    return image_file

def radom_gender():
    gender: list = ['Male', 'Female', 'Other']
    return random.choice(gender)

def random_role():
    roles: list = ['staff', 'admin', 'subscriber']
    return random.choice(roles)

def current_date_time():
    now = datetime.utcnow()
    formatted_date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    return formatted_date

def create_fake_payload():
    fist_name: str = fake.first_name()
    middle_initial: str = random.choice(string.ascii_letters)
    last_name: str = fake.last_name()
    email: str = f"{fist_name}{last_name}!2022@gmail.com"
    passwrd: str = f"{fist_name}{last_name}!2022@passWord"
    gender: list = ['Male', 'Female', 'Other']

    payload_str = json.dumps({
                "first_name": f"{fist_name}",
                "middle_initial": f"{middle_initial}",
                "last_name": f"{last_name}",
                "mw_role": f"{random_role()}",
                "email": f"{email}",
                "mw_password": f"{passwrd}",
                "gender": f"{random.choice(gender)}"
            })
    return payload_str

def create_fake_register():
    fist_name: str = fake.first_name()
    middle_initial: str = random.choice(string.ascii_letters)
    last_name: str = fake.last_name()
    role: str = random.choice(['admin', 'staff'])
    school: str = fake.state() + "State High School"
    email: str = f"{fist_name}{last_name}!2022@gmail.com"
    passwrd: str = f"{fist_name}{last_name}!2022@passWord"
    repeat_password: str = passwrd
    created_by: str = f"{'first_name'} {'last_name'} "
    payload_str = json.dumps({
                "first_name": f"{fist_name}",
                "middle_name": f"{middle_initial}",
                "last_name": f"{last_name}",
                "role": f"{role}",
                "school": f"{school}",
                "email": f"{email}",
                "password": f"{passwrd}",
                "repeat_password": f"{repeat_password}",
                "created_by": "John Doe"
            })
    return payload_str

def assert_unprocessalbe_entity(response, msg: str):
    response_message_dict = json.loads(response.text)
    assert response.status_code == 422
    assert response_message_dict['detail'][0]['msg'] == msg

def assert_ok(response, msg: str):
    response_message_dict = json.loads(response.text)
    assert response.status_code == 202
    assert response_message_dict['guid'] != ""
    assert response_message_dict['status'] == msg

def make_put_request(guid: dict, payload_str: str):
    headers: dict = create_header()
    req = Requester()
    response = req.mw_put(endpoint=f'member/update/{guid}', payload=payload_str, headers=headers)
    return response

def remote_item(guid: str, withHeader = True):
    if withHeader:
        headers: dict = create_header()
    else:
        headers: dict = {}
    req = Requester()
    response = req.mw_remove(endpoint=f'member/delete/{guid}', headers=headers)
    return response

def fetching_member_to_update(member_data)-> dict:
    member_to_update: dict = create_a_member(member_data)
    headers: dict = create_header()
    req = Requester()
    fetched_member_to_update  = req.mw_get(f"member/fetch/{member_to_update['guid']}", headers=headers )
    return { "member": fetched_member_to_update, "guid": member_to_update['guid'] }

def fetch_member(guid: str):
    headers: dict = create_header()
    req = Requester()
    response = req.mw_get(f"member/fetch/{guid}", headers=headers)
    return response

def assert_json_compare(expected_json: dict, actual_json: dict):
    if 'guid' in actual_json.keys():
        del actual_json['guid']
    if 'mw_password' in expected_json.keys():
        del expected_json['mw_password']
    assert cp.compare(expected_json, actual_json) == True

def assert_invalid_credentials(response, msg):
    response_message_dict = json.loads(response.text)
    assert response.status_code == 403
    assert response_message_dict['detail'] == msg

def verify_not_created(response, expected_status_code: int, expected_type: str, expected_message: str):
    response_json: dict = json.loads(response.content.decode('utf-8'))
    assert response.status_code == expected_status_code
    assert response_json['detail'][0]['type'] == expected_type
    assert response_json['detail'][0]['msg'] == expected_message

def verify_created(response):
    response_json: dict = json.loads(response.content.decode('utf-8'))
    assert response_json["status"] == 'OK'
    assert str(type(UUID(response_json["guid"]))) == "<class 'uuid.UUID'>"

def verify_detail_response(response, expected_status_code: int, expected_type: str, expected_message: str):
    if  response.status_code != 409:
        response_json: dict = json.loads(response.content.decode('utf-8'))
        assert response_json['detail'][0]['type'] == expected_type
        assert response_json['detail'][0]['msg'] == expected_message

def count_items(json_data: str = "", item_key: str = "", item_value: str = "") -> int:
    count: int = 0
    try:
        data = json.loads(json_data)
        for item in data['data']:
            if item[item_key] == item_value:
                count += 1
    except RuntimeError as error:
        pass
    return count

def is_valid_uuid(uuid_to_test, version=4) -> bool:
    result: bool
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
        result = str(uuid_obj) == uuid_to_test
    except ValueError:
        result = False
    return result

def get_current_yyyy_mm():
    try:
        current_date = datetime.now().date()
        return str(current_date.strftime("%Y-%m"))
    except Exception as e:
        pass

def get_future_yyyy_mm(bydays: int = 30) -> str:    
    current_date = datetime.now().date()
    return str((current_date + timedelta(days=bydays)).strftime("%Y-%m"))

def get_past_yyyy_mm(bydays: int = 30) -> str:        
    current_date = datetime.now().date()
    return str((current_date - timedelta(days=bydays)).strftime("%Y-%m"))
            
def create_random_string_width(int: int) -> str:
    return ''.join(random.choice(string.ascii_letters) for _ in range(int))

def random_name() -> str:
    return fake.name()

def random_email() -> str:
    first_name: str = fake.first_name()
    last_name: str = fake.last_name()
    email_address: str = first_name + last_name + "@gmail.com"
    return email_address

def chop_string(input_string: str, max_length: int = 25) -> str:
    truncated_string: str = input_string
    if len(input_string) > max_length:
        truncated_string: str = input_string[-max_length:]
    return truncated_string
        
def current_date() -> str:
     from datetime import datetime
     current_datetime: datetime = datetime.now()
     formatted_datetime: str = current_datetime.isoformat(timespec='milliseconds') + 'Z'
     return formatted_datetime

def get_random_question() -> str:
    question_start: list = ["What is", "How many", "When did", "Who was", "Where is", "What happened to"]
    question_end: list = ["the capital of", "the population of", "the birth year of", "the inventor of", "the tallest building in"]

    start: str = fake.random_element(question_start)
    end: str = fake.random_element(question_end)

    if end == "the capital of":
        question: str = f"{start} {end} {fake.country()}?"
    elif end == "the population of":
        question: str = f"{start} {end} {fake.city()}?"
    elif end == "the birth year of":
        question: str = f"{start} {end} {fake.name()}?"
    elif end == "the inventor of":
        question: str = f"{start} {end} {fake.catch_phrase()}?"
    else:
        question: str = f"{start} {end} {fake.city()}?"
    return question

def get_random_tek_code() -> str:
    tek_code: str = fake.random_element(["A.1", "A.2", "A.3", "A.4", "A.5", "A.6"])
    return tek_code

def get_random_unit() -> str:
    unit: str = fake.random_element(["kg", "lb", "oz", "g", "mg", "t", "st", "gr"])
    return unit

def get_random_char(length: int) -> str:
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def generate_random_sentence(length: int) -> str:
    words: list = ['you', 'side', 'tonight', 'idiot', 'want', 'conservative', 'going', 'she', 'know', 'do', 'fever', 'weight lift', 'fat ass', 'got to go', 'give', 'door', 'find', 'make me', 'pre-billing']
    sentence: str = ' '.join(random.choice(words) for _ in range(length))
    return sentence.capitalize() + '.'

def replace_numbers_with_zero(input_string: str) -> str:
    result = ""
    for char in input_string:
        if char.isdigit():
            result += "0"
        else:
            result += char
    return result

def random_school() -> str:
    state: str = fake.state
    school: str = fake.state() + " State High School"
    return school

def get_admin_token() -> str:
    token: str = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    return token

def get_staff_token() -> str:
    token: str = generate_token.generate_token(email="staffABC@gmail.com", password="Staff123!")
    return token

def get_staar_random_payload_data()  -> dict:
    random_month = str (random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']))
    random_date = "2024-" + str(random_month)
    random_response_type: str = random.choice(['Open Response Exact', 'Range Open Response', 'Multiple Choice', 'Checkbox'])
    random_question_type: str = random.choice(['STAAR', 'College Level', 'MathWord'])
    random_grade_level: int = random.choice([3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    random_letter: str = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    random_unit: str = random.choice(['pounds', 'kilograms', 'meters', 'centimeters', 'inches', 'feet', 'yards', 'miles', 'grams', 'liters'])
    random_is_answer: bool = random.choice([True, False])
    random_category: str = random.choice(['1', '2', '3', '4', '5'])
    random_keyword: str = random.choice(['math', 'science', 'history', 'english', 'spanish', 'french', 'german', 'italian', 'chinese', 'japanese'])
    random_student_expectation: str = random.choice(['A.1(A)', 'A.1(B)', 'A.1(C)', 'A.1(D)', 'A.1(E)', 'A.1(F)', 'A.1(G)'])
    random_question_content: str = get_random_question()
    random_payload: dict = {  "random_month": random_month, "random_date": random_date, "random_response_type": random_response_type, \
                        "random_question_type": random_question_type, "random_grade_level": random_grade_level, \
                        "random_letter": random_letter, "random_unit": random_unit, "random_is_answer": random_is_answer, \
                        "random_category": random_category, "random_keyword": random_keyword, "random_student_expectation": random_student_expectation, \
                        "random_question_content": random_question_content }
    return random_payload

def get_mathworld_random_payload_data() -> dict:
    random_month = str (random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']))
    random_date = "2024-" + str(random_month)
    random_response_type: str = random.choice(['Open Response Exact', 'Range Open Response', 'Multiple Choice', 'Checkbox'])
    random_question_type: str = random.choice(['STAAR', 'College Level', 'MathWord'])
    random_grade_level: int = random.choice([3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    random_student_expectation: str = random.choice(['A.1(A)', 'A.1(B)', 'A.1(C)', 'A.1(D)', 'A.1(E)', 'A.1(F)', 'A.1(G)'])
    random_letter: str = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    random_unit: str = random.choice(['pounds', 'kilograms', 'meters', 'centimeters', 'inches', 'feet', 'yards', 'miles', 'grams', 'liters'])
    random_topic: str = random.choice(['Algebra 1', 'Algebra 2', 'Algebra 3', 'Geometry 1', 'Chemistry II', 'Networking I', 'Logic II', 'Trigonometry I', 'Sharepoint I', 'Astrology 1'])
    random_subject: str = random.choice(['Math', 'Science', 'Social Studies', 'English', 'Spanish', 'French', 'German', 'Chinese', 'Japanese', 'Russian'])
    random_category: str = random.choice(['1', '2', '3', '4', '5'])
    random_difficulty: str = random.choice(['Easy','Average','Hard','Advance'])
    random_question_content: str = get_random_question()
    random_teks_code: str = get_random_tek_code()
    random_payload: dict = { "random_month": random_month, "random_date": random_date, "random_response_type": random_response_type \
                        , "random_question_type": random_question_type, "random_grade_level": random_grade_level, "random_student_expectations": random_student_expectation \
                        , "random_letter": random_letter, "random_unit": random_unit, "random_topic": random_topic \
                        , "random_subject": random_subject, "random_category": random_category, "random_difficulty": random_difficulty \
                        , "random_question_content": random_question_content, "random_teks_code": random_teks_code }
    return random_payload


def get_random_payload_data() -> dict:
    random_month = str (random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']))
    random_date = "2024-" + str(random_month)
    release_date: str = f"{get_current_yyyy_mm()}"
    random_sentence: str = generate_random_sentence(5)
    current_datetime: str = current_date()    
    random_category: str = random.choice(['1', '2', '3', '4', '5'])
    update_status: str = random.choice(['Approved', 'Pending', 'Rejected', 'Reported'])
    random_response_type: str = random.choice(['Open Response Exact', 'Range Open Response', 'Multiple Choice', 'Checkbox'])
    random_question_type: str = random.choice(['STAAR', 'College Level', 'MathWord'])
    random_classification: str = random.choice(['SAT', 'TSI', 'ACT'])
    random_name: str = fake.name()
    random_grade_level: int = random.choice([3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    random_student_expectation: str = random.choice(['A.1(A)', 'A.1(B)', 'A.1(C)', 'A.1(D)', 'A.1(E)', 'A.1(F)', 'A.1(G)'])
    random_letter: str = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    random_unit: str = random.choice(['pounds', 'kilograms', 'meters', 'centimeters', 'inches', 'feet', 'yards', 'miles', 'grams', 'liters'])
    random_topic: str = random.choice(['Algebra 1', 'Algebra 2', 'Algebra 3', 'Geometry 1', 'Chemistry II', 'Networking I', 'Logic II', 'Trigonometry I', 'Sharepoint I', 'Astrology 1'])
    random_subject: str = random.choice(['Algebra I', 'Algebra II', 'Geometry','Pre-Calculus'])    
    random_difficulty: str = random.choice(['Easy','Average','Hard','Advance'])
    random_question_content: str = get_random_question()
    random_teks_code: str = get_random_tek_code()
    random_payload: dict = { "random_month": random_month, "random_date": random_date, "random_response_type": random_response_type \
                        , "random_question_type": random_question_type, "random_grade_level": random_grade_level, "random_student_expectations": random_student_expectation \
                        , "random_letter": random_letter, "random_unit": random_unit, "random_topic": random_topic, "random_classification": random_classification \
                        , "random_subject": random_subject, "random_category": random_category, "random_difficulty": random_difficulty \
                        , "random_question_content": random_question_content, "random_teks_code": random_teks_code \
                        , "release_date": release_date, "random_sentence": random_sentence, "current_datetime": current_datetime \
                        , "update_status": update_status, "random_category": random_category, "random_name": random_name \
                        , "random_student_expectations": random_student_expectation }
    return random_payload


def create_a_staar_question(member_type: str, response_type: str = "Open Response Exact") -> dict:
    try:
        req = Requester()
        user_token: str = get_admin_token() if member_type == "admin" else get_staff_token()
        random_data: dict = get_staar_random_payload_data()
        header: dict = req.create_basic_headers(token=user_token)
        url: str = f"{req.base_url}/question/staar/create"
        payload: dict = {'data': '{"question_type": "STAAR", "update_note": "'+ random_data['random_question_content'] +'", "grade_level": 3, "release_date": "2023-05", "category": "' + random_data['random_category'] + '","keywords": ["math"], "student_expectations": ["'+ random_data['random_student_expectation'] +'"],"response_type": "' + response_type + '","question_content": "'+ random_data['random_question_content'] + '","question_img": "","options": [{"letter": "' + random_data['random_letter'] + '","content": "'+ random_data['random_question_content'] +'","image": "","unit": "pounds","is_answer": true},{"letter": "' + random_data['random_letter'] + '","content": "option b","image": "","unit": "pounds","is_answer": false}]}'}
        response = requests.request("POST", url, headers=header, data=payload)
        new_staar_questions: dict = json.loads(response.text)
    except Exception as e:
        return { "error": -1, "message": e}
    return new_staar_questions

def create_a_mathworld_question(member_type: str, response_type: str = "Open Response Exact") -> dict:
    try:
        req = Requester()
        user_token: str = get_admin_token() if member_type == "admin" else get_staff_token()
        random_data: dict = get_random_payload_data()
        header: dict = req.create_basic_headers(token=user_token)
        question2: str = common.get_random_question()
        url: str = f"{req.base_url}/question/mathworld/create"
        upload_file: list = []
        difficulty: dict = {"Easy": 1, "Average": 2, "Hard": 3}
        
        random_payload: dict = {'data': '{ \
        "question_type": "MathWorld", \
        "grade_level": 3, \
        "teks_code": "' + random_data['random_teks_code'] +'", \
        "subject": "' +  random_data['random_subject'] +'", \
        "topic": "' + random_data['random_topic'] +'", \
        "category": "' + random_data['random_category'] +'", \
        "keywords": ["happy"], \
        "student_expectations": ["' + random_data['random_student_expectations'] +'"], \
        "difficulty": "Easy", \
        "points": 1, \
        "response_type": "' + response_type  +'", \
        "question_content": "' + random_data['random_question_content'] +'", \
        "question_img": "", \
        "options": [ \
            { \
            "letter": "' + random_data['random_letter'] +'", \
            "content": "' + question2 + '", \
            "image": "", \
            "unit": "' + random_data['random_unit'] + '", \
            "is_answer": true \
            } \
        ] \
        }'}

        upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
        response = requests.request("POST", url, headers=header, data=random_payload, files=upload_file)
        json_response: dict = json.loads(response.text)
        return json_response
    except Exception as e:
        return { "error": -1, "message": e}

def create_a_college_question(member_type: str, response_type: str = "Open Response Exact") -> dict:
    try:
        req = Requester()
        user_token: str = get_admin_token() if member_type == "admin" else get_staff_token()
        random_data: dict = get_random_payload_data()
        header: dict = req.create_basic_headers(token=user_token)
        question2: str = common.get_random_question()
        url: str = f"{req.base_url}/question/college/create"
        upload_file: list = []

        random_payload: dict = {'data': '{ \
                "question_type": "College Level", \
                "classification": "' + random_data['random_classification'] +'", \
                "test_code": "123456", \
                "keywords": ["2"], \
                "response_type": "' + response_type + '", \
                "question_content": "' + question2 + '", \
                "question_img": "", \
                "options": [ \
                    { \
                    "letter": "' + random_data['random_letter'] + '", \
                    "content": "' + question2 + '", \
                    "image": "", \
                    "unit": "' + random_data['random_unit'] + '", \
                    "is_answer": true \
                    } \
                ] \
                }'}

        upload_file: list = []
        response = requests.request("POST", url, headers=header, data=random_payload, files=upload_file)
        json_response: dict = json.loads(response.text)
        return json_response
    except Exception as e:
        return { "error": -1, "message": e}

def update_question_status(uuid: str = "", status: str = "Pending") -> dict:
    try:
        req = Requester()
        user_token: str = get_admin_token()
        header: dict = req.create_basic_headers(token=user_token)
        random_data: dict = common.get_random_payload_data()
        patch_url: str = f"{req.base_url}/question/update/question_status/{uuid}"
        patch_payload: str = json.dumps({
            "status":  status,
            "update_note": f"{random_data['random_sentence']}",
            "reviewed_by": f"{random_data['random_name']}",
            "reviewed_at": f"{random_data['current_datetime']}"
    })
        patch_response = requests.request("PATCH", patch_url, headers=header, data=patch_payload)
        json_patch_response: dict = json.loads(patch_response.text)
        return json_patch_response
    except Exception as e:
        return { "error": -1, "message": e}

def register_staff_member() -> dict:
    req = Requester()
    user_token: str = get_admin_token()
    random_data: dict = json.loads(common.create_fake_register())
    random_data['password']= "Staff123!"    
    payload: dict = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "'+ random_data['password'] +'", "repeat_password": "'+ random_data['password'] +'", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=user_token)
    url: str = f"{req.base_url}/staff/register"
    response: requests.models.Response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response: dict = json.loads(response.text)
    return json_response

