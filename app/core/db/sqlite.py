from fastapi import FastAPI
from loguru import logger

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.settings.app import AppSettings


class SQLite():

    async def Connect(app: FastAPI, settings: AppSettings) -> None:
        logger.info("Opening database file {0}", repr(settings.sqlite_file))

        # https://towardsdatascience.com/build-an-async-python-service-with-fastapi-sqlalchemy-196d8792fa08
        # engine = create_async_engine("sqlite+aiosqlite:///"+settings.sqlite_file, future=True, echo=True)
        # async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
        # Base = declarative_base()

    async def Close(app: FastAPI, settings: AppSettings) -> None:
        logger.info("Closing database file {0}", repr(settings.sqlite_file))
