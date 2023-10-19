from fastapi import APIRouter, Request, Depends, status, HTTPException, Body, Query
from typing import Any, Annotated
from pymongo import ReturnDocument
from bson import ObjectId
import math, json
from server.authentication.jwt_bearer import JWTBearer
from server.models.utilities import sample_payloads, model_parser
from server.connection.database import db
from server.models.question import (
    Question,
    StaarQuestion,
    CollegeQuestion,
    MathworldQuestion,
    UpdateQuestionStatus
)
from server.controllers import activity_controller

router = APIRouter()

###############################
# get all questions  endpoint #
###############################

@router.get("/",
            dependencies=[Depends(JWTBearer(access_level='staff'))],
            status_code=status.HTTP_201_CREATED,
            response_description="Fetch all questions from the database with pagination"
            )
async def get_all_questions(question_status:  Annotated[list[str] | None, Query()] = None,
                            question_type: Annotated[list[str] | None, Query()] = None,
                            response_type: Annotated[list[str] | None, Query()] = None,
                            keywords: Annotated[list[str] | None, Query()] = None,
                            grade_level: Annotated[list[str] | None, Query()] = None,
                            release_date: Annotated[list[str] | None, Query()] = None,
                            category: Annotated[list[str] | None, Query()] = None,
                            student_expectations: Annotated[list[str] | None, Query()] = None,
                            subject: Annotated[list[str] | None, Query()] = None,
                            topic: Annotated[list[str] | None, Query()] = None,
                            teks_code: Annotated[list[str] | None, Query()] = None,
                            difficulty: Annotated[list[str] | None, Query()] = None,
                            classification: Annotated[list[str] | None, Query()] = None,
                            test_code: Annotated[list[str] | None, Query()] = None,
                            page_num: int = 1,
                            page_size: int = 10):
        try: 
            # default status
            question_status = ['Pending'] if question_status is None else question_status

            arguments = locals()
            pagination_filter = {}
            query = {"$and": []}
            for k, v in arguments.items():
                if v is not None:
                    if (k =='page_num' or k == 'page_size'):
                        continue
                    query['$and'].append({k: {"$in": v}})
                    pagination_filter[k] = v

            questions = await db['question_collection'].find(query).sort('updated_at', -1).skip((page_num - 1) * page_size).limit(page_size).to_list(1000)
            total_count = await db['question_collection'].count_documents(query)
            questions = model_parser.parse_response(questions)

            response = {
                "data": questions,
                "count": len(questions),
                "total": total_count,
                "page": page_num,
                "no_of_pages": math.ceil(total_count/page_size),
                "pagination_filter": pagination_filter
            }

            return response
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="An error occured: " + str(e)) 

###############################
# get question by id endpoint #
###############################

@router.get("/{question_id}",
            dependencies=[Depends(JWTBearer(access_level='staff'))],
            status_code=status.HTTP_201_CREATED,
            response_description="Fetch specific question by id from the database"
            )
async def get_question_by_id(question_id: str):
        try:
            fetched_question = await db['question_collection'].find_one({"_id": ObjectId(question_id)})
            if fetched_question:
                parsed_question = model_parser.parse_response([fetched_question])[0]
                return {"question": parsed_question}

            raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Question not found") 
        
        except Exception as e:
            if str(e) == '404':
                raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Question not found") 
            
            if 'not a valid ObjectId' in str(e):
                raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="Question not found")
        
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="An error occured: " + str(e)) 

############################
# create question endpoint #
############################

@router.post("/create",
            dependencies=[Depends(JWTBearer(access_level='staff'))],
            status_code=status.HTTP_201_CREATED,
            response_description="Question added into the database"
            )
async def create_question(request: Request,
                        question: Any = Body(openapi_examples=sample_payloads.question_payload)):
        question = model_parser.question_parser(question)
        try:
            question.created_by = request.state.user_details['name']
            await question.insert()
            await activity_controller.record_activity(activity_title='Create',
                                                    staff_involved=question.created_by,
                                                    staff_uuid=request.state.user_details['uuid'],
                                                    question=question)

            return {"detail": "Successfully Added Question",  "question_id": str(question.id)}
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e))
        

############################
# update question endpoint #
############################

@router.put("/update/{question_id}",
            dependencies=[Depends(JWTBearer(access_level='staff'))],
            status_code=status.HTTP_201_CREATED,
            response_description="Question has been updated in the database")
async def update_question(request: Request,
                                question_id: str,
                                updated_question: Any = Body(openapi_examples=sample_payloads.updated_question_payload)):
        updated_question = model_parser.updated_question_parser(updated_question)
        try:
            fetched_question = await StaarQuestion.get(question_id) if updated_question.question_type == 'STAAR' else \
                            await CollegeQuestion.get(question_id) if updated_question.question_type == 'College level' else \
                            await MathworldQuestion.get(question_id)
            
            if fetched_question:
                updated_question.updated_by = request.state.user_details['name']
                question = await fetched_question.update(
                    {"$set": updated_question.dict()}
                )
                await activity_controller.record_activity(activity_title='Update',
                                                        staff_involved=question.updated_by,
                                                        staff_uuid=request.state.user_details['uuid'],
                                                        update_note=updated_question.update_note,
                                                        question=question)

                return {"detail": "Successfully Updated Question",  "question": question}
            
            raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Question not found") 
        
        except Exception as e:
            if str(e) == '404':
                raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Question not found") 
            
            if 'not a valid ObjectId' in str(e):
                raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="Question not found")
        
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="An error occured: " + str(e)) 

###################################
# update question status endpoint #
###################################

@router.patch("/update/question_status/{question_id}", dependencies=[Depends(JWTBearer(access_level='staff'))], status_code=status.HTTP_200_OK)
async def update_question_status(question_id: str,
                                 request: Request,
                                 status_update: UpdateQuestionStatus,
                                 ):
    try:
        status_update.reviewed_by = request.state.user_details['name']
        question = await db['question_collection'].find_one_and_update({'_id': ObjectId(question_id)},
                                                                        {'$set': {'question_status': status_update.status,
                                                                                'reviewed_by' : status_update.reviewed_by,
                                                                                'reviewed_at' : status_update.reviewed_at}},
                                                                        return_document=ReturnDocument.AFTER
                                                                        )
        question = json.loads(model_parser.JSONEncoder().encode(question))
        if question:
            return {'data': question}
        
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Question not found") 
        
    except Exception as e:
        if str(e) == '404':
            raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Question not found") 
        
        if 'not a valid ObjectId' in str(e):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Question not found")
        
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e)) 
        


############################
# delete question endpoint #
############################

@router.delete("/delete/{question_id}",
            dependencies=[Depends(JWTBearer(access_level='staff'))],
            status_code=status.HTTP_201_CREATED,
            response_description="Question has been deleted in the database")
async def delete_question(question_id: str, request: Request,):
        try:

            deleted_question = await db['question_collection'].find_one_and_delete({"_id": ObjectId(question_id)})

            if deleted_question:
                parsed_question = model_parser.parse_response([deleted_question])[0]
                await activity_controller.record_activity(activity_title='Delete',
                                                        staff_involved=request.state.user_details['name'],
                                                        staff_uuid=request.state.user_details['uuid'],
                                                        question=parsed_question)
                return {"detail": "Successfully Deleted Question"}

            raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Question not found") 
        
        except Exception as e:
            if str(e) == '404':
                raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Question not found") 
            
            if 'not a valid ObjectId' in str(e):
                raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="Question not found")
        
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="An error occured: " + str(e)) 
    