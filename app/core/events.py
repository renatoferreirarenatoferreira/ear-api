from typing import Callable

from loguru import logger
from fastapi import FastAPI

from app.core.settings.app import AppSettings
from app.core.db.sqlite import SQLite


def create_start_app_handler(
    app: FastAPI,
    settings: AppSettings,
) -> Callable:
    async def start_app() -> None:
        logger.info(settings.title + " is starting up!")
        await SQLite.Connect(app, settings)

    return start_app


def create_stop_app_handler(
    app: FastAPI,
    settings: AppSettings,
) -> Callable:
    async def stop_app() -> None:
        logger.info("Shutting down...")
        await SQLite.Close(app, settings)

    return stop_app
