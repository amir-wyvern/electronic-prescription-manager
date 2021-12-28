from fastapi import Depends, FastAPI

from api.routers.v1 import prescription as presc_v1
import sys


dire = sys.path[0] + '/api/'
sys.path.insert(0, dire )

# from .dependencies import get_query_token, get_token_header
from routers.v1 import patient  as patient_v1
from routers.v1 import login    as login_v1
from routers.v1 import services as services_v1
# from routers.v1 import doctor   as doctor_v1
from routers.v1 import visit    as visit_v1

from async_redis.redis_obj import redis
from fastConfig import Swagger
from fastapi.middleware.cors import CORSMiddleware

REDIS_HOST = 'localhost'
REDIS_PORT = '6379'


api = FastAPI( 
    **Swagger.attrs
)

origins = ['*']

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

api.include_router(patient_v1.router)
api.include_router(login_v1.router)
api.include_router(services_v1.router)
# api.include_router(doctor_v1.router)
api.include_router(presc_v1.router)
api.include_router(visit_v1.router)


@api.on_event("startup")
async def startup_event():
    
    redis.connect(REDIS_HOST ,REDIS_PORT)


@api.on_event("shutdown")
async def startup_event():
    
    await redis.close()
