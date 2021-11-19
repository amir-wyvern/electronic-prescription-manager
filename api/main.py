from fastapi import Depends, FastAPI

from api.routers import prescription

# from .dependencies import get_query_token, get_token_header

from .routers import patient
from .routers import login
from .routers import services
from .routers import doctor
from .async_redis import redis

REDIS_HOST = 'localhost'
REDIS_PORT = '6379'


description = """
### *Electronic Prescription Manager*
*epm is a interface api that allows the registration and management of electronic prescriptions
It also has other facilities such as better clinic management and patient medical records*

### *Features*
- *Register ,Edit & Remove electronic prescription*
- *Clinic management*
- ✨ *Patient medical record*✨

> *This version is still under development* 
> *and some of its features may not work*
 
  """

api = FastAPI( 
        title="EPM Backend",
        description=description,
        version="0.0.1",
        docs_url = '/docs',  # swagger UI
        redoc_url ='/'     # Redoc UI
)

api.include_router(patient.router)
api.include_router(login.router)
api.include_router(services.router)
api.include_router(doctor.router)
api.include_router(prescription.router)


@api.on_event("startup")
async def startup_event():
    
    redis.connect(REDIS_HOST ,REDIS_PORT)

@api.on_event("shutdown")
async def startup_event():
    
    await redis.close()

