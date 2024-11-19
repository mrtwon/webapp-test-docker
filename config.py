from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    backend_login: str = Field('backend', alias='backend_login')
    backend_password: str = Field('qwerty', alias='backend_password')

    postgres_login: str = Field('postgres', alias='postgres_password')
    postgres_password: str = Field('qwerty', alias='postgres_password')

    model_config = SettingsConfigDict(env_prefix='', env_file='.env')

    @property
    def DATABASE_URL_BACKEND(self):
        return f'postgresql+asyncpg://{self.backend_login}:{self.backend_password}@192.168.1.18:5432/postgres?async_fallback=True'

    @property
    def DATABASE_URL_POSTGRES(self):
        return f'postgresql+asyncpg://{self.postgres_login}:{self.postgres_password}@192.168.1.18:5432/postgres?async_fallback=True'

settings = Settings()