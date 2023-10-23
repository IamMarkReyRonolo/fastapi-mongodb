import pdb, sys, os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
WORKING_DIR = os.path.abspath(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
from faker import Faker
import random
import logging as logger

fake = Faker()

def create_member_data(domain="QA", prefix="test_") -> dict:
    logger.debug("Generate random member data")
    roles = ["Student", "Teacher", "Faculty", "Administrator"]
    gender = ["Male", "Female", "Other", "Private"]
    member: dict = {}
    random_num: int = random.randint(10, 10000)

    member["first_name"] = fake.first_name()
    member["middle_initial"] = "a"
    member["last_name"] = fake.last_name()  
    member["mw_role"] =   roles[random.randrange(0, len(roles))]
    member["email"] = f'{prefix}{member["first_name"]}.{member["last_name"]}{random_num}@gmail.com'
    member["gender"] =   gender[random.randrange(0, len(gender))]
    member["mw_password"] = f'{member["last_name"]}_{member["first_name"]}!2022'
    logger.debug(f"Generate random member data: {member}")
    return  member
