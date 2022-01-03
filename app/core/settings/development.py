import logging

from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True
    title: str = "EAR-API backend (develpment mode)"
    logging_level: int = logging.DEBUG

    class Config:
        env_file = ".env"
