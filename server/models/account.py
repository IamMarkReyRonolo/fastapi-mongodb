from enum import Enum
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, model_validator, validator, Field 
from bson import ObjectId
from beanie import Document, PydanticObjectId
from server.models.validators.accounts_validator import (
    validate_fields
)

class TypeEnum(str, Enum):
    staff = 'staff'
    admin = 'admin'
    subscriber = 'subscriber'

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

class Account(Document):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    role: str
    email: str
    password: str
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None

    @validator('updated_at', pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()
    
    @validator('created_at', pre=True, always=True)
    def set_created_at_now(v):
        return v or datetime.utcnow()
    
    class Settings:
        name = "account_collection"

class SubscriberAccount(Account):
    school: str
    

class LogIn(BaseModel):
    email: str
    password: str

    _validate_fields = model_validator(mode='before')(validate_fields)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "validemail@gmail.com",
                "password": "password",
            }
        }

class Registration(Account):
    school: Optional[str] = None
    repeat_password: str

    _validate_fields = model_validator(mode='before')(validate_fields)

    class Config:
        json_schema_extra = {
            "example": {
                "first_name": "John",
                'middle_name': "David",
                "last_name": "Doe",
                "role": "staff",
                "school": "this is optional (subscriber only)",
                "email": "validemail@gmail.com",
                "password": "Heyy123!",
                "repeat_password": "Heyy123!"
            }
        }

class UpdatedAccount(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    role: str
    email: str
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None

    @validator('updated_at', pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()
    

class UpdatedSubscriberAccount(UpdatedAccount):
    school: str

class UpdatedPassword(BaseModel):
    old_password: str
    new_password: str
    repeat_new_password: str
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None

    @validator('updated_at', pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()
    
    class Config:
        json_schema_extra = {
            "example": {
                "old_password": "Hello123!",
                'new_password': "HiBro567!",
                "repeat_new_password": "HiBro567!",
            }
        }

class AccountResponseModel(BaseModel):
    id: PydanticObjectId = Field(alias='_id')
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    role: str
    email: str
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None