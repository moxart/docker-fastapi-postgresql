from typing import Union

from fastapi import FastAPI

from .config.db import database

api = FastAPI()


@api.on_event("startup")
async def startup():
    await database.connect()


@api.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@api.get("/")
async def index():
    data = {"Hello": "World"}
    
    return data
