from os import name
from typing import Dict, List, Optional
from fastapi import APIRouter ,Body ,Query
from pydantic import BaseModel ,Field
from api.models.SERVICE_MODEL import TaminDrugs 
from api.models.FAVORIT_MODEL import FavoritDrug

from async_redis.redis_obj import redis
import logging

from insuranceAPI.insurance_handler import TaminHandler

router = APIRouter(
    prefix="/v1/srvc",
    tags=["Services"]
    )


# ===== Drug =====

class DrugModel(BaseModel):

    class FavoritModel(BaseModel):

        drugAmntName : Optional[str] = Field(... ,example= 'یک واحد')
        drugAmntId : Optional[str] = Field(... ,example= '23')
        drugInstName : Optional[str] = Field(... ,example= 'یک بار در روز')
        drugInstId : Optional[str] = Field(... ,example= '69')
        numberOfRequest : Optional[int] = Field(... ,example= 1)

    id      : str = Field(... ,example= '8786522')
    name    : str = Field(... ,example= 'ANTI-D‬‬ ‫‪IMMUNOGLOBULIN‬‬ ‫‪INJECTION‬‬ INTRAMUSCULAR‬‬‫‪') 
    favorit :   Optional[List[FavoritModel]]

class DrugQuery_ResponseModel(BaseModel):

    data : List[DrugModel] 


# ===== Physiotherapy =====

class PhysioModel(BaseModel):

    class FavoritModel(BaseModel):

        numberOfRequest : Optional[int] = Field(... ,example= 1)

    id      : str = Field(... ,example= '4352234')
    name    : str = Field(... ,example= 'اسکن استاتيک کف پا (Foot Scan) براي تعيين نقاط فشاري کف پا و تجويز کفي و يا اورتز مناسب')
    favorit : Optional[List[FavoritModel]] 

class PhysiotherapyQuery_ResponseModel(BaseModel):

    data : List[PhysioModel]


# ===== Imaging =====

class ImagingModel(BaseModel):

    class FavoritModel(BaseModel):

        numberOfRequest : Optional[int] = Field(... ,example= 1)

    id      : str = Field(... ,example= '798454')
    name    : str = Field(... ,example= 'سي تي اسکن ساق پا چپ بدون کنتراست') 
    favorit : Optional[List[FavoritModel]] 

class ImagingQuery_ResponseModel(BaseModel):

    data : List[ImagingModel]


# ===== Doctor Service =====

class DocServiceModel(BaseModel):

    class FavoritModel(BaseModel):

        numberOfRequest : Optional[int] = Field(... ,example= 1)

    id  : str = Field(... ,example= '521692')
    name    : str = Field(... ,example= 'پوستچروگرافي ديناميک کامپيوتري (صندلي چرخان)')
    favorit : Optional[List[FavoritModel]] 
    
class DocServiceQuery_ResponseModel(BaseModel):

    data : List[DocServiceModel]


# ===== Experimentation =====

class ExperModel(BaseModel):

    class FavoritModel(BaseModel):

        numberOfRequest : Optional[int] = Field(... ,example= 1)

    id      : str = Field(... ,example= '3453662') 
    name    : str = Field(... ,example= 'اندازه گيري کمّي نوراپي نفرين در خون/سرم/پلاسما') 
    favorit : Optional[List[FavoritModel]] 

class ExperimentationQuery_ResponseModel(BaseModel):

    data : List[ExperModel]


# ===== Drug Amount =====
class DrugAmntModel(BaseModel):
    
    id : str = Field(... ,example= '465468')
    name : str = Field(... ,example= 'یک واحد')

class DrugAmntQuery_ResponseModel(BaseModel):

    drugAmnt : List[DrugAmntModel]


# ===== Drug Instruction =====
class DrugInstModel(BaseModel):

    id   : str = Field(... ,example= '3452342')
    name : str = Field(... ,example= 'یک بار در روز')

class DrugInstQuery_ResponseModel(BaseModel):
   
   drugInst : List[DrugInstModel]


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
async def drug_query(patientId : str = Query(None, min_length=3, max_length=60 ,example= 'bba18866-5bd8-4264-9e0d-4d91190688bb') ,
                    doctorId : str = Query(None, min_length=3, max_length=60 ,example= '640b4ea5-69b4-46a1-a97f-0405aaee6474'),
                    clause : str = Query(None, min_length=1, max_length=60 ,example= 'ANTY')):

    # if patient insurance is tamin 
    # ****
    # if patient insurance is salamat

    resSearch = await TaminHandler().getDrugs(clause)
    resFav = await FavoritDrug(doctorId= doctorId).getFavorit((5,))
    lsDrugs = []
    for name ,_id in resSearch :
        lsDrugs.append({
            'id' : _id,
                'name' : name,
                'favorit' : resFav
                #  [
                    # {
                    #     'drugInstName' : 'یک بار در روز' ,
                    #     'drugInstId' : '69' ,
                    #     'drugAmntName' : 'یک واحد',
                    #     'drugAmntId' : '23',
                    #     'numberOfRequest' : 1
                    # }
                # ]
        })

    resp = {
        'data' : lsDrugs
    }
    return resp
    

@router.get("/drug-amnt" ,response_model= DrugAmntQuery_ResponseModel) 
async def drug_amnt_query(patientId : str = Query(None, min_length=3, max_length=60 ,example= 'bba18866-5bd8-4264-9e0d-4d91190688bb') ,
                        doctorId : str = Query(None, min_length=3, max_length=60 ,example= '640b4ea5-69b4-46a1-a97f-0405aaee6474')):
    
    resSearch = await TaminHandler().getDrugAmnt()
    resp = {
        'drugAmnt': resSearch
    }
    return resp


@router.get("/drug-inst" ,response_model= DrugInstQuery_ResponseModel) 
async def drug_instr_query(patientId : str = Query(None, min_length=3, max_length=60 ,example= 'bba18866-5bd8-4264-9e0d-4d91190688bb') ,
                        doctorId : str = Query(None, min_length=3, max_length=60 ,example= '640b4ea5-69b4-46a1-a97f-0405aaee6474')):

    resSearch = await TaminHandler().getDrugInst()
    resp = {
        'drugInst': resSearch
    }
    return resp


@router.get("/exper" ,response_model= ExperimentationQuery_ResponseModel) 
async def experimentation_query(patientId : str = Query(None, min_length=3, max_length=60 ,example= 'bba18866-5bd8-4264-9e0d-4d91190688bb') ,
                    doctorId : str = Query(None, min_length=3, max_length=60 ,example= '640b4ea5-69b4-46a1-a97f-0405aaee6474'),
                    clause : str = Query(None, min_length=1, max_length=60 ,example= 'اندازه')):

    ExperimentationQuery_ResponseModel = {
        'data': [
            {
                'id' : '3453662' ,
                'name' : 'اندازه گيري کمّي نوراپي نفرين در خون/سرم/پلاسما',
                'favorit' : [
                    {
                        'numberOfRequest' : 1
                    }
                ]  
            }
        ]
    } 

    return ExperimentationQuery_ResponseModel


@router.get("/physio" ,response_model= PhysiotherapyQuery_ResponseModel) 
async def physiotherapy_query(patientId : str = Query(None, min_length=3, max_length=60 ,example= 'bba18866-5bd8-4264-9e0d-4d91190688bb') ,
                    doctorId : str = Query(None, min_length=3, max_length=60 ,example= '640b4ea5-69b4-46a1-a97f-0405aaee6474'),
                    clause : str = Query(None, min_length=1, max_length=60 ,example= 'کف پا')):
    
    PhysiotherapyQuery_ResponseModel = {
        'data': [
            {
                'id' : '4352234' ,
                'name' : 'اندازه گيري کمّي نوراپي نفرين در خون/سرم/پلاسما',
                'favorit' : [
                    {
                        'numberOfRequest' : 1
                    }
                ]  
            }
        ]
    } 

    return PhysiotherapyQuery_ResponseModel


@router.get("/imaging" ,response_model= ImagingQuery_ResponseModel) 
async def imaging_query(atientId : str = Query(None, min_length=3, max_length=60 ,example= 'bba18866-5bd8-4264-9e0d-4d91190688bb') ,
                    doctorId : str = Query(None, min_length=3, max_length=60 ,example= '640b4ea5-69b4-46a1-a97f-0405aaee6474'),
                    clause : str = Query(None, min_length=1, max_length=60 ,example= 'ساق پا')):
    
    ImagingQuery_ResponseModel = {
        'data': [
            {
                'id' : '798454' ,
                'name' : 'سي تي اسکن ساق پا چپ بدون کنتراست',
                'favorit' : [
                    {
                        'numberOfRequest' : 1
                    }
                ]  
            }
        ]
    } 

    return ImagingQuery_ResponseModel


@router.get("/service" ,response_model= DocServiceQuery_ResponseModel) 
async def service_query(atientId : str =  Query(None, min_length=3, max_length=60 ,example= 'bba18866-5bd8-4264-9e0d-4d91190688bb') ,
                    doctorId : str = Query(None, min_length=3, max_length=60 ,example= '640b4ea5-69b4-46a1-a97f-0405aaee6474'),
                    clause : str = Query(None, min_length=1, max_length=60 ,example= 'پوستچروگرا')):
    
    DocServiceQuery_ResponseModel = {
        'data': [
            {
                'id' : '521692' ,
                'name' : 'پوستچروگرافي ديناميک کامپيوتري (صندلي چرخان)',
                'favorit' : [
                    {
                        'numberOfRequest' : 1
                    }
                ]  
            }
        ]
    } 

    return DocServiceQuery_ResponseModel


