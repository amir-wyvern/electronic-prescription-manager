from fastapi import APIRouter ,Body
from pydantic import BaseModel ,Field 
from typing import List, Optional


router = APIRouter(
    prefix="/v1/presc",
    tags=["Prescription"]
    )

class DrugsModel(BaseModel):

    id     : str 
    drugAmnt : str
    drugQty  : str
    number   : str
    description : str


class ExperimentationModel(BaseModel):
    
    id        : str
    number      : str
    description : str

class ImageingModel(BaseModel):

    id   : str
    number : str
    description : str


class ServicesModel(BaseModel):

    id   : str
    number : str
    description : str
    

class PhysiotherapyModel(BaseModel):

    id     : str
    number : str
    description : str


class ReferenceModel(BaseModel):

    id     : str
    number : str
    description : str


class PrescriptionModel(BaseModel):
    
    experimentation : List[ExperimentationModel]
    physiotherapy   : List[PhysiotherapyModel]
    imaging         : List[ImageingModel]
    drugs           : List[DrugsModel]
    services        : List[ServicesModel]
    # reference       : List[ReferenceModel]


class PrescriptionRequestModel(BaseModel):
    
    patientId     : str  = Field(...)
    doctorId      : str  = Field(...)
    prescription  : PrescriptionModel


class PrescriptionResponseModel(BaseModel):
    
    prescId : str


@router.post("/drug" ,response_model= PrescriptionResponseModel) 
async def drug_prescription(item: PrescriptionRequestModel= Body(...)):
    return item

@router.post("/exper" ,response_model= PrescriptionResponseModel) 
async def experimentation_prescription(item: PrescriptionRequestModel= Body(...)):
    return item

@router.post("/physio" ,response_model= PrescriptionResponseModel) 
async def physiotherapy_prescription(item: PrescriptionRequestModel= Body(...)):
    return item

@router.post("/imaging" ,response_model= PrescriptionResponseModel) 
async def imaging_prescription(item: PrescriptionRequestModel= Body(...)):
    return item

@router.post("/service" ,response_model= PrescriptionResponseModel) 
async def service_prescription(item: PrescriptionRequestModel= Body(...)):
    return item

# @router.post("/refrence" ,response_model= PrescriptionResponseModel) 
# async def refrence_prescription(item: PrescriptionRequestModel= Body(...)):
#     return item

@router.post("/submit" ,response_model= PrescriptionResponseModel) 
async def refrence_prescription(item: PrescriptionRequestModel= Body(...)):
    return item


class PrescriptionDeleteModel(BaseModel):

    prescId : str
    doctorId : str

class PrescriptionDeleteModel(BaseModel):

    prescId : str
    doctorId : str
    prescription : PrescriptionModel

@router.delete("/delete" ) 
async def save_prescription(item: PrescriptionDeleteModel= Body(...)):
    return item

@router.put("/update" ) 
async def save_prescription(item: PrescriptionRequestModel= Body(...)):
    return item

@router.get("/detail" ) 
async def detail_prescription(item: PrescriptionRequestModel= Body(...)):
    return item




