from fastapi import APIRouter ,Body
from pydantic import BaseModel ,Field

from routers import patient

router = APIRouter(
    prefix="/presc",
    tags=["presc"]
    )

class DrugsModel(BaseModel):

    drugName : str 


class SendPrescriptionModel(BaseModel):
    
    patientId : str = Field(...)
    doctorId  : str = Field(...)
    drugId    : list = Field(...)

@router.post("/asdrug") 
async def send_prescription(item: SendPrescriptionModel= Body(...)):

    return item


# {
# "id":int,
# "serviceId":int,
# "consumption":String,
# "shape":String,
# "consumptionInstruction":String,
# "numberOfRequest":int,
# "numberOfPeriod":int,
# "description":String,
# "checkCode":String
# }

#     "noteDetailEprscs": [
#         {
#             "srvId": {
#                 "srvType": {
#                     "srvType": "01"
#                 },
#                 "srvCode": "00694"
#             },
#             "srvQty": 1,
#             "timesAday": {
#                 "drugAmntId": 1
#             },
#             "repeat": null,
#             "drugInstruction": {
#                 "drugInstId": 5
#             }
#         }
#     ]


# "nationalNumber"