from pydantic import BaseSettings, SecretStr
from enum import Enum


class ModeEnum(str, Enum):
    DEVELOPMENT = "dev"
    PRODUCTION = "prod"


class LoggingRenderer(str, Enum):
    JSON = "json"
    CONSOLE = "console"


class LoggingSettings(BaseSettings):
    level: str = "INFO"
    format: str = "%Y-%m-%d %H:%M:%S"
    is_utc: bool = False
    renderer: LoggingRenderer = LoggingRenderer.JSON
    log_unhandled: bool = False

    # Вложенный класс с дополнительными указаниями для настроек
    class Config:
        # Имя файла, откуда будут прочитаны данные
        env_file = '.venv/.env'
        env_file_encoding = 'utf-8'
        env_prefix = "LOGGING_"


class BotSettings(BaseSettings):
    bot_token: SecretStr

    # main_chat_id: int

    class Config:
        env_file = '.venv/.env'
        env_file_encoding = 'utf-8'


bot_config = BotSettings()
log_config = LoggingSettings()
