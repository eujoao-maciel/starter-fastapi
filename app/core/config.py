from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 3000

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
