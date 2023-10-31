from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, model_validator, validator, Field 
import re
import secrets
import string
from beanie import Document, PydanticObjectId, Indexed
from server.models.validators.accounts_validator import (
    validate_fields,
    validate_update_fields,
    password_must_be_valid
)


def is_not_empty(cls, values):
    for attr, value in values.items():
        if(attr == "middle_name" or attr == 'created_by' or attr == 'updated_by' or attr == "phone_number"):
            continue
        else:
            if(value == ""):
                raise ValueError(f'{attr} field should not be empty')

    return values


class User(Document):
    subscriber_id: str
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    role: str
    status: str
    email: Indexed(str, unique=True)
    password: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @validator('updated_at', pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()
    
    @validator('created_at', pre=True, always=True)
    def set_created_at_now(v):
        return v or datetime.utcnow()
    
    class Settings:
        name = "user_collection"
        indexes = [
            [("role", 1)]
        ]

class ContactPerson(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    relationship: str
    country: str
    state: str
    city: str
    street: str
    zip_code: str
    phone_number: Optional[str] = None

class OfficeDetails(BaseModel):
    location: str
    conference_time: Optional[str] = None
    phone_number: str

class Education(BaseModel):
    school: str
    degree: Optional[str] = None
    area_of_study: Optional[str] = None
    year_started: str
    year_ended: str

class Student(User):
    contact_person: ContactPerson

class Teacher(User):
    office_details: Optional[OfficeDetails] = None
    education: Optional[List[Education]] = None
    

class LogIn(BaseModel):
    email: str
    password: str

    @validator('email', pre=True, always=True)
    def check_email(cls, v):
        if v:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if(re.fullmatch(regex, v)):
                return v
            else:
                raise ValueError('email is invalid')
        else:
            raise ValueError('email field should not be empty')
    

    class Config:
        json_schema_extra = {
            "example": {
                "email": "validemail@gmail.com",
                "password": "password",
            }
        }

class Registration(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    role: str
    school: str
    email: str
    password: str
    repeat_password: str
    contact_person: Optional[ContactPerson]
    _no_empty_required_fields =model_validator(mode='before')(is_not_empty)
    _check_password = model_validator(mode='before')(password_must_be_valid)

    @validator('role')
    def check_role(cls, v):
        if v != "student":
            raise ValueError('role must be a student when creating a student account')
        
        return v
            

    @validator('email')
    def check_email(cls, v):
        if v:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if(re.fullmatch(regex, v)):
                return v
            else:
                raise ValueError('email is invalid')
        else:
            raise ValueError('email field should not be empty')

# class Registration(Account):
#     school: Optional[str] = None
#     repeat_password: str

#     _validate_fields = model_validator(mode='before')(validate_fields)

#     class Config:
#         json_schema_extra = {
#             "example": {
#                 "first_name": "John",
#                 'middle_name': "David",
#                 "last_name": "Doe",
#                 "role": "staff",
#                 "school": "this is optional (subscriber only)",
#                 "email": "validemail@gmail.com",
#                 "password": "Heyy123!",
#                 "repeat_password": "Heyy123!"
#             }
#         }

# class UpdatedAccount(BaseModel):
#     first_name: str
#     middle_name: Optional[str] = None
#     last_name: str
#     role: str
#     email: str
#     updated_by: Optional[str] = None
#     updated_at: Optional[datetime] = None
#     _validate_fields = model_validator(mode='before')(validate_update_fields)

#     @validator('updated_at', pre=True, always=True)
#     def set_updated_at_now(v):
#         return v or datetime.utcnow()
    

# class UpdatedSubscriberAccount(UpdatedAccount):
#     school: str

# class UpdatedPassword(BaseModel):
#     old_password: str
#     new_password: str
#     repeat_new_password: str
#     updated_by: Optional[str] = None
#     updated_at: Optional[datetime] = None
#     _validate_fields = model_validator(mode='before')(password_must_be_valid)

#     @validator('updated_at', pre=True, always=True)
#     def set_updated_at_now(v):
#         return v or datetime.utcnow()
    
#     class Config:
#         json_schema_extra = {
#             "example": {
#                 "old_password": "Hello123!",
#                 'new_password': "HiBro567!",
#                 "repeat_new_password": "HiBro567!",
#             }
#         }

class UserAccount(BaseModel):
    email: str
    role: str

class UserAccounts(BaseModel):
    accounts: List[UserAccount]

class UserResponseModel(BaseModel):
    id: PydanticObjectId = Field(alias='_id')
    subscriber_id: str
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    role: str
    status: str
    email: str
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None

class InitialUserAccountResponseModel(BaseModel):
    id: PydanticObjectId = Field(alias='_id')
    subscriber_id: str
    role: str
    status: str
    email: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class UpdatedUserViaSubscriber(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    email: str
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None

    @validator('updated_at', pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()
    
    class Config:
        json_schema_extra = {
            "example": {
                "first_name": "Peter",
                "middle_name": "John",
                "last_name": "James",
                "email": "peterjohnj@gmail.com"
            }
        }

class UpdatedRole(BaseModel):
    role: str
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None

    @validator('updated_at', pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()
    
    class Config:
        json_schema_extra = {
            "example": {
                "role": "teacher",
            }
        }

class UpdatedStatus(BaseModel):
    status: str
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None

    @validator('updated_at', pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()
    
    class Config:
        json_schema_extra = {
            "example": {
                "status": "active",
            }
        }

class ResetPassword(BaseModel):
    password: Optional[str] = None
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None

    @validator('updated_at', pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()
    
    @validator('password', pre=True, always=True)
    def generate_password(v):
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation.replace('"','')
        special_chars = special_chars.replace('"','').replace("'","").replace(".","")
        choices = letters + digits + special_chars
        v = ''
        for i in range(9):
            v += ''.join(secrets.choice(choices))
        
        return v
