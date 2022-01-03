from fastapi import APIRouter, Body

from loguru import logger

from .login_model import UserLogin

router = APIRouter()


@router.post("/login", name="auth:login")
async def login(
    user_login: UserLogin = Body(..., embed=True, alias="user"),
):
    logger.info("Login")
