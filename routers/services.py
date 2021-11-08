from typing import Dict, List
from fastapi import APIRouter ,Body
from pydantic import BaseModel ,Field
from pydantic.errors import BytesError
from async_redis.redis_obj import redis

from logs import Logger
logger = Logger()

router = APIRouter(
    prefix="/services",
    tags=["services"]
    )

class drugQueryModel(BaseModel):

    match     : str = Field(... ,max_length=150 )


class drugAmntQueryModel(BaseModel):

    match     : str = Field(... ,max_length=150 )


class drugInstrQueryModel(BaseModel):

    match     : str = Field(... ,max_length=150 )


class ServiceType(BaseModel):

    srvType      : str = Field(... ,example= '01')
    srvTypeDes   : str = Field(... ,example= 'دارویی')
    status       : str = Field(... ,example= '1')
    statusstDate : str = Field(... ,example= '13940101')
    custType     : str = Field(... ,example= '3')


class DrugQuery_ResponseModel(BaseModel):

    agreementFlag     : str
    bGType            : str = Field(... ,example= '1')
    dentalServiceType : str
    doseCode          : str
    gSrvCode          : str
    hosprescType      : str
    srvName           : str = Field(... ,example= 'ADAPALENE/BENZOYL PEROXIDE  0.1 %/2.5 % TOPICAL GEL')
    srvName2          : str
    srvPrice          : int = Field(... ,example= 0)
    srvPriceDate      : str = Field(... ,example= '13980216')
    isDeleted         : str
    parTarefGrp       : str
    srvBimSw          : str = Field(... ,example= '2')
    srvCode           : str = Field(... ,example= '52198')
    srvCodeComplete   : str = Field(... ,example= '0000052198')
    srvId             : int = Field(... ,example= 183957)
    srv_id            : str 
    status            : str = Field(... ,example= '2')
    statusstDate      : str = Field(... ,example= '13980216')
    visible           : str = Field(... ,example= '1')
    wsSrvCode         : str = Field(... ,example= '52198')

    srvType           : ServiceType


class DrugAmntQuery_ResponseModel(BaseModel):

    drugAmntId      : int = Field(... ,example=  14)
    drugAmntCode    : str = Field(... ,example= '14')
    drugAmntSumry   : str
    drugAmntLatin   : str
    drugAmntConcept : str = Field(... ,example= 'دو (2)  قاشق غذاخوري (10 سي سي)')


class DrugInstrQuery_ResponseModel(BaseModel):
   
    drugInstId      : str = Field(... ,example= 9)
    drugInstCode    : str = Field(... ,example= '9')
    drugInstSumry   : str = Field(... ,example= 'A.M')
    drugInstLatin   : str = Field(... ,example= 'ante meridiem')
    drugInstConcept : str = Field(... ,example= 'صبح، پيش از ظهر')


class Examples:

    drug_query = {
                'match': {
                    'summary': 'Get a special item',
                    'description': 'If value is sent, Similar values will be returned',
                    'value':{
                        'doctor_id':'98789' ,
                        'match' : 'Ada'
                    }
                } ,

                'get_all': {
                    'summary': 'get all the items',
                    'description': 'If the value is empty, All values will be returned',
                    'value':{
                        'doctor_id' : '98789' ,
                        'match':''
                    }
                }
    }

    drug_amnt_query = {
                'match': {
                    'summary': 'Get a special item',
                    'description': 'If value is sent, Similar values will be returned',
                    'value':{
                        'doctor_id':'98789' ,
                        'match' : 'قاشق غذاخوري'
                    }
                } ,

                'get_all': {
                    'summary': 'get all the items',
                    'description': 'If the value is empty, All values will be returned',
                    'value':{
                        'doctor_id' : '98789' ,
                        'match':''
                    }
                }
    }    

    drug_instr_query = {
                'match': {
                    'summary': 'Get a special item',
                    'description': 'If value is sent, Similar values will be returned',
                    'value':{
                        'doctor_id':'98789' ,
                        'match' : 'صبح'
                    }
                } ,

                'get_all': {
                    'summary': 'get all the items',
                    'description': 'If the value is empty, All values will be returned',
                    'value':{
                        'doctor_id' : '98789' ,
                        'match':''
                    }
                }
    }    

    check_drgus = {
                'check': {
                    'summary': 'check drugs',
                    'description': '',
                    'value':{

                        'doctor_id':'98789' ,
                    }
                } ,

    }    

@router.get("/drugs" ,response_model= List[DrugQuery_ResponseModel]) 
async def drug_query(match: drugQueryModel= Body(... ,examples= Examples.drug_query)):
    
    ls_match = await redis._zscan('GlobalDrug' , match)
    return ls_match


@router.get("/drug-amnt" ,response_model= List[DrugAmntQuery_ResponseModel]) 
async def drug_amnt_query(match: drugAmntQueryModel= Body(... ,examples= Examples.drug_amnt_query )):
    
    ls_match = await redis._zscan('GlobalDrugAmnt' , match)
    return ls_match

@router.get("/drug-instr" ,response_model= List[DrugInstrQuery_ResponseModel]) 
async def drug_instr_query(match: drugInstrQueryModel= Body(... ,examples= Examples.drug_instr_query)):

    ls_match = await redis._zscan('GlobalDrugInstr' , match)
    return ls_match 


