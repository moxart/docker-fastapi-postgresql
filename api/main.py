from typing import Union

from fastapi import FastAPI

api = FastAPI()


@api.get("/")
def index():
    return {"Hello": "World"}
