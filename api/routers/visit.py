from typing import Dict
from fastapi import APIRouter ,Depends, HTTPException ,Path ,Body
from fastapi.param_functions import File
from pydantic import BaseModel ,Field

router = APIRouter(
    prefix="/visit",
    tags=["visit"]
    )

class VisitModel(BaseModel):

    national_number : str = Field(... ,max_length= 10 ,min_length= 10)
    numberphone     : str = Field(... ,max_length= 11 ,min_length= 11) 


class VisitResponse(BaseModel):
    
    prescCode : str 


@router.post("/" ,response_model= VisitResponse)
async def visitRegister(item :VisitModel = Body(...)):
    return item



