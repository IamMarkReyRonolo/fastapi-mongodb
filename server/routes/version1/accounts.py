from fastapi import APIRouter, Request, Depends, status, HTTPException, Body
from typing import Any
import math
from bson import ObjectId
from server.authentication.jwt_bearer import JWTBearer
from server.authentication import jwt_handler
from server.authentication.bcrypter import Hasher
from server.connection.database import db
from server.models.utilities import sample_payloads, model_parser
from server.models.account import (
  LogIn,
  Registration,
  Account,
  AccountResponseModel,
  SubscriberAccount,
  UpdatedPassword
)

router = APIRouter()

@router.post("/login",
             status_code=status.HTTP_200_OK,
             response_description="Successfully logged in.")
async def login(credentials: LogIn):
        try:
            account = await Account.find_one(Account.email == credentials.email)
            if account:
              verified = Hasher().verify_password(
                    login_password=credentials.password, member_password=account.password)
              
              if verified:
                  name = account.first_name + " " + account.last_name
                  token = jwt_handler.signJWT(str(account.id), name, account.role)
                  return token

            raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="username or password is incorrect") 
        except Exception as e:

            if str(e) == '404':
                raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="username or password is incorrect")
            
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="An error occured: " + str(e)) 

@router.post("/create",
             dependencies=[Depends(JWTBearer(access_level='admin'))],
             status_code=status.HTTP_201_CREATED,
             response_description="Account created"
            )
async def create_account(request: Request, account: Registration):
        try:
            account.created_by = request.state.user_details['name']
            if account.role != 'subscriber':
              new_account = Account(
                  first_name=account.first_name,
                  middle_name=account.middle_name,
                  last_name=account.last_name,
                  role=account.role,
                  email=account.email,
                  password=Hasher().hash_password(password=account.password),
                  created_by=account.created_by
              )
              
            else:
                new_account = SubscriberAccount(
                  first_name=account.first_name,
                  middle_name=account.middle_name,
                  last_name=account.last_name,
                  role=account.role,
                  school=account.school,
                  email=account.email,
                  password=Hasher().hash_password(password=account.password),
                  created_by=account.created_by
              )
                
            await new_account.insert()
            return {"detail": "Successfully Created Account",  "Account": new_account}
        except Exception as e:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="An error occured: " + str(e)) 
    
@router.get("/all", dependencies=[Depends(JWTBearer(access_level='admin'))], status_code=status.HTTP_200_OK)
async def get_all_accounts(role: str = None, page_num: int = 1, page_size: int = 10):  # type: ignore
    if(page_num <=0 ):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Page number should not be equal or less than to 0")

    if(page_size <= 0):
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Page size should not be equal or less than to 0")
    try:
        query = {}
                
        if role:
            query['role'] =  role
        
        accounts = await Account.find(query).project(AccountResponseModel).sort('-updated_at').skip((page_num - 1) * page_size).limit(page_size).to_list(None)

        pipeline = [
                    {
                        "$group": {
                            "_id": None,
                            "no_of_admin": {
                                "$sum": {
                                    "$cond": [{"$eq": ["$role", "admin"]}, 1, 0]
                                }
                            },
                            "no_of_staff": {
                                "$sum": {
                                    "$cond": [{"$eq": ["$role", "staff"]}, 1, 0]
                                }
                            },
                            "no_of_subscriber": {
                                "$sum": {
                                    "$cond": [{"$eq": ["$role", "subscriber"]}, 1, 0]
                                }
                            },
                            "total_no_of_accounts": {"$sum": 1}
                        }
                    },
                    {
                        "$project": {
                            "_id": 0,
                            "no_of_admin": 1,
                            "no_of_staff": 1,
                            "no_of_subscriber": 1,
                            "total_no_of_accounts": 1
                        }
                    }
                ]
        
        total_count = await db['account_collection'].aggregate(pipeline).to_list(None)
        total_count_of_specific_role = total_count[0]['total_no_of_accounts']
        if role:
            total_count_of_specific_role = total_count[0]['total_no_of_' + role]
        response = {
            "data": accounts,
            "count": len(accounts),
            "total": total_count[0],
            "page": page_num,
            "no_of_pages": math.ceil(total_count_of_specific_role/page_size),
        }

        return response
    except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e))

@router.get("/user_data", dependencies=[Depends(JWTBearer(access_level='staff'))], status_code=status.HTTP_200_OK)
async def get_user_data(request: Request, account_id: str = None):
    if account_id:
      sample = JWTBearer(access_level='admin')
      await sample.__call__(request)
    else:
      account_id = request.state.user_details['uuid']

    account = await Account.find({"_id":ObjectId(account_id) }).project(AccountResponseModel).to_list(None)
    return account

@router.put("/update_details", dependencies=[Depends(JWTBearer(access_level='staff'))], status_code=status.HTTP_200_OK)
async def get_user_data(request: Request,
                        account_id: str = None,
                        updated_account: Any = Body(openapi_examples=sample_payloads.updated_account_payload)):
    updated_account = model_parser.updated_account_parser(updated_account)
    updated_account.updated_by = request.state.user_details['name']
    if account_id:
      sample = JWTBearer(access_level='admin')
      await sample.__call__(request)
    else:
      account_id = request.state.user_details['uuid']

    fetched_account = await Account.get(account_id)
    if fetched_account:
        account = await fetched_account.update(
                        {"$set": updated_account.dict()}
                  )
        return {"Successfully updated": account}

@router.put("/change_password", dependencies=[Depends(JWTBearer(access_level='staff'))], status_code=status.HTTP_200_OK)
async def get_user_data(request: Request, updated_password: UpdatedPassword, account_id: str = None, ):
    updated_password.updated_by = request.state.user_details['name']
    if account_id:
      sample = JWTBearer(access_level='admin')
      await sample.__call__(request)
    else:
      account_id = request.state.user_details['uuid']

    fetched_account = await Account.get(account_id)

    if fetched_account:
        verified = Hasher().verify_password(
                login_password=updated_password.old_password, member_password=fetched_account.password)
        if verified:
            updated_password = updated_password.model_dump()
            del updated_password['old_password']
            del updated_password['repeat_new_password']
            updated_password['password'] = Hasher().hash_password(updated_password['new_password'])
            del updated_password['new_password']

            await fetched_account.update(
                            {"$set": updated_password}
                      )
            
            return {"message": "Successfully change password"}
        
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="Wrong password")

@router.delete("/delete/{account_id}", dependencies=[Depends(JWTBearer(access_level='admin'))], status_code=status.HTTP_200_OK)
async def change_password(account_id: str):
    deleted_account = await db['account_collection'].find_one_and_delete({"_id": ObjectId(account_id)})
    if deleted_account:
        return {"detail": "Successfully Deleted Account"}

    raise HTTPException(status.HTTP_404_NOT_FOUND,
                        detail="Account not found") 
