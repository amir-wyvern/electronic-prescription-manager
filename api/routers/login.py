from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter ,Body , status
from fastapi.responses import JSONResponse

from pydantic import BaseModel ,Field
import hashlib
from uuid import uuid4

from ..models.DOCTOR_MODEL import NobanDoctor
from ..insuranceAPI import Doctor

router = APIRouter(
    prefix='/login',
    tags=["Login"]
    )

class Examples:

    user_login_model = {
                'noban': {
                    'summary'    : 'noban account',
                    'description': 'login with noban account',
                    'value':{
                        'username' : 'noban-username' ,
                        'password' : 'noban-password' ,
                        'orgType'  : 'noban'
                    }
                } ,

                'salamat': {
                    'summary': 'salamat account',
                    'description': 'login with salamat account',
                    'value':{
                        'username' : 'salamat-username' ,
                        'password' : 'salamat-password' ,
                        'orgType'  : 'salamat'
                    }
                }
    }

    doctor_info_model = {
                'normal': {
                    'summary': 'normal response',
                    'description': "if the login was successful The doctor's information is returned؛",
                    'value':{
                        'doctorId' : '640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'fistname' : 'حجت',
                        'lastname' : 'مولودی جامی' ,
                        'fullName' : 'حجت مولودی جامی' ,
                        'numberPhone' : '09151234567' ,
                        'nationalNumber' : '08401234567',
                        'contractingLicense' : '8799456',
                        'contractingLicense' : 'قازچ شناسی' 
                    }
                },
                'incomplete': {
                    'summary': 'incomplete data',
                    'description': "The user may not have completed their information yet",
                    'value':{
                        'doctorId' : '640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'fistname' : '',
                        'lastname' : '' ,
                        'fullName' : 'حجت مولودی جامی' ,
                        'numberPhone' : '09151234567' ,
                        'nationalNumber' : '08401234567',
                        'medicalCouncilCode' : '8799456',
                        'contractingLicense' : ''
                    }
                }
    }    


class UserLoginModel(BaseModel):

    username : str = Field(... ,min_length= 3 ,max_length=30)
    password : str = Field(... ,min_length= 3 ,max_length=64)
    orgType  : str = Field(... ,min_length= 3 ,max_length=64)


class DoctorInfoModel(BaseModel):
    
    doctorId                : str = Field(... ,example= '640b4ea5-69b4-46a1-a97f-0405aaee6474')
    fistname                : str = Field(... ,example= 'حجت')
    lastname                : str = Field(... ,example= 'مولودی جامی')
    fullName                : str = Field(... ,example= 'حجت مولودی جامی')
    numberPhone             : str = Field(... ,example= '09151234567')
    nationalNumber          : str = Field(... ,example= '084012345678')
    medicalCouncilCode      : str = Field(... ,example= '8799456')
    contractingLicense      : str = Field(... ,example= 'قازچ شناسی' )


class ErrorModel(BaseModel):

    detail: str = Field(... ,example= 'Username or password is incorrect!' )


@router.post("/" ,response_model= DoctorInfoModel ,responses={401: {'model': ErrorModel}})
async def login(user: UserLoginModel = Body(... ,examples= Examples.user_login_model)):


    if user.orgType == 'salamat':

        salamatCode ,salamatDetail = NobanDoctor().find(salamatUsername= user.username)

        if not salamatCode and salamatDetail['salamatPassword'] == user.password:

            return JSONResponse(
                status_code= status.HTTP_401_UNAUTHORIZED,
                content= jsonable_encoder({"detail": 'Username or password is incorrect!'}),
                )

        session = Doctor().getSession(username= user.username ,password= user.password)

        return salamatDetail


    nobanCode ,nobanDetail = NobanDoctor().find(nbnUsername= user.username )

    if not nobanCode and nobanDetail['nbnPassword'] == user.password:

        return JSONResponse(
                status_code= status.HTTP_401_UNAUTHORIZED,
                content= jsonable_encoder({"detail": 'Username or password is incorrect!'}),
                )

    return nobanDetail    

    


