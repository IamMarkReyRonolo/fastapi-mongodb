from fastapi import status, HTTPException

def validate_query_params(page_num:int, page_size:int):
    if(page_num <=0 ):
              raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                  detail="Page number should not be equal or less than to 0")

    if(page_size <= 0):
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Page size should not be equal or less than to 0")