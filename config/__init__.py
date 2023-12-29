from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='config/.env', env_file_encoding='utf-8')
    server_host: SecretStr
    server_port: SecretStr
    db_url: SecretStr


config = Settings()
