from os import error, name
from typing import Dict, List
from fastapi import APIRouter ,Body
from fastapi.param_functions import Query
from pydantic import BaseModel ,Field
from pydantic.errors import BytesError
from async_redis.redis_orm import redis

import logging
router = APIRouter(
    prefix="/v1/doctor",
    tags=["doctor"]
    )


@router.get("/presc")  
async def history_presc():#match: CheckDrugModel= Query(None )):

    ls_match = await redis._zscan('GlobalDrugInstr' )
    return ls_match 




