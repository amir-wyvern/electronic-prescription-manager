from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter ,Body , status
from fastapi.responses import JSONResponse
from pydantic import BaseModel ,Field
from uuid import uuid4

from async_redis.redis_obj import redis
from insuranceAPI.insurance_handler import Pateint

router = APIRouter(
    prefix="/v1/patient",
    tags=["Patient"] 
    )


def checkNationalNumber(nationalNumber : str) -> bool:

    """
    Check the accuracy of the national number
    """

    sum = 0
    checkNumber = int(nationalNumber[-1])
    otherNumbers = nationalNumber[:-1]

    for index ,number in enumerate(otherNumbers[::-1]):
        
        sum += int(number) * (index + 2)
        
    resNumber = sum % 11
    
    if resNumber < 2 and resNumber == checkNumber:
        return True

    elif resNumber >= 2 and checkNumber == (11 - resNumber):
        return True

    return False


class FetchNationalNumber(BaseModel):

    doctorID       : str = Field(... ,max_length=100 ,min_length=1 ,regex='[0-9]+'    ,example= '640b4ea5-69b4-46a1-a97f-0405aaee6474') 
    nationalNumber : str = Field(... ,max_length=10 ,min_length=10 ,regex='[0-9]{10}' ,example= '0840123456')


class SaveNumberPhone(BaseModel):

    pateintId   : str = Field(... ,max_length=30 ,min_length=40 ,regex='[0-9]+'    ,example= 'bba18866-5bd8-4264-9e0d-4d91190688bb')
    numberPhone : str = Field(... ,max_length=11 ,min_length=11 ,regex='[0-9]{11}' ,example= '09150123456')


class PatientInfo(BaseModel):
    
    patienId     : str = Field(... ,example= 'bba18866-5bd8-4264-9e0d-4d91190688bb')
    firstName    : str = Field(... ,example= 'امیر')
    lastName     : str = Field(... ,example= 'حدادیان')
    fullName     : str = Field(... ,example= 'امیر حدادیان')
    numberPhone  : str = Field(... ,example= '09151234567')
    birthDate    : str = Field(... ,example= '1636299942')
    insurance    : str = Field(... ,example= 'سلامت')
    subInsurance : str = Field(... ,example= 'روستاییان')
    exDate       : str = Field(... ,example= '1786299942')


class ErrorModel(BaseModel):

    detail : str = Field(... ,example= 'Username or password is incorrect!' )

@router.post('/numberphone')
async def save_patient_numberPhone(model: SaveNumberPhone= Body(...)):
    
    # ===== save in redis and check the phone number so that it is not duplicated in the database =======
    pass
    # ===========================

    return JSONResponse(
            status_code= status.HTTP_200_OK,
            content= jsonable_encoder({"detail": 'Numberphone saved'}),
            ) 


@router.get("/" ,response_model= PatientInfo ,responses= {422: {'model': ErrorModel}}) 
async def fetch_patient_info(model: FetchNationalNumber= Body(...)):

    if checkNationalNumber(model.nationalNumber) == False:

        return JSONResponse(
            status_code= status.HTTP_422_UNPROCESSABLE_ENTITY,
            content= jsonable_encoder({"detail": 'This national number is not valid'}),
            )

    print('sdsdfs================================')    
    # ====== Check the existence of a national number in the sabteahval system ======
    pass
    # ===============================================================================
    
    # resp = await Pateint.getInfo(model.nationalNumber)

    # ====== if insurance patient is salamat ,so we have to get samad code ==========
    pass
    # ================================================================================

    # ====== This part will be completed after receiving the complete api from the organizations ======
    pass
    # =================================================================================================

    PatientInfo = {
    'patienId'     : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
    'firstName'    : 'امیر',
    'lastName'     : 'حدادیان',
    'fullName'     : 'امیر حدادیان',
    'numberPhone'  : '09151234567',
    'birthDate'    : '1636299942',
    'insurance'    : 'سلامت',
    'subInsurance' : 'روستاییان',
    'exDate'       : '1786299942'}
    
    return PatientInfo
