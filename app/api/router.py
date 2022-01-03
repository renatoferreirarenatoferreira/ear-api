from fastapi import APIRouter

from app.api.authentication import login


def getRouter():
    router = APIRouter()
    router.include_router(login.router, tags=["Authentication"])
    return router
