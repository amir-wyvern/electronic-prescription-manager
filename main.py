from fastapi import Depends, FastAPI

# from .dependencies import get_query_token, get_token_header

from routers import patient
from routers import login
from routers import services
from routers import doctor
from async_redis import redis



REDIS_HOST = 'localhost'
REDIS_PORT = '6379'

app = FastAPI()

app.include_router(patient.router)
app.include_router(login.router)
app.include_router(services.router)
app.include_router(doctor.router)


@app.on_event("startup")
async def startup_event():
    
    redis.connect(REDIS_HOST ,REDIS_PORT)

@app.on_event("shutdown")
async def startup_event():
    
    await redis.close()

