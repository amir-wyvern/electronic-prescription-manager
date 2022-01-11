from typing import Dict
from fastapi import APIRouter ,Depends, HTTPException ,Path ,Body ,status
from fastapi.param_functions import File
from pydantic import BaseModel ,Field
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

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
    # return item
    return JSONResponse(
        status_code= status.HTTP_404_NOT_FOUND,
        content= jsonable_encoder({"detail": 'The Doctor Id not found'}),
        ) 



