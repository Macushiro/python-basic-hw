"""
    Router for base functionality of API
"""
from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse
from datetime import datetime


router = APIRouter(
    tags=["Main"],
)


@router.get('/ping')
def main_response() -> JSONResponse:
    return JSONResponse(
        {
            "message": "pong",
        },
        status_code=status.HTTP_200_OK
    )

@router.get('/get_current_dts')
def get_current_time() -> JSONResponse:
    now = datetime.now()
    return JSONResponse(
        {
            "Current date is": now.strftime('%Y-%m-%d'),
            "Current time is": now.strftime('%H:%M:%S'),
        },
        status_code=status.HTTP_200_OK
    )