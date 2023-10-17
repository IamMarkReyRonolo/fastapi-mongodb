from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, model_validator, validator, Field
from beanie import Document

from server.models.validators.question_request_root_validators import (
    validate_staar_fields, 
    validate_college_fields, 
    validate_mathworld_fields, 
    validate_option_fields, 
    validate_updated_question_fields, 
    validate_updated_status_fields
)


class Option(BaseModel):
    letter: str
    content: str
    image: Optional[str]
    unit: Optional[str]
    is_answer: bool
    _validate_fields = model_validator(mode='before')(validate_option_fields)

class Question(Document):
    response_type: str
    question_content: str
    question_img: Optional[str]
    question_status: str = 'Pending'
    options: List[Option]
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    reviewed_by: Optional[str] = None
    reviewed_at: Optional[datetime] = None

    @validator('updated_at', pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()
    
    @validator('created_at', pre=True, always=True)
    def set_created_at_now(v):
        return v or datetime.utcnow()

    class Settings:
        name = "question_collection"

class StaarQuestion(Question):
    question_type: str
    grade_level: int
    release_date: str
    category: str
    student_expectations: List[str]
    keywords: List[str]
    _validate_fields = model_validator(mode='before')(validate_staar_fields)


class CollegeQuestion(Question):
    question_type: str
    classification: str
    test_code: str
    keywords: List[str]
    _validate_fields =model_validator(mode='before')(validate_college_fields)


class MathworldQuestion(Question):
    question_type: str
    grade_level: int
    teks_code: str
    subject: str
    topic: str
    category: str
    student_expectations: List[str]
    keywords: List[str]
    difficulty: str
    points: int
    _validate_fields =model_validator(mode='before')(validate_mathworld_fields)


class UpdatedStaarQuestion(StaarQuestion):
    update_note: str = Field(examples=["Foo"])
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    options: List[Option]
    _no_missing_update_fields =model_validator(mode='before')(validate_updated_question_fields)

    @validator('updated_at', pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()


class UpdatedCollegeQuestion(CollegeQuestion):
    update_note: str 
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    options: List[Option]
    _no_missing_update_fields =model_validator(mode='before')(validate_updated_question_fields)

    @validator('updated_at', pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()


class UpdatedMathworldQuestion(MathworldQuestion):
    update_note: str
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    options: List[Option]
    _no_missing_update_fields =model_validator(mode='before')(validate_updated_question_fields)

    @validator('updated_at', pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()


class UpdateQuestionStatus(BaseModel):
    status: str
    update_note: Optional[str] = None
    reviewed_by: Optional[str] = None
    reviewed_at: Optional[datetime] = None
    _validate_fields =model_validator(mode='before')(validate_updated_status_fields)

    @validator('reviewed_at', pre=True, always=True)
    def set_updated_at_now(cls, v):
        return v or datetime.utcnow()

    class Config:
        json_schema_extra = {
            "example": {
                "status": "Approved",
                "update_note": "Update message"
            }
        }
        
def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

# class SuccessCreatedQuestionModel(BaseModel):
#     return {
#         "data": [data],
#         "code": 200,
#         "message": message,
#     }

