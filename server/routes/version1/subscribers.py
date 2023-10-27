from fastapi import APIRouter, Request, Depends, status, HTTPException
import math
from bson import ObjectId
from beanie.operators import In
from server.authentication.jwt_bearer import JWTBearer
from server.authentication import jwt_handler
from server.authentication.bcrypter import Hasher
from server.connection.database import db
from server.models.validators.query_params_validators import validate_query_params
from server.models.account import (
    LogIn,
    Account,
    SubscriberAccount,
    UpdatedPassword,
    SubscriberAccountResponseModel
)

from server.models.users import (
    UserAccounts,
    User,
    UpdatedUserViaSubscriber,
    UpdatedStatus,
    UpdatedRole,
    ResetPassword,
    UserResponseModel,
    InitialUserAccountResponseModel
)

router = APIRouter()

@router.post("/login",
             status_code=status.HTTP_200_OK,
             response_description="Successfully logged in.")
async def login(credentials: LogIn):
        try:
            account = await SubscriberAccount.find_one(SubscriberAccount.email == credentials.email)
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
            
            if '1 validation error for SubscriberAccount' in str(e) :
                    raise HTTPException(status.HTTP_404_NOT_FOUND,
                                    detail="username or password is incorrect")
            
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="An error occured: " + str(e))
        

@router.post("/register_emails",
             status_code=status.HTTP_200_OK,
             dependencies=[Depends(JWTBearer(access_level='subscriber'))],
             response_description="Successfully registered emails.")
async def register_emails(request: Request, user_accounts: UserAccounts):
        try:
            user_accounts = user_accounts.model_dump()
            user_id = request.state.user_details['uuid']
            accounts = [
                        User(subscriber_id=user_id, first_name='DEFAULT', last_name='DEFAULT',
                            status='inactive', role=user['role'], email=user['email'], password="DEFAULT")
                        for user in user_accounts['accounts']
                      ]
            
            results = await User.insert_many(accounts)
            accounts = await User.find(
                            In(User.id, results.inserted_ids)
                        ).project(InitialUserAccountResponseModel).to_list()
            
            return {"message": "Successfully registered emails", "accounts": accounts}
        
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e)) 


@router.get("/all_users", dependencies=[Depends(JWTBearer(access_level='subscriber'))], status_code=status.HTTP_200_OK)
async def get_all_users(request: Request, role: str = None, status: str = None, page_num: int = 1, page_size: int = 10):
    validate_query_params(page_num=page_num, page_size=page_size)
    try:
        user_id = request.state.user_details['uuid']
        query = {'subscriber_id': user_id }
        if role:
            query['role'] = role
        
        if status:
            query['status'] = status

        accounts = await User.find(query).project(UserResponseModel).sort(-User.updated_at).skip((page_num - 1) * page_size).limit(page_size).to_list(None)
        total_count = await User.find(query).count()
        response = {
                "data": accounts,
                "count": len(accounts),
                "total": total_count,
                "page": page_num,
                "no_of_pages": math.ceil(total_count/page_size)
            }

        return response
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e))

@router.get("/user_data", dependencies=[Depends(JWTBearer(access_level='subscriber'))], status_code=status.HTTP_200_OK)
async def get_user_data(request: Request, user_id: str = None):
    try:
        model = User
        projectionModel = UserResponseModel
        if not user_id:
            user_id = request.state.user_details['uuid']
            model = SubscriberAccount
            projectionModel = SubscriberAccountResponseModel

        account = await model.find({"_id":ObjectId(user_id) }).project(projectionModel).to_list(None)
        if account:
            return {'data': account[0]}
    
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Account not found") 
    except Exception as e:
        if str(e) == '404':
                raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Account not found") 
      
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e))

@router.patch("/update_details", dependencies=[Depends(JWTBearer(access_level='subscriber'))], status_code=status.HTTP_200_OK)
async def update_account_details(request: Request,
                        updated_account: UpdatedUserViaSubscriber,
                        user_id: str = None
                        ):
        try:
            updated_account.updated_by = request.state.user_details['name']
            if not user_id:
                user_id = request.state.user_details['uuid']
            
            fetched_account = await User.get(user_id)
            if fetched_account:
                account = await fetched_account.update(
                                {"$set": updated_account.model_dump()}
                            )
                return {"message": "Successfully updated status"}
            
            raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="User not found") 
        except Exception as e:
            if str(e) == '404':
                    raise HTTPException(status.HTTP_404_NOT_FOUND,
                                    detail="User not found") 
            
            if 'Id must be of type PydanticObjectId' in str(e):
                    raise HTTPException(status.HTTP_404_NOT_FOUND,
                                    detail="User not found")
                
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                    detail="An error occured: " + str(e))

@router.patch("/update/user_role/{user_id}", dependencies=[Depends(JWTBearer(access_level='subscriber'))], status_code=status.HTTP_200_OK)
async def update_user_role(request: Request, updated_role: UpdatedRole, user_id:str):
    
    try:
        updated_role.updated_by = request.state.user_details['name']
        fetched_account = await User.get(user_id)

        if fetched_account:
            await fetched_account.update(
                            {"$set": updated_role}
                        )
            
            return {"message": "Successfully changed role"}
        
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="User not found") 
    except Exception as e:
        if str(e) == '404':
                raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="User not found")
        
        if 'Id must be of type PydanticObjectId' in str(e):
                    raise HTTPException(status.HTTP_404_NOT_FOUND,
                                    detail="User not found")
        
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e))
    
@router.patch("/update/user_status{user_id}", dependencies=[Depends(JWTBearer(access_level='subscriber'))], status_code=status.HTTP_200_OK)
async def update_user_status(request: Request, updated_status: UpdatedStatus, user_id:str):
    
    try:
        updated_status.updated_by = request.state.user_details['name']
        fetched_account = await User.get(user_id)

        if fetched_account:
            await fetched_account.update(
                            {"$set": updated_status}
                        )
            
            return {"message": "Successfully changed status"}
        
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="User not found") 
    except Exception as e:
        if str(e) == '404':
                raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="User not found")
        
        if 'Id must be of type PydanticObjectId' in str(e):
                    raise HTTPException(status.HTTP_404_NOT_FOUND,
                                    detail="User not found")
        
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e))

@router.patch("/change_password", dependencies=[Depends(JWTBearer(access_level='subscriber'))], status_code=status.HTTP_200_OK)
async def change_password(request: Request, updated_password: UpdatedPassword):
    
    try:
        user_id = request.state.user_details['uuid']
        fetched_account = await Account.get(user_id)

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
                
                return {"message": "Successfully changed password"}
            
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Wrong password")
    except Exception as e:
        if str(e) == '404':
                raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Account not found") 
        
        if str(e) == '400':
                raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Wrong password") 
        
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e))
    
@router.patch("/reset_password/{user_id}", dependencies=[Depends(JWTBearer(access_level='subscriber'))], status_code=status.HTTP_200_OK)
async def reset_password(request: Request,  user_id: str = None, ):
    try:
        fetched_account = await User.get(user_id)
        if fetched_account:

            data = ResetPassword(updated_by=request.state.user_details['name'])
            password = data.password

            data.password = Hasher().hash_password(data.password)
            data = data.model_dump()
            await fetched_account.update({"$set": data})

            return {"message": "Successfully reset password", "new_password": password}
        
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="User not found") 
    except Exception as e:
        if str(e) == '404':
                raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="User not found")
        
        if 'Id must be of type PydanticObjectId' in str(e):
                    raise HTTPException(status.HTTP_404_NOT_FOUND,
                                    detail="User not found")
        
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e))

@router.delete("/delete/{user_id}", dependencies=[Depends(JWTBearer(access_level='subscriber'))], status_code=status.HTTP_200_OK)
async def delete_account(user_id: str):
    try:
      deleted_account = await db['user_collection'].find_one_and_delete({"_id": ObjectId(user_id)})
      if deleted_account:
          return {"detail": "Successfully Deleted Account"}

      raise HTTPException(status.HTTP_404_NOT_FOUND,
                          detail="Account not found") 
    except Exception as e:
        if str(e) == '404':
                raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Account not found")
        
        if 'Id must be of type PydanticObjectId' in str(e):
                    raise HTTPException(status.HTTP_404_NOT_FOUND,
                                    detail="User not found")

        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e))
