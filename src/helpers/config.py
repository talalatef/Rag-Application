from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    VERSION_APP: str
    ANYSCALE_API_KEY: str
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFUELT_CHUNK_SIZE:int

    class Config():

        env_file = ".env"

def get_settings():
    return Settings()
