FROM python:3.9

WORKDIR /epm

COPY ./requirements.txt /epm/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /epm/requirements.txt
COPY ./api /epm/api
CMD uvicorn  api.main:api --host 0.0.0.0 --port 80
