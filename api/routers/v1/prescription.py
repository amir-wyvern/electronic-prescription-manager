from fastapi import APIRouter ,Body ,status ,Query
from pydantic import BaseModel ,Field 
from typing import List, Optional
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router = APIRouter(
    prefix="/v1/presc",
    tags=["Prescription"]
    )

class BaseDocModel(BaseModel):
    
    doctorId : str
    patientId: str

# ===== Drug =====
class DrugSrvcModel(BaseModel):

    class DetailModel(BaseModel):

        drugAmntId      : str
        drugInstId      : str
        numberOfRequest :str
        description   : str

    serviceId     : str 
    serviceDetail : DetailModel

class DrugPrescModel(DrugSrvcModel):
    
    doctorId      : str
    patientId     : str
    otherServices : List


# ===== Experimentation =====

class ExperSrvcModel(BaseModel):

    class DetailModel(BaseModel):

        numberOfRequest :str
        description   : str

    serviceId     : str 
    serviceDetail : DetailModel

class ExperModel(ExperSrvcModel):

    doctorId      : str
    patientId     : str
    otherServices : List


# ===== Imaging =====
class ImagingSrvcModel(BaseModel):

    class DetailModel(BaseModel):

        numberOfRequest :str
        description   : str

    serviceId     : str 
    serviceDetail : DetailModel

class ImageingModel(ImagingSrvcModel):

    doctorId      : str
    patientId     : str
    otherServices : List


# ===== Service =====
class ServicesSrvcModel(BaseModel):

    class DetailModel(BaseModel):

        numberOfRequest :str
        description   : str

    serviceId     : str 
    serviceDetail : DetailModel

class ServicesModel(ServicesSrvcModel):

    doctorId      : str
    patientId     : str
    otherServices : List


# ===== Physiotherapy =====

class PhysioSrvcModel(BaseModel):

    class DetailModel(BaseModel):

        numberOfRequest :str
        description   : str

    serviceId     : str 
    serviceDetail : DetailModel

class PhysioModel(PhysioSrvcModel):

    doctorId      : str
    patientId     : str
    otherServices : List


# ===== Reference =====

class ReferenceSrvcModel(BaseModel):

    class DetailModel(BaseModel):

        numberOfRequest :str
        description   : str

    serviceId     : str 
    serviceDetail : DetailModel

class ReferenceModel(ReferenceSrvcModel):

    doctorId      : str
    patientId     : str
    otherServices : List


class PrescriptionModel(BaseModel):
    
    experimentation : List#[ExperimentationModel]
    physiotherapy   : List#[PhysiotherapyModel]
    imaging         : List#[ImageingModel]
    drugs           : List#[DrugsModel]
    services        : List#[ServicesModel]
    # reference       : List[ReferenceModel]
 
class PrescriptionRequestModel(BaseModel):
    
    patientId     : str  = Field(...)
    doctorId      : str  = Field(...)
    prescription  : PrescriptionModel


class TotalPrescModel(BaseDocModel):

    class DetailModel(BaseModel):

        drug    : Optional[List[DrugSrvcModel]] 
        exper   : Optional[List[ExperSrvcModel]] 
        physio  : Optional[List[PhysioSrvcModel]] 
        imaging : Optional[List[ImagingSrvcModel]] 
        service : Optional[List[ServicesSrvcModel]] 

    presc : DetailModel


class CheckService_ResponseModel(BaseModel):

    class WarningModel(BaseModel):
        
        serviceId : str
        message   : str

    class ErrorModel(BaseModel):
        
        serviceId : str
        message   : str

    resultCode : int
    warnings : List[WarningModel]
    errors : List[ErrorModel]


class TotalPresc_ResponseModel(CheckService_ResponseModel):

    class PrescCodesList(BaseModel):

        prescNumber : str
        prescCode: str

    prescCodes : List[PrescCodesList]


@router.post("/drug" ,response_model= CheckService_ResponseModel) 
async def drug_prescription(item: DrugPrescModel= Body(...)):

    {
        'resultCode': 200 ,
        'warnings':[] ,
        'errors' : []
    }

    return CheckService_ResponseModel


@router.post("/exper" ,response_model= CheckService_ResponseModel) 
async def experimentation_prescription(item: ExperModel= Body(...)):
    return CheckService_ResponseModel


@router.post("/physio" ,response_model= CheckService_ResponseModel) 
async def physiotherapy_prescription(item: PhysioModel= Body(...)):
    return CheckService_ResponseModel


@router.post("/imaging" ,response_model= CheckService_ResponseModel) 
async def imaging_prescription(item: ImageingModel= Body(...)):
    return CheckService_ResponseModel


@router.post("/service" ,response_model= CheckService_ResponseModel) 
async def service_prescription(item: ServicesModel= Body(...)):
    return CheckService_ResponseModel


# @router.post("/refrence" ,response_model= DrugPrescModel) 
# async def refrence_prescription(item: PrescriptionRequestModel= Body(...)):
#     return item


@router.post("/submit" ,response_model= TotalPresc_ResponseModel) 
async def save_prescription(item: TotalPrescModel= Body(...)):

    return JSONResponse(
            status_code= status.HTTP_404_NOT_FOUND,
            content= jsonable_encoder({"detail": 'The Doctor Id not found'}),
            ) 

    # return TotalPresc_ResponseModel


class PrescDeleteModel(BaseModel):

    prescId : str
    doctorId : str

class PrescDelete_ResponseModel(BaseModel):
    
    message : str


class PrescUpdateModel(TotalPrescModel):

    prescId : str

class PrescUpdate_ResponseModel(BaseModel):
    pass

class PrescDetailModel(BaseModel):

    doctorId : str
    prescId : str

class PrescDetail_ResponseModel(BaseModel):
    
    pass


@router.delete("/delete" ,response_model= PrescDelete_ResponseModel) 
async def delete_prescription(item: PrescDeleteModel= Body(...)):
    # return item
    return JSONResponse(
        status_code= status.HTTP_404_NOT_FOUND,
        content= jsonable_encoder({"detail": 'The Doctor Id not found'}),
        ) 


@router.put("/update" ,response_model= TotalPresc_ResponseModel) 
async def update_prescription(item: PrescUpdateModel= Body(...)):
    # return item
    return JSONResponse(
        status_code= status.HTTP_404_NOT_FOUND,
        content= jsonable_encoder({"detail": 'The Doctor Id not found'}),
        ) 


@router.get("/detail") 
async def detail_prescription(
                            doctorID: str = Query(
                                        None ,max_length=50 , min_length=2 ,regex='[0-9]+' ,example= '640b4ea5-69b4-46a1-a97f-0405aaee6474') ,
                            prescId : str = Query(
                                        None ,max_length=50 , min_length=1 ,example='640b4ea5-69b4' ) ):
    # return item
    return JSONResponse(
        status_code= status.HTTP_404_NOT_FOUND,
        content= jsonable_encoder({"detail": 'The Doctor Id not found'}),
        ) 





