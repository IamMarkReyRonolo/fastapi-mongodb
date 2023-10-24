question_payload={
                "staar_type_question": {
                    "summary": "Staar type question",
                    "description": "Create a staar type question",
                    "value":{
                        "question_type": "STAAR",
                        "grade_level": 3,
                        "release_date": "2023-12",
                        "category": "1",
                        "student_expectations": ["A.1(A)"],
                        "keywords": ["quadratic formula"],
                        "response_type": "Open Response Exact",
                        "question_content": "This is a question example",
                        "question_img": "",
                        "options": [
                            {
                                "letter": "A",
                                "content": "Sample content",
                                "image": "",
                                "unit": "",
                                "is_answer": True
                            }
                        ]
                    }
                },
                "college_type_question": {
                    "summary": "College type question",
                    "description": "Create a college type question",
                    "value": {
                        "question_type": "College Level",
                        "classification": "SAT",
                        "test_code": "123456",
                        "keywords": ["quadratic formula"],
                        "response_type": "Open Response Exact",
                        "question_content": "This is a question example",
                        "question_img": "",
                        "options": [
                            {
                            "letter": "A",
                            "content": "Sample content",
                            "image": "",
                            "unit": "",
                            "is_answer": True
                            }
                        ]
                    }
                },
                "mathworld_type_question": {
                    "summary": "Mathworld type question",
                    "description": "Create a mathworld type question",
                    "value": {
                        "question_type": "Mathworld",
                        "grade_level": 3,
                        "teks_code": "A.1",
                        "subject": "Algebra I",
                        "topic": "sample topic",
                        "category": "1",
                        "student_expectations": ["A.1(A)"],
                        "keywords": ["quadratic formula"],
                        "difficulty": "Easy",
                        "points": 1,
                        "response_type": "Open Response Exact",
                        "question_content": "This is a question example",
                        "question_img": "",
                        "options": [
                            {
                            "letter": "A",
                            "content": "Sample content",
                            "image": "",
                            "unit": "",
                            "is_answer": True
                            }
                        ]
                    }
                },
            }

updated_question_payload={
                "staar_type_question": {
                    "summary": "Staar type question",
                    "description": "Create a staar type question",
                    "value":{
                        "question_type": "STAAR",
                        "grade_level": 3,
                        "release_date": "2023-12",
                        "category": "1",
                        "student_expectations": ["A.1(A)"],
                        "keywords": ["quadratic formula"],
                        "response_type": "Open Response Exact",
                        "question_content": "This is a question example",
                        "question_img": "",
                        "options": [
                            {
                                "letter": "A",
                                "content": "Sample content",
                                "image": "",
                                "unit": "",
                                "is_answer": True
                            }
                        ],
                        "update_note" : "Updated message"
                    }
                },
                "college_type_question": {
                    "summary": "College type question",
                    "description": "Create a college type question",
                    "value": {
                        "question_type": "College Level",
                        "classification": "SAT",
                        "test_code": "123456",
                        "keywords": ["quadratic formula"],
                        "response_type": "Open Response Exact",
                        "question_content": "This is a question example",
                        "question_img": "",
                        "options": [
                            {
                            "letter": "A",
                            "content": "Sample content",
                            "image": "",
                            "unit": "",
                            "is_answer": True
                            }
                        ],
                        "update_note" : "Updated message"
                    }
                },
                "mathworld_type_question": {
                    "summary": "Mathworld type question",
                    "description": "Create a mathworld type question",
                    "value": {
                        "question_type": "Mathworld",
                        "grade_level": 3,
                        "teks_code": "A.1",
                        "subject": "Algebra I",
                        "topic": "sample topic",
                        "category": "1",
                        "student_expectations": ["A.1(A)"],
                        "keywords": ["quadratic formula"],
                        "difficulty": "Easy",
                        "points": 1,
                        "response_type": "Open Response Exact",
                        "question_content": "This is a question example",
                        "question_img": "",
                        "options": [
                            {
                            "letter": "A",
                            "content": "Sample content",
                            "image": "",
                            "unit": "",
                            "is_answer": True
                            }
                        ],
                        "update_note" : "Updated message"
                    }
                },
            }

account_payload={
                "staff_or_admin_create_account": {
                    "summary": "Create staff or admin account details",
                    "description": "Create staff or admin account details",
                    "value":{
                        "first_name": "John",
                        "middle_name": "Dee",
                        "last_name": "Doe",
                        "role": "staff",
                        "email": "john_d_doe@gmail.com",
                        "password": "Heyy123!",
                        "repeat_password": "Heyy123!"
                    },
                    
                },
                "subscriber_create_account": {
                    "summary": "Create subsriber account details",
                    "description": "Create subsriber account details",
                    "value":{
                        "first_name": "John",
                        "middle_name": "Dee",
                        "last_name": "Doe",
                        "role": "subscriber",
                        "school": "Harvard University",
                        "email": "john_d_doe@gmail.com",
                        "password": "Heyy123!",
                        "repeat_password": "Heyy123!"
                    },
                },
            }

updated_account_payload={
                "staff_or_admin_update_details": {
                    "summary": "Update staff or admin account details",
                    "description": "Update staff or admin account details",
                    "value":{
                        "first_name": "John",
                        "middle_name": "Dee",
                        "last_name": "Doe",
                        "role": "staff",
                        "email": "john_d_doe@gmail.com"
                    },
                    
                },
                "subscriber_update_details": {
                    "summary": "Update subsriber account details",
                    "description": "Update subsriber account details",
                    "value":{
                        "first_name": "John",
                        "middle_name": "Dee",
                        "last_name": "Doe",
                        "role": "staff",
                        "school": "Harvard University",
                        "email": "john_d_doe@gmail.com"
                    },
                },
            }