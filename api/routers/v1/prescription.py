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

class DrugDetailModel(BaseModel):

    drugAmnt : str
    drugInnst : str
    numberOfDrug :str

class DrugPrescModel(BaseModel):
    
    doctorId : str
    patientId : str

    drugId :str 
    description : str
    detailDrug : DrugDetailModel


@router.post("/drug" ) 
async def drug_prescription(item: DrugPrescModel= Body(...)):
    return item

@router.post("/exper" ,response_model= DrugPrescModel) 
async def experimentation_prescription(item: PrescriptionRequestModel= Body(...)):
    return item

@router.post("/physio" ,response_model= DrugPrescModel) 
async def physiotherapy_prescription(item: PrescriptionRequestModel= Body(...)):
    return item

@router.post("/imaging" ,response_model= DrugPrescModel) 
async def imaging_prescription(item: PrescriptionRequestModel= Body(...)):
    return item

@router.post("/service" ,response_model= DrugPrescModel) 
async def service_prescription(item: PrescriptionRequestModel= Body(...)):
    return item

# @router.post("/refrence" ,response_model= DrugPrescModel) 
# async def refrence_prescription(item: PrescriptionRequestModel= Body(...)):
#     return item

@router.post("/submit" ,response_model= DrugPrescModel) 
async def save_prescription(item: PrescriptionRequestModel= Body(...)):
    return item


class PrescriptionDeleteModel(BaseModel):

    prescId : str
    doctorId : str

class PrescriptionDeleteModel(BaseModel):

    prescId : str
    doctorId : str
    prescription : PrescriptionModel

@router.delete("/delete" ) 
async def delete_prescription(item: PrescriptionDeleteModel= Body(...)):
    return item

@router.put("/update" ) 
async def update_prescription(item: PrescriptionRequestModel= Body(...)):
    return item

@router.get("/detail" ) 
async def detail_prescription(item: PrescriptionRequestModel= Body(...)):
    return item




