from typing import Callable

from loguru import logger
from fastapi import FastAPI

from app.core.settings.app import AppSettings


def create_start_app_handler(
    app: FastAPI,
    settings: AppSettings,
) -> Callable:
    async def start_app() -> None:
        logger.info(settings.title + " is starting up!")

    return start_app


def create_stop_app_handler(
    app: FastAPI
) -> Callable:
    async def stop_app() -> None:
        logger.info("Shutting down...")

    return stop_app
