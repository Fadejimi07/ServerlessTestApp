from fastapi import FastAPI
import os
from src.env import config

MODE = config("MODE", default="testing")  # Default to 'prod' if not set
app = FastAPI()


@app.get("/")  # GET -> http method
def home_page():
    return {"Hello": "World", "mode": MODE}
