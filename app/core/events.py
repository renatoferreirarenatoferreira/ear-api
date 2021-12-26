from typing import Callable

from loguru import logger

def create_start_app_handler() -> Callable:
    async def start_app() -> None:
        logger.info("Starting up!")

    return start_app


def create_stop_app_handler() -> Callable:
    async def stop_app() -> None:
        logger.info("Shutting down...")

    return stop_app