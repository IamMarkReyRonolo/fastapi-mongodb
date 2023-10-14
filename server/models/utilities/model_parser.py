from bson import ObjectId, datetime
import json
from server.models.question import (
    StaarQuestion,
    CollegeQuestion,
    MathworldQuestion,
    UpdatedStaarQuestion,
    UpdatedCollegeQuestion,
    UpdatedMathworldQuestion
)


def question_parser(question):
    if question['question_type'].strip().upper() == 'STAAR':
        question = StaarQuestion.model_validate(question)
    elif question['question_type'].strip().title() == 'College Level':
        question = CollegeQuestion.model_validate(question)
    elif question['question_type'].strip().title() == 'Mathworld':
        question = MathworldQuestion.model_validate(question)
    return question

def updated_question_parser(question):
    if question['question_type'].strip().upper() == 'STAAR':
        question = UpdatedStaarQuestion.model_validate(question)
    elif question['question_type'].strip().title() == 'College level':
        question = UpdatedCollegeQuestion.model_validate(question)
    elif question['question_type'].strip().title() == 'Mathworld':
        question = UpdatedMathworldQuestion.model_validate(question)
    return question


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

def parse_response(result):
    result = json.loads(JSONEncoder().encode(result))
    return generate_response_payload(result)

def generate_response_payload(result):
    response_payload = []
    total_count = 0
    for res in result:
        question = {}
        item = {}
        # total_count = res['total_count']
        if res['question_type'] == 'STAAR':
            item['grade_level'] = res['grade_level']
            item['student_expectations'] = res['student_expectations']
            item['category'] = res['category']
            item['release_date'] = res['release_date']
            item['keywords'] = res['keywords']
        elif res['question_type'] == 'College Level':
            item['classification'] = res['classification']
            item['test_code'] = res['test_code']
            item['keywords'] = res['keywords']
        elif res['question_type'] == 'Mathworld':
            item['subject'] = res['subject']
            item['topic'] = res['topic']
            item['teks_code'] = res['teks_code']
            item['category'] = res['category']
            item['student_expectations'] = res['student_expectations']
            item['keywords'] = res['keywords']
            item['difficulty'] = res['difficulty']
            item['points'] = res['points']
        if item:
            question['id'] = res['_id']
            question['question_type'] = res['question_type']
            question['response_type'] = res['response_type']
            question['question_content'] = res['question_content']
            question['question_img'] = res['question_img']
            question['question_status'] = res['question_status']
            question['created_by'] = res['created_by']
            question['created_at'] = res['created_at']
            question['updated_by'] = res['updated_by']
            question['updated_at'] = res['updated_at']
            question['reviewed_by'] = res['reviewed_by']
            question['reviewed_at'] = res['reviewed_at']
            question['metadata'] = item
            question['options'] = res['options']
        response_payload.append(question)
    return response_payload

