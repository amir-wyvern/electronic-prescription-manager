from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter ,Body , status
from fastapi.responses import JSONResponse

from pydantic import BaseModel ,Field


from async_redis import redis
from models.DOCTOR_MODEL import DoctorInfo
from insuranceAPI import Doctor

router = APIRouter(
    prefix="/signup",
    tags=["signup"]
    )

class LoginUserModel(BaseModel):

    username : str = Field(... ,min_length= 3 ,max_length=30)
    password : str = Field(... ,min_length= 3 ,max_length=64)


class DoctorInfoModel(BaseModel):
    
    username : str
    name : str
    lastname :str
    number_phone : str
    doctor_id : str
    contracting_party_license : str
    

@router.post("/" ,response_model= DoctorInfoModel)
async def signup(user: LoginUserModel = Body(...)):


    docInfo = DoctorInfo().find(username= user.username ,password= user.password)

    if not docInfo:

        return JSONResponse(
            status_code= status.HTTP_401_UNAUTHORIZED,
            content= jsonable_encoder({"detail": 'Username or password is incorrect!'}),
            )


    if docInfo.salamat_insurance :
        
        Doctor().getSession(username= user.username ,password= user.password)
    
    
    # userDetail = await redis._hgetall(user.username)
    # if hashlib.sha256(user.username.encode()) == userDetail['password']:

    #     return JSONResponse(
    #         status_code= status.HTTP_403_FORBIDDEN,
    #         content= jsonable_encoder({"detail": 'Username or password is incorrect!'}),
    #         )
    
    return docInfo

