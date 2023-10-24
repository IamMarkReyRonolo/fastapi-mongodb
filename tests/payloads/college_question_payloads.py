import lib.common as common

def get_valid_successful_college_payload():
    return {
        "question_type": "College Level",
        "classification": "SAT",
        "test_code": "123456",
        "keywords": ["2"], \
        "response_type": "Open Response Exact",
        "question_content": common.get_random_question(),
        "question_img": "",
        "options": [
            {
            "letter": "a",
            "content": common.get_random_question(),
            "image": "",
            "unit": "pound",
            "is_answer": True
            }
        ]
    }