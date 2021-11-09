# EPM
## Electronic Prescription Manager

epm is a interface api that allows the registration and management of electronic prescriptions
It also has other facilities such as better clinic management and patient medical records


## Features

- Register ,Edit & Remove electronic prescription
- Clinic management
- ✨ Patient medical record✨


> This version is still under development 
> and some of its features may not work
 
  
## Tech

EPM-backend uses a number of open source projects to work:

- [FastApi](https://fastapi.tiangolo.com) is a modern, fast (high-performance) web framework 
- [Uvicorn](https://www.uvicorn.org)  is a lightning-fast ASGI server implementation
- [Redis](https://redis.io) is an in-memory data structure store, used as a database & cache 


## Docker-Compose

>Images of Redis:latest and python:3.9 have been used ✔

```sh
docker-compose build
docker-compose up -d 
```


## Docs
Now you can go to [http://127.0.0.1/redoc](http://127.0.0.1/redoc) or [http://127.0.0.1/docs](http://127.0.0.1/docs)

Please make sure to update as appropriate.