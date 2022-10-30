"""
    Description: Main module for API.
    To run this service, just execute this command in terminal:  uvicorn main:app
"""
from fastapi import APIRouter, FastAPI

from views.base_route import router


app = FastAPI()
app.include_router(router)