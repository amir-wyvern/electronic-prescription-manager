from fastapi import APIRouter ,Body
from pydantic import BaseModel ,Field 
from typing import List, Optional


router = APIRouter(
    prefix="/v1/presc",
    tags=["Prescription"]
    )

class DrugsModel(BaseModel):

    code     : str 
    drugAmnt : str
    drugQty  : str
    number   : str


class ExperimentationModel(BaseModel):
    
    code   : str
    number : str


class ImageingModel(BaseModel):
    code   : str
    number : str


class ServicesModel(BaseModel):

    code   : str
    number : str


class PhysiotherapyModel(BaseModel):

    id     : str
    number : str


class ReferenceModel(BaseModel):
    id     : str
    number : str


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



@router.post("/" ,response_model= PrescriptionResponseModel) 
async def save_prescription(item: PrescriptionRequestModel= Body(...)):
    return item

