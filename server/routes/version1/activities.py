from fastapi import APIRouter, Request, Depends, status, HTTPException
from server.authentication.jwt_bearer import JWTBearer
import math
from server.models.question import (
  Activity
)

router = APIRouter()

@router.get("/",
             dependencies=[Depends(JWTBearer(access_level='staff'))],
             status_code=status.HTTP_201_CREATED,
             response_description="Get all activities"
            )
async def get_all_activities(request: Request, is_own: bool = False, question_id: str = None, page_num: int = 1, page_size: int = 10):
        if(page_num <=0 ):
                raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="Page number should not be equal or less than to 0")

        if(page_size <= 0):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="Page size should not be equal or less than to 0")
        
        try:
            query = {}
            
            if is_own:
                query['staff_id'] =  request.state.user_details['uuid']
            
            if question_id:
                query['question_id'] =  question_id
                
            activities = await Activity.find(query).sort('-created_at').skip((page_num - 1) * page_size).limit(page_size).to_list(1000)
            total_count = await Activity.find(query).count()
        
            response = {
                "data": activities,
                "count": len(activities),
                "total": total_count,
                "page": page_num,
                "no_of_pages": math.ceil(total_count/page_size),
            }
            
            return response
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e))
