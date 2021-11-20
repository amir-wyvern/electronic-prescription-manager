from typing import Dict, List
from fastapi import APIRouter ,Body
from pydantic import BaseModel ,Field

from ..async_redis.redis_obj import redis

from ..logs import Logger
logger = Logger()

router = APIRouter(
    prefix="/srvc",
    tags=["Services"]
    )


class drugQueryModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    phrase     : str = Field(... ,max_length=150 )


class drugAmntQueryModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    phrase     : str = Field(... ,max_length=150 )


class drugInstrQueryModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    phrase     : str = Field(... ,max_length=150 )


class ExperimentationModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    phrase     : str = Field(... ,max_length=150 )    
    
class PhysiotherapyModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    phrase     : str = Field(... ,max_length=150 )    
class ImagingModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    phrase     : str = Field(... ,max_length=150 )    


class ServiceModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    phrase     : str = Field(... ,max_length=150 )    


class ServiceType(BaseModel):

    srvType      : str = Field(... ,example= '01')
    srvTypeDes   : str = Field(... ,example= 'دارویی')
    status       : str = Field(... ,example= '1')
    statusstDate : str = Field(... ,example= '13940101')
    custType     : str = Field(... ,example= '3')


class DrugQuery_ResponseModel(BaseModel):

    id      : str = Field(... ,example= '8786522')
    name    : str = Field(... )
    favorit : bool 

class PhysiotherapyQuery_ResponseModel(BaseModel):

    id      : str = Field(... ,example= '1332457')
    name    : str = Field(...)
    favorit : bool 
class ImagingQuery_ResponseModel(BaseModel):

    id      : str = Field(... ,example= '8975642')
    name    : str = Field(...)
    favorit : bool 
class ServiceQuery_ResponseModel(BaseModel):

    id      : str = Field(... ,example= '4568752')
    name    : str = Field(...)
    favorit : bool 



class ExperimentationQuery_ResponseModel(BaseModel):

    id  : str = Field(... ,example= '183957')
    name    : str = Field(... )
    favorit : bool 


class ItemCheckDrug(BaseModel):

    drugId : str = Field(... ,example= '897986')


class CheckDrugModel(BaseModel):
    
    doctorId    : str = Field(... ,example= '640b4ea5-69b4-46a1-a97f-0405aaee6474')
    patientId   : str = Field(... ,example= 'bba18866-5bd8-4264-9e0d-4d91190688bb')
    drugs       : List[ItemCheckDrug] 


class CheckDrug_ResponseModel(BaseModel):

    id            : str = Field(... ,example= '897986')
    drugName      : str = Field(... ,example= 'ADAPALENE/BENZOYL PEROXIDE  0.1 %/2.5 % TOPICAL GEL')
    exceptionType : str = Field(... ,example= 'error')
    exceptionMsg  : List = Field(... ,example= ['تداخل دارویی وجود درد']) 


class DrugAmntQuery_ResponseModel(BaseModel):

    id : str = Field(... ,example= '46546823')
    name       : str = Field(... ,example= 'دو (2)  قاشق غذاخوري (10 سي سي)')
    

class DrugInstrQuery_ResponseModel(BaseModel):
   
    id : str = Field(... ,example= '1354954')
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
                'phrase': {
                    'summary': 'Get a special item',
                    'description': 'If value is sent, Similar values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'phrase' : 'Ada'
                    }
                } ,

                'get_all': {
                    'summary': 'get all the items',
                    'description': 'If the value is empty, All values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'phrase':''
                    }
                }
    }

    drug_amnt_query = {
                'phrase': {
                    'summary': 'Get a special item',
                    'description': 'If value is sent, Similar values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'phrase' : 'قاشق غذاخوري'
                    }
                } ,

                'get_all': {
                    'summary': 'get all the items',
                    'description': 'If the value is empty, All values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'phrase':''
                    }
                }
    }    

    drug_instr_query = {
                'phrase': {
                    'summary': 'Get a special item',
                    'description': 'If value is sent, Similar values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'phrase' : 'صبح'
                    }
                } ,

                
                'get_all': {
                    'summary': 'get all the items',
                    'description': 'If the value is empty, All values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'phrase':''
                    }
                }
    }    



@router.get("/drugs" ,response_model= List[DrugQuery_ResponseModel]) 
async def drug_query(phrase: drugQueryModel= Body(... ,examples= Examples.drug_query)):
    
    ls_phrase = await redis._zscan('GlobalDrug' , phrase)
    return ls_phrase


@router.get("/drug-amnt" ,response_model= List[DrugAmntQuery_ResponseModel]) 
async def drug_amnt_query(phrase: drugAmntQueryModel= Body(... ,examples= Examples.drug_amnt_query )):
    
    ls_phrase = await redis._zscan('GlobalDrugAmnt' , phrase)
    return ls_phrase


@router.get("/drug-instr" ,response_model= List[DrugInstrQuery_ResponseModel]) 
async def drug_instr_query(phrase: drugInstrQueryModel= Body(...)):

    ls_phrase = await redis._zscan('GlobalDrugInstr' , phrase)
    return ls_phrase 


@router.get("/experimentation" ,response_model= List[ExperimentationQuery_ResponseModel]) 
async def experimentation_query(phrase: ExperimentationModel= Body(... )):
    
    ls_phrase = await redis._zscan('GlobalDrug' , phrase)
    return ls_phrase

@router.get("/physiotherapy" ,response_model= List[PhysiotherapyQuery_ResponseModel]) 
async def physiotherapy_query(phrase: PhysiotherapyModel= Body(... )):
    
    ls_phrase = await redis._zscan('GlobalDrug' , phrase)
    return ls_phrase

@router.get("/imaging" ,response_model= List[ImagingQuery_ResponseModel]) 
async def imaging_query(phrase: ImagingModel= Body(... )):
    
    ls_phrase = await redis._zscan('GlobalDrug' , phrase)
    return ls_phrase

@router.get("/service" ,response_model= List[ServiceQuery_ResponseModel]) 
async def service_query(phrase: ServiceModel= Body(... )):
    
    ls_phrase = await redis._zscan('GlobalDrug' , phrase)
    return ls_phrase



# @router.get("/check" ,response_model= List[CheckDrug_ResponseModel]) 
# async def drug_instr_query(phrase: CheckDrugModel= Body(... ,examples= Examples.check_drugs)):

#     ls_phrase = await redis._zscan('GlobalDrugInstr' , phrase)
#     return ls_phrase 


