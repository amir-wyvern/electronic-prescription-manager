from fastapi import Depends, FastAPI

# from .dependencies import get_query_token, get_token_header

from .routers import patient
from .routers import login
from .routers import services
from .routers import doctor
from .async_redis import redis

REDIS_HOST = 'localhost'
REDIS_PORT = '6379'

api = FastAPI()

api.include_router(patient.router)
api.include_router(login.router)
api.include_router(services.router)
api.include_router(doctor.router)


@api.on_event("startup")
async def startup_event():
    
    redis.connect(REDIS_HOST ,REDIS_PORT)

@api.on_event("shutdown")
async def startup_event():
    
    await redis.close()

