"""
    Router for base functionality of API
"""
from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse


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