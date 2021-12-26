from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter ,Body , status ,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel ,Field
from uuid import uuid4
from typing import Union
from models.PATIENT_MODEL import Patient as PatientModel

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

    doctorId       : str = Field(... ,max_length=100 ,min_length=1 ,regex='[0-9]+'    ,example= '640b4ea5-69b4-46a1-a97f-0405aaee6474') 
    nationalNumber : str = Field(... ,max_length=10 ,min_length=10 ,regex='[0-9]{10}' ,example= '0840123456')


class SaveNumberPhone(BaseModel):

    doctorId    : str = Field(... ,max_length=100 ,min_length=1 ,example= '640b4ea5-69b4-46a1-a97f-0405aaee6474') 
    patientId   : str = Field(... ,max_length=100 ,min_length=2 ,example= 'bba18866-5bd8-4264-9e0d-4d91190688bb')
    numberPhone : str = Field(... ,max_length=11 ,min_length=11 ,example= '09150123456')


class PatientInfo(BaseModel):
    
    patientId     : str = Field(... ,example= 'bba18866-5bd8-4264-9e0d-4d91190688bb')
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



# class UnionNumberPhone(BaseModel): # This will Hold the Union
#     Child: Union[child1, child2, child3] #The Union Required

#     class Config: #This is inside UnionChild, do not place it outside. 
#         schema_extra = {
#             "example": {                    #Mandatory field, this holds your example. Define Your Field from here. 
#                 "id": "1",
#                 "error": "Some Random String",
#                 "user": "OSAS UVUWE",
#                 "user_data": {"oh": "oh_no"},
#             }
#         }

@router.post('/numberphone')
async def save_patient_numberPhone(model: SaveNumberPhone= Body(...)):
    
    # ===== save in redis and check the phone number so that it is not duplicated in the database =======
    await PatientModel(patientId= model.patientId).edit(numberPhone= model.numberPhone)
    # ===========================

    return JSONResponse(
            status_code= status.HTTP_200_OK,
            content= jsonable_encoder({"detail": 'Numberphone saved'}),
            ) 


@router.get("/" ,response_model= PatientInfo ) 
async def fetch_patient_info(doctorID: str = Query(
                                        None ,max_length=50 , min_length=2 ,regex='[0-9]+' ,example= '640b4ea5-69b4-46a1-a97f-0405aaee6474') ,
                            nationalNumber : str = Query(
                                        None ,max_length=10 , min_length=10 ,regex='[0-9]{10}',example='0840123456' ) ):

    if checkNationalNumber(nationalNumber) == False:

        return JSONResponse(
            status_code= status.HTTP_422_UNPROCESSABLE_ENTITY,
            content= jsonable_encoder({"detail": 'This national number is not valid'}),
            )

    resultPatient = await PatientModel().find(nationalNumber= nationalNumber)
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

    result = {}
    if resultPatient:

        for key ,value in resultPatient[0].items():
            result[key] = value
        
        return result


    else:
        return JSONResponse(
            status_code= status.HTTP_404_NOT_FOUND,
            content= jsonable_encoder({"detail": 'No information is available for this national number'}),
            )


    # PatientInfo = {
    # 'patienId'     : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
    # 'firstName'    : 'امیر',
    # 'lastName'     : 'حدادیان',
    # 'fullName'     : 'امیر حدادیان',
    # 'numberPhone'  : '09151234567',
    # 'birthDate'    : '1636299942',
    # 'insurance'    : 'سلامت',
    # 'subInsurance' : 'روستاییان',
    # 'exDate'       : '1786299942'}
