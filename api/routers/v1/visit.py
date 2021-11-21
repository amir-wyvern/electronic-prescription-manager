from typing import Dict
from fastapi import APIRouter ,Depends, HTTPException ,Path ,Body
from fastapi.param_functions import File
from pydantic import BaseModel ,Field

router = APIRouter(
    prefix="/v1/visit",
    tags=["Visit"]
    )

class VisitModel(BaseModel):

    doctorId        : str 
    patientId        : str 


class VisitResponse(BaseModel):
    
    prescCode : str 


@router.post("/" ,response_model= VisitResponse)
async def visitRegister(item :VisitModel = Body(...)):
    return item



