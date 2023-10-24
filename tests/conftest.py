import sys, os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
WORKING_DIR = os.path.abspath(CURRENT_DIR)
PARENT_DIR = os.path.join(CURRENT_DIR, '..')
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)
import pytest
from lib.fake_data import create_member_data

@pytest.fixture(scope='function')
def member_data():
    payload: dict = create_member_data()
    return payload

@pytest.fixture(scope='function')    
def expired_token():
    return { "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImhlbHBAZXhhbXBsZS5jb20iLCJleHAiOjE2NjExMzQ4MTN9.QW6TRONFqO4KOZfajIVck3Mgjk3fJpZeAO4IsDguiy8" }
