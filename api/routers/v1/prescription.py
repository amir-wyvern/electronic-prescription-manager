from fastapi import APIRouter ,Body
from pydantic import BaseModel ,Field 
from typing import List, Optional


router = APIRouter(
    prefix="/v1/presc",
    tags=["Prescription"]
    )

# ===== Drug =====
class DrugDetailModel(BaseModel):

    drugAmntId      : str
    drugInstId      : str
    numberOfRequest :str

class DrugPrescModel(BaseModel):
    
    doctorId      : str
    patientId     : str
  
    serviceId     : str 
    description   : str
    ServiceDetail : DrugDetailModel

    otherServices : List


# ===== Experimentation =====
class ExperDetailModel(BaseModel):

    numberOfRequest :str

class ExperModel(BaseModel):

    doctorId      : str
    patientId     : str
  
    serviceId     : str 
    description   : str
    ServiceDetail : ExperDetailModel

    otherServices : List


# ===== Imaging =====
class ImageingDetailModel(BaseModel):

    numberOfRequest :str

class ImageingModel(BaseModel):

    doctorId      : str
    patientId     : str
  
    serviceId     : str 
    description   : str
    ServiceDetail : ImageingDetailModel

    otherServices : List


# ===== Service =====
class ServicesDetailModel(BaseModel):

    numberOfRequest :str

class ServicesModel(BaseModel):

    doctorId      : str
    patientId     : str
  
    serviceId     : str 
    description   : str
    ServiceDetail : ServicesDetailModel

    otherServices : List


# ===== Physiotherapy =====
class PhysioDetailModel(BaseModel):

    numberOfRequest :str

class PhysioModel(BaseModel):

    doctorId      : str
    patientId     : str
  
    serviceId     : str 
    description   : str
    ServiceDetail : PhysioDetailModel

    otherServices : List


# ===== Reference =====
class ReferenceDetailModel(BaseModel):

    numberOfRequest :str

class ReferenceModel(BaseModel):

    doctorId      : str
    patientId     : str
  
    serviceId     : str 
    description   : str
    ServiceDetail : ReferenceDetailModel

    otherServices : List


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


@router.post("/drug" ) 
async def drug_prescription(item: DrugPrescModel= Body(...)):
    return item

@router.post("/exper" ,response_model= DrugPrescModel) 
async def experimentation_prescription(item: ExperModel= Body(...)):
    return item

@router.post("/physio" ,response_model= DrugPrescModel) 
async def physiotherapy_prescription(item: PhysioModel= Body(...)):
    return item

@router.post("/imaging" ,response_model= ImageingModel) 
async def imaging_prescription(item: ImageingModel= Body(...)):
    return item

@router.post("/service" ,response_model= DrugPrescModel) 
async def service_prescription(item: ServicesModel= Body(...)):
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




