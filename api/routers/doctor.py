from os import error, name
from typing import Dict, List
from fastapi import APIRouter ,Body
from pydantic import BaseModel ,Field
from pydantic.errors import BytesError
from ..async_redis import redis

from ..logs import Logger
from ..routers import patient

logger = Logger()

router = APIRouter(
    prefix="/doctor",
    tags=["doctor"]
    )


class drugQueryModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    match     : str = Field(... ,max_length=150 )


class drugAmntQueryModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    match     : str = Field(... ,max_length=150 )


class drugInstrQueryModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    match     : str = Field(... ,max_length=150 )

class ServiceType(BaseModel):

    srvType      : str = Field(... ,example= '01')
    srvTypeDes   : str = Field(... ,example= 'دارویی')
    status       : str = Field(... ,example= '1')
    statusstDate : str = Field(... ,example= '13940101')
    custType     : str = Field(... ,example= '3')


class DrugQuery_ResponseModel(BaseModel):

    drugId : str = Field(... ,example= '183957')
    name   : str = Field(... ,example= 'ADAPALENE/BENZOYL PEROXIDE  0.1 %/2.5 % TOPICAL GEL')
    

class ItemCheckDrug(BaseModel):

    drugId : str = Field(... ,example= '897986')


class RespCheckDrug(BaseModel):
    
    drugId        : str = Field(... ,example= '897986')
    drugName      : str = Field(... ,example= 'ADAPALENE/BENZOYL PEROXIDE  0.1 %/2.5 % TOPICAL GEL')
    exceptionType : str = Field(... ,example= 'error')
    exceptionMsg  : List = Field(... ,example= ['تداخل دارویی وجود درد']) 


class CheckDrugModel(BaseModel):
    
    doctorId    : str = Field(... ,example= '640b4ea5-69b4-46a1-a97f-0405aaee6474')
    patientId   : str = Field(... ,example= 'bba18866-5bd8-4264-9e0d-4d91190688bb')
    drugs       : List[ItemCheckDrug] 


class CheckDrug_ResponseModel(BaseModel):

    exception : str = Field(... ,example= 'error')
    drugs     : List[RespCheckDrug]


class DrugAmntQuery_ResponseModel(BaseModel):

    drugAmntId : str = Field(... ,example= '46546823')
    name       : str = Field(... ,example= 'دو (2)  قاشق غذاخوري (10 سي سي)')
    

class DrugInstrQuery_ResponseModel(BaseModel):
   
    drugInstId : str = Field(... ,example= '1354954')
    name       : str = Field(... ,example= 'صبح، پيش از ظهر')


class Examples:

    check_drugs ={
                'normal': {
                    'summary': 'without error and warning',
                    'description': 'everything is ok',
                    'value':{
                        'exception' : False,
                        'drugs': [
                            {
                            'drugId': '897986' ,
                            'drugName': 'ADAPALENE/BENZOYL PEROXIDE  0.1 %/2.5 % TOPICAL GEL',
                            'exceptionType': 'ok', 
                            'exceptionMsg' : []
                        }
                        ]
                    }
                } ,

                'error': {
                    'summary': 'having a error',
                    'description': 'Drug combinations or drug coverage do not overlap',
                    'value':{
                        'exception' : True,
                        'drugs': [
                            {
                            'drugId': '897986' ,
                            'drugName': 'ADAPALENE/BENZOYL PEROXIDE  0.1 %/2.5 % TOPICAL GEL',
                            'exceptionType': 'error', 
                            'exceptionMsg' : ['تداخل دارویی وجود درد']
                        }
                        ]
                    }
                } ,
                'warning': {
                    'summary': 'having a warning',
                    'description': 'Insurance is not granted',
                    'value':{
                        'exception' : True,
                        'drugs': [
                            {
                            'drugId': '897986' ,
                            'drugName': 'ADAPALENE/BENZOYL PEROXIDE  0.1 %/2.5 % TOPICAL GEL',
                            'exceptionType': 'warning', 
                            'exceptionMsg' : ['سقف پذیرش بیمه پر شده و تمامی هزینه ها به صورت آزاد محاسبه میشود']
                        }
                        ]
                    }
                }
    }

    drug_query = {
                'match': {
                    'summary': 'Get a special item',
                    'description': 'If value is sent, Similar values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'match' : 'Ada'
                    }
                } ,

                'get_all': {
                    'summary': 'get all the items',
                    'description': 'If the value is empty, All values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'match':''
                    }
                }
    }

    drug_amnt_query = {
                'match': {
                    'summary': 'Get a special item',
                    'description': 'If value is sent, Similar values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'match' : 'قاشق غذاخوري'
                    }
                } ,

                'get_all': {
                    'summary': 'get all the items',
                    'description': 'If the value is empty, All values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'match':''
                    }
                }
    }    

    drug_instr_query = {
                'match': {
                    'summary': 'Get a special item',
                    'description': 'If value is sent, Similar values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'match' : 'صبح'
                    }
                } ,

                
                'get_all': {
                    'summary': 'get all the items',
                    'description': 'If the value is empty, All values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'match':''
                    }
                }
    }    


@router.get("/drug" ,response_model= List[DrugQuery_ResponseModel]) 
async def drug_query(match: drugQueryModel= Body(... ,examples= Examples.drug_query)):
    
    ls_match = await redis._zscan('doctor:' , match)
    ls_match = await redis._zscan('GlobalDrug' , match)
    return ls_match

@router.get("/drug-amnt" ,response_model= List[DrugAmntQuery_ResponseModel]) 
async def drug_amnt_query(match: drugAmntQueryModel= Body(... ,examples= Examples.drug_amnt_query )):
    
    ls_match = await redis._zscan('GlobalDrugAmnt' , match)
    return ls_match

@router.get("/drug-inst" ,response_model= List[DrugInstrQuery_ResponseModel]) 
async def drug_instr_query(match: drugInstrQueryModel= Body(... ,examples= Examples.drug_instr_query)):

    ls_match = await redis._zscan('GlobalDrugInstr' , match)
    return ls_match 


@router.get("/drug/check" ,response_model= CheckDrug_ResponseModel)  
async def check_drugs(match: CheckDrugModel= Body(... )):

    ls_match = await redis._zscan('GlobalDrugInstr' , match)
    return ls_match 


