from fastapi import FastAPI

from api.endpoints import api_router
from settings import URL_PREFIX

app = FastAPI(title="js-assigment")

app.include_router(api_router, prefix=URL_PREFIX)
