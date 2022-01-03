import logging

from pydantic import SecretStr

from app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    debug: bool = True
    title: str = "EAR-API backend (test mode)"
    secret_key: SecretStr = SecretStr("test_secret")
    logging_level: int = logging.DEBUG
