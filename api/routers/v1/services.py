from os import name
from typing import Dict, List, Optional
from fastapi import APIRouter ,Body ,Query
from pydantic import BaseModel ,Field

from async_redis.redis_obj import redis
import logging

router = APIRouter(
    prefix="/v1/srvc",
    tags=["Services"]
    )


class drugQueryModel(BaseModel):

    patientId  : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId   : str = Field(... ,min_length=1 ,max_length=30 )
    clause     : str = Field(... ,max_length=150 )


class drugAmntQueryModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )


class drugInstrQueryModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    clause     : str = Field(... ,max_length=150 )

class PhysiotherapyModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    clause     : str = Field(... ,max_length=150 )    

class ImagingModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    clause     : str = Field(... ,max_length=150 )    


class ServiceModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    clause     : str = Field(... ,max_length=150 )    


class ServiceType(BaseModel):

    srvType      : str = Field(... ,example= '01')
    srvTypeDes   : str = Field(... ,example= 'دارویی')
    status       : str = Field(... ,example= '1')
    statusstDate : str = Field(... ,example= '13940101')
    custType     : str = Field(... ,example= '3')


class DrugFavoritModel(BaseModel):

    drugAmnt : Optional[str]
    drugInnst : Optional[str]
    numberOfDrug : Optional[str]

class DrugModel(BaseModel):

    id      : str = Field(... ,example= '8786522')
    name    : str = Field(... )
    favorits :   Optional[List[DrugFavoritModel]]

class DrugQuery_ResponseModel(BaseModel):

    drugs : List[DrugModel]


class PhysiotherapyModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    clause     : str = Field(... ,max_length=150 )    

class PhysioFavoritModel(BaseModel):

    id : Optional[str]
    name : Optional[str]

class PhysiotherapyQuery_ResponseModel(BaseModel):

    id  : str = Field(... ,example= '183957')
    name    : str = Field(... )
    favorit : Optional[List[PhysioFavoritModel]] 


class ImagingModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    clause     : str = Field(... ,max_length=150 )    

class ImagingFavoritModel(BaseModel):

    id : Optional[str]
    name : Optional[str]

class ImagingQuery_ResponseModel(BaseModel):

    id  : str = Field(... ,example= '183957')
    name    : str = Field(... )
    favorit : Optional[List[ImagingFavoritModel]] 


class DocServiceModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    clause     : str = Field(... ,max_length=150 )    

class DocServiceFavoritModel(BaseModel):

    id : Optional[str]
    name : Optional[str]

class DocServiceQuery_ResponseModel(BaseModel):

    id  : str = Field(... ,example= '183957')
    name    : str = Field(... )
    favorit : Optional[List[DocServiceFavoritModel]] 


class ExperimentationModel(BaseModel):

    patientId : str = Field(... ,min_length=1 ,max_length=30 )
    doctorId  : str = Field(... ,min_length=1 ,max_length=30 )
    clause     : str = Field(... ,max_length=150 )    
 
class ExperFavoritModel(BaseModel):

    id : Optional[str]
    name : Optional[str]

class ExperimentationQuery_ResponseModel(BaseModel):

    id  : str = Field(... ,example= '183957')
    name    : str = Field(... )
    favorit : Optional[List[ExperFavoritModel]] 


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
    name : str = Field(... ,example= 'دو (2)  قاشق غذاخوري (10 سي سي)')
    

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
                'clause': {
                    'summary': 'Get a special item',
                    'description': 'If value is sent, Similar values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'clause' : 'Ada'
                    }
                } ,

                'get_all': {
                    'summary': 'get all the items',
                    'description': 'If the value is empty, All values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'clause':''
                    }
                }
    }

    drug_amnt_query = {
                'clause': {
                    'summary': 'Get a special item',
                    'description': 'If value is sent, Similar values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'clause' : 'قاشق غذاخوري'
                    }
                } ,

                'get_all': {
                    'summary': 'get all the items',
                    'description': 'If the value is empty, All values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'clause':''
                    }
                }
    }    

    drug_instr_query = {
                'clause': {
                    'summary': 'Get a special item',
                    'description': 'If value is sent, Similar values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'clause' : 'صبح'
                    }
                } ,

                
                'get_all': {
                    'summary': 'get all the items',
                    'description': 'If the value is empty, All values will be returned',
                    'value':{
                        'patientId' : 'bba18866-5bd8-4264-9e0d-4d91190688bb',
                        'doctorId':'640b4ea5-69b4-46a1-a97f-0405aaee6474' ,
                        'clause':''
                    }
                }
    }    



@router.get("/drugs" ,response_model= DrugQuery_ResponseModel) 
async def drug_query(patientId : str =  Query(None, min_length=3, max_length=60) ,
                    doctorId : str = Query(None, min_length=3, max_length=60),
                    clause : str = Query(None, min_length=1, max_length=60)):

    # if patient insurance is tamin 
    # ****
    # if patient insurance is salamat

    # get drugs from database
    DrugQuery_ResponseModel = [{
        'id' : '4234234' ,
        'name' : 'estaminofin',
        'favorit' : [{
            'drugInst' : '1' ,
            'drugAmnt' : '2',
            'numberOfDrug' : '3'
        }]  
    }]
    
    return DrugQuery_ResponseModel


@router.get("/drug-amnt" ,response_model= List[DrugAmntQuery_ResponseModel]) 
async def drug_amnt_query(patientId : str =  Query(None, min_length=3, max_length=60) ,
                    doctorId : str = Query(None, min_length=3, max_length=60)):
    
    resp = [
        {'id':'2354564' ,'name': 'دو قاشق غذاخوری'}
    ]
    return resp


@router.get("/drug-instr" ,response_model= List[DrugInstrQuery_ResponseModel]) 
async def drug_instr_query(patientId : str =  Query(None, min_length=3, max_length=60) ,
                    doctorId : str = Query(None, min_length=3, max_length=60)):

    resp = [
        {'id':'3452342' ,'name': 'یک روز درمیان'}
    ]
    return resp 


@router.get("/experimentation" ,response_model= ExperimentationQuery_ResponseModel) 
async def experimentation_query(patientId : str =  Query(None, min_length=3, max_length=60) ,
                    doctorId : str = Query(None, min_length=3, max_length=60),
                    clause : str = Query(None, min_length=1, max_length=60)):
    
    ls_clause = await redis._zscan('GlobalDrug')
    return ls_clause

@router.get("/physiotherapy" ,response_model= PhysiotherapyQuery_ResponseModel) 
async def physiotherapy_query(patientId : str =  Query(None, min_length=3, max_length=60) ,
                    doctorId : str = Query(None, min_length=3, max_length=60),
                    clause : str = Query(None, min_length=1, max_length=60)):
    
    ls_clause = await redis._zscan('GlobalDrug' )
    return ls_clause

@router.get("/imaging" ,response_model= ImagingQuery_ResponseModel) 
async def imaging_query(patientId : str =  Query(None, min_length=3, max_length=60) ,
                    doctorId : str = Query(None, min_length=3, max_length=60),
                    clause : str = Query(None, min_length=1, max_length=60)):
    
    ls_clause = await redis._zscan('GlobalDrug')
    return ls_clause

@router.get("/service" ,response_model= DocServiceQuery_ResponseModel) 
async def service_query(patientId : str =  Query(None, min_length=3, max_length=60) ,
                    doctorId : str = Query(None, min_length=3, max_length=60),
                    clause : str = Query(None, min_length=1, max_length=60)):
    
    ls_clause = await redis._zscan('GlobalDrug')
    return ls_clause



# @router.get("/check" ,response_model= List[CheckDrug_ResponseModel]) 
# async def drug_instr_query(clause: CheckDrugModel= Body(... ,examples= Examples.check_drugs)):

#     ls_clause = await redis._zscan('GlobalDrugInstr' , clause)
#     return ls_clause 


