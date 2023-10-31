from fastapi import APIRouter, Request, Depends, status, HTTPException
from bson import ObjectId
from server.authentication.jwt_bearer import JWTBearer
from server.authentication import jwt_handler
from server.authentication.bcrypter import Hasher
from server.models.account import (
  LogIn,
  Account,
  SubscriberAccount,
  UpdatedPassword,
  SubscriberAccountResponseModel
)

from server.models.users import (
    User,
    Registration,
    UpdatedUserViaSubscriber
)

router = APIRouter()

@router.post("/login",
             status_code=status.HTTP_200_OK,
             response_description="Successfully logged in.")
async def login(credentials: LogIn):
        try:
            account = await User.find_one(User.email == credentials.email)
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
            
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e))


@router.post("/register", status_code=status.HTTP_200_OK)
async def login(user: Registration):
    pass
        
@router.get("/user_data", dependencies=[Depends(JWTBearer(access_level='subscriber'))], status_code=status.HTTP_200_OK)
async def get_user_data(request: Request):
    try:
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
                        updated_account: UpdatedUserViaSubscriber
                        ):
        try:
            updated_account.updated_by = request.state.user_details['name']
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

@router.patch("/update/student/contact_person", dependencies=[Depends(JWTBearer(access_level='student'))], status_code=status.HTTP_200_OK)
async def update_class(request: Request):
    pass

@router.patch("/update/teacher/education", dependencies=[Depends(JWTBearer(access_level='student'))], status_code=status.HTTP_200_OK)
async def update_class(request: Request):
    pass

@router.patch("/update/user_profile_picture", dependencies=[Depends(JWTBearer(access_level='student'))], status_code=status.HTTP_200_OK)
async def update_class(request: Request):
    pass


@router.delete("/delete/user_profile_picture", dependencies=[Depends(JWTBearer(access_level='student'))], status_code=status.HTTP_200_OK)
async def update_class(request: Request):
    pass