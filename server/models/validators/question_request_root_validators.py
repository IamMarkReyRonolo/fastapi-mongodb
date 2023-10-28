from fastapi import HTTPException, status
from datetime import datetime
import re
from server.models.validators.question_class_enum import (
    TypeEnum,
    ResponseEnum,
    StatusEnum,
    ClassificationEnum,
    DifficultyEnum
)


def validate_staar_fields(cls, values):
    values = is_not_empty(cls, values)
    values = validate_missing_staar_keys(cls, values)
    values['question_type'] = is_type_match(values['question_type'], "STAAR")
    values['grade_level'] = validate_grade_level(values["grade_level"])
    values['release_date'] = validate_release_date(values['release_date'])
    values['category'] = validate_category(values['category']) # affected
    values['keywords'] = validate_keywords(values['keywords'])
    values['student_expectations'] = validate_student_expectations(
        values['student_expectations']) # affected
    values['response_type'] = set_response_type(values['response_type'])
    values['question_content'] = validate_question_content(
        values['question_content'])
    values['question_img'] = set_image(values['question_img'])
    return values


def validate_college_fields(cls, values):
    values = is_not_empty(cls, values)
    values = validate_missing_college_keys(cls, values)
    values['classification'] = set_classification_type(
        values['classification'])
    values['test_code'] = validate_test_code(values['test_code'])
    values['question_type'] = is_type_match(
        values['question_type'], "College Level")
    values['keywords'] = validate_keywords(values['keywords'])
    values['response_type'] = set_response_type(values['response_type'])
    values['question_content'] = validate_question_content(
        values['question_content'])
    values['question_img'] = set_image(values['question_img'])
    return values


def validate_mathworld_fields(cls, values):
    values = is_not_empty(cls, values)
    values = validate_missing_mathworld_keys(cls, values)
    values['question_type'] = is_type_match(
        values['question_type'], "MathWorld")
    values['grade_level'] = validate_grade_level(values["grade_level"])
    values['category'] = validate_category(values['category'])
    values['topic'] = validate_topic(values['topic'])
    values['teks_code'] = validate_teks_code(values['teks_code'])
    values['subject'] = validate_subject(values['subject'])
    values['difficulty'] = validate_difficulty(values['difficulty'])
    values['keywords'] = validate_keywords(values['keywords'])
    values['student_expectations'] = validate_student_expectations(
        values['student_expectations'])
    values['points'] = validate_points(values["points"], values['difficulty'])
    values['response_type'] = set_response_type(values['response_type'])
    values['question_content'] = validate_question_content(
        values['question_content'])
    values['question_img'] = set_image(values['question_img'])
    return values


def validate_option_fields(cls, values):
    values = is_not_empty(cls, values)
    values = validate_missing_option_keys(cls, values)
    values['content'] = validate_option_content(values['content'])
    values['unit'] = validate_unit(values['unit'])
    values['letter '] = validate_option_letter(values['letter'])
    values['is_answer'] = validate_is_answer(values['is_answer'])
    values['image'] = set_option_image(values['image'])
    return values


def validate_updated_question_fields(cls, values):
    values = validate_missing_update_keys(cls, values)
    values['update_note'] = validate_update_note(values['update_note'])
    return values


def validate_updated_status_fields(cls, values):
    # values['update_note'] = validate_update_note(values['update_note'])
    values['status'] = validate_question_status(values['status'])
    values = validate_missing_update_keys(cls, values)
    return values


# individual validators

def is_not_empty(cls, values):
    for attr, value in values.items():
        if(attr == "question_img" or attr == "image" or attr == 'unit' or attr == 'created_by' or attr == 'updated_by'):
            continue
        else:
            if(value == ""):
                raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail=attr + " is required")
    return values


def validate_missing_staar_keys(cls, values):

    keys = values.keys()
    required_keys = ["question_type", "grade_level", "release_date", "category",
                     "keywords", "student_expectations", "response_type", "question_content"]
    for key in required_keys:
        if (key not in keys):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail=key + " is required")
    return values


def validate_missing_college_keys(cls, values):

    keys = values.keys()
    required_keys = ["question_type", "classification",
                     "test_code", "keywords", "response_type", "question_content"]
    for key in required_keys:
        if (key not in keys):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail=key + " is required")
    return values


def validate_missing_mathworld_keys(cls, values):

    keys = values.keys()
    required_keys = ["question_type", "grade_level", "teks_code", "subject", "topic", "category",
                     "keywords", "student_expectations", "difficulty", "points", "response_type", "question_content"]
    for key in required_keys:
        if (key not in keys):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail=key + " is required")
    return values


def validate_missing_option_keys(cls, values):
    keys = values.keys()
    required_keys = ["letter", "content", "is_answer"]
    for key in required_keys:
        if (key not in keys):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail=key + " is required in option object")
    return values


def validate_missing_update_keys(cls, values):
    keys = values.keys()
    required_keys = []

    if 'status' not in keys or ('status' in keys and values['status'] in ['Rejected', 'Reported']):
        required_keys = ["update_note"]
    
    for key in required_keys:
        if (key not in keys):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail=key + " is required")
    return values


def validate_category(v):
    if(str(type(v)) == "<class 'str'>"):
        v = v.strip()
        if(v == ""):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="category should not be empty")
        if v not in ['1', '2', '3', '4', '5']:
                raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Valid category is from 1 to 5")
        
        return v
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="category must be a string")
    
def validate_topic(v):
    if(str(type(v)) == "<class 'str'>"):
        v = v.strip()
        if(v == ""):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="topic should not be empty")
        
        return v
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="topic must be a string")

def validate_grade_level(v):
    if(str(type(v)) == "<class 'int'>"):
        if(v > 12 or v < 3):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="invalid grade level: should only be between 3 to 12")
        return v
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="grade level must be an integer")


def validate_points(v, difficulty):
    if(str(type(v)) == "<class 'int'>"):
        if(v > 100 or v < 1):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="invalid points value: should only be between 1 to 3")
        match difficulty:
            case "Easy":
                if v != 1:
                    raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="Difficulty level is incompatible with points assigned.")
            case "Average":
                if v != 2:
                    raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="Difficulty level is incompatible with points assigned.")
            case "Hard":
                if v != 3:
                    raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="Difficulty level is incompatible with points assigned.")
        return v
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="points must be an integer")


def validate_subject(v):
    if(str(type(v)) == "<class 'str'>"):
        v = v.strip()
        if(v == ""):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="subject should not be empty")
        
        if v not in ['Algebra I', 'Algebra II', 'Geometry','Pre-Calculus']:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Invalid Subject")
        return v
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="subject must be a string")


def validate_keywords(v):
    if(str(type(v)) == "<class 'list'>"):
        if len(v) > 10:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="Max number of keywords reached")
        if(len(v) > 0):
            for value in v:
                if(str(type(value)) == "<class 'str'>"):
                    if(value.strip() == ""):
                        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                            detail="a value in keywords should not be an empty string")
                else:
                    raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                        detail="all values in keywords must be string")
                if len(value) > 50:
                    raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="Max length of keyword reached")
            return v
        else:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="keywords must not be empty")
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="keywords must be a list")


def validate_student_expectations(v):
    if(str(type(v)) == "<class 'list'>"):
        if(len(v) > 0):
            for value in v:
                if(str(type(value)) == "<class 'str'>"):
                    if(value.strip() == ""):
                        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                            detail="student_expectations should not be an empty string")
                else:
                    raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                        detail="student_expectations must be a string")
                value = value.strip()
                if(value not in ["A.1(A)","A.1(B)","A.1(C)","A.1(D)","A.1(E)","A.1(G)",
                                "A.2(A)","A.2(B)","A.2(C)","A.2(D)","A.2(E)","A.2(F)","A.2(G)","A.2(H)","A.2(I)",
                                "A.3(A)","A.3(B)","A.3(C)","A.3(D)","A.3(E)","A.3(F)","A.3(G)","A.3(H)",
                                "A.4(A)","A.4(B)","A.4(C)","A.5(A)","A.5(B)","A.5(C)",
                                "A.6(A)","A.6(B)","A.6(C)",
                                "A.7(A)","A.7(B)","A.7(C)",
                                "A.8(A)","A.8(B)",
                                "A.9(A)","A.9(B)","A.9(C)","A.9(D)","A.9(E)",
                                "A.10(A)","A.10(B)","A.10(C)","A.10(D)","A.10(E)","A.10(F)",
                                "A.11(A)","A.11(B)",
                                "A.12(A)","A.12(B)","A.12(C)","A.12(D)","A.12(E)",]):
                    raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                        detail="Invalid student expectations")


            return v
        else:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="student_expectations must not be empty")
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="student_expectations must be a list")


def validate_question_content(v):
    if(str(type(v)) == "<class 'str'>"):
        if(v.strip() == ""):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="question content should not be empty")
        if(len(v.strip()) > 1000):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="question content should not exceed 1000 characters")
        return v
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="question content must be a string")


def validate_release_date(v):
    if(str(type(v)) == "<class 'str'>"):
        if(v.strip() == ""):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="release date should not be empty")

        pattern = "^(?:\d{4}-\d{2})$"
        is_matched = re.match(pattern, v)

        if(not is_matched):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="release date invalid format: format accepted xxxx-xx | year-month")

        dates = v.split("-")
        today = datetime.now()
        if(int(dates[0]) > today.year and int(dates[1]) > today.month):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="release date invalid - date should not be in future")

        return v

    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="release date must be a string")


def set_response_type(v):
    if(str(type(v)) == "<class 'str'>"):
        v = v.strip().title()
        if(v in [response.value for response in ResponseEnum]):
            return v
        else:
            if v == "":
                raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="response_type should not be an empty string")
            else:
                raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="invalid response type")
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="response_type must be a string")


def is_type_match(v, question_type):
    if(str(type(v)) == "<class 'str'>"):
        if question_type == "STAAR":
            v = v.strip().upper()
            if(v == question_type and v in [q_type.value for q_type in TypeEnum]):
                return v
            else:
                raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="question type must match to the endpoint use: " + question_type)
        else:
            v = v.strip().title()
            if(v == question_type.title() and v in [q_type.value for q_type in TypeEnum]):
                return v
            else:
                raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="question type must match to the endpoint use: " + question_type)

    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="question_type must be a string")


def set_image(v):
    if(str(type(v)) == "<class 'str'>"):
        if(len(v) > 0):
            if(len(v.strip()) == ""):
                raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="question image value not allowed")

            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="invalid image insertion: image must be added through the Form, not in payload.")
        return v
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="image must be a string")


def validate_test_code(v):
    if(str(type(v)) == "<class 'str'>"):
        if(len(v) > 6):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="test code must not exceed 6 characters")
        return v
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="test code must be a string")


def set_classification_type(v):
    if(str(type(v)) == "<class 'str'>"):
        v = v.strip().upper()
        if(v in [classification.value for classification in ClassificationEnum]):
            return v
        else:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="invalid classification type")
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="classification value must be a string")


def validate_teks_code(v):
    if(str(type(v)) == "<class 'str'>"):
        v = v.strip()
        if(len(v) > 6):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="teks code must not exceed 6 characters")
        if(v not in ['A.1','A.2', 'A.3', 'A.4', 'A.5', 'A.6', 'A.7','A.8', 'A.9', 'A.10', 'A.11', 'A.12']):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Invalid Teks Code")
        return v
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="teks code must be a string")


def validate_difficulty(v):
    if(str(type(v)) == "<class 'str'>"):
        v = v.strip().title()
        if(v in [difficulty.value for difficulty in DifficultyEnum]):
            return v
        else:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="invalid difficulty level")
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="difficulty value must be a string")


def validate_option_content(v):
    print(v)
    if(str(type(v)) == "<class 'str'>"):
        if(v.strip() == ""):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="option content should not be empty")
        if(len(v.strip()) > 1000):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="option content should not exceed 1000 characters")
        return v
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="option content must be a string")


def validate_unit(v):
    if(v):
        if(str(type(v)) == "<class 'str'>"):
            if(len(v) != 0):
                if(v.strip() == ""):
                    raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                        detail="unit should not be all whitespaces")
                if(len(v.strip()) > 20):
                    raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                        detail="unit content should not exceed 20 characters")
            return v.strip()
        else:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="unit must be a string")

    return v.strip()


def validate_option_letter(v):
    if(str(type(v)) == "<class 'str'>"):
        if(v.strip() == ""):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="option letter should not be empty")
        if(len(v.strip()) > 1):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="option letter should only be 1 character long")
        return v.strip()
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="option lettter must be a string")


def validate_is_answer(v):
    if(str(type(v)) == "<class 'bool'>"):
        return v
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="is_answer should be type boolean")


def set_option_image(v):
    if(str(type(v)) == "<class 'str'>"):
        if(len(v) > 0):
            if(len(v.strip()) == ""):
                raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="option image value not allowed")

            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="invalid option image insertion: image must be added through the Form, not in payload.")
        return v
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="image must be a string")


def validate_update_note(v):
    if v:
        if v.strip() == "":
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="update_note is required")

    return v


def validate_question_status(v):
    v = v.strip().title()
    if(v in [status.value for status in StatusEnum]):
        return v.title()
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="invalid status")
