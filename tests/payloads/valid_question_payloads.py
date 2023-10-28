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

def get_valid_successful_mathworld_payload():
    return {
        "question_type": "MathWorld",
        "grade_level": 3,
        "teks_code": "A.1",
        "subject": "Algebra I",
        "topic": "quantity",
        "category": "1",
        "keywords": ["happy"],
        "student_expectations": ["A.1(A)"],
        "difficulty": "easy",
        "points": 1,
        "response_type": "Open Response Exact",
        "question_content": common.get_random_question(),
        "question_img": "",
        "options": [
            { 
            "letter": "a",
            "content": common.get_random_question(),
            "image": "",
            "unit": common.get_random_unit(),
            "is_answer": True
            } 
        ] 
        }

def get_valid_successful_staar_payload():
    return { 
      "question_type": "STAAR", 
      "grade_level": 3, 
      "release_date": "2024-02", 
      "category": "1", 
      "keywords": ["math"], 
      "student_expectations": ["A.1(A)"], 
      "response_type": "Open Response Exact", 
      "question_content": common.get_random_question(), 
      "question_img": "", 
      "options": [ 
        { 
          "letter": "a", 
          "content": common.get_random_question(), 
          "image": "", 
          "unit": "pounds", 
          "is_answer": True 
        }, 
        { 
          "letter": "b", 
          "content": common.get_random_question(), 
          "image": "", 
          "unit": "pounds", 
          "is_answer": False 
        } 
      ] 
    }
    