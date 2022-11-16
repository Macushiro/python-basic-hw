"""
    Description: Main module for API.
    To run this service locally, just execute this command in terminal:  uvicorn main:app
    To run this service in docker, just execute this command in terminal:  docker run -it -p 8000:8000 app
"""
from fastapi import APIRouter, FastAPI

from views.base_route import router


app = FastAPI()
app.include_router(router)