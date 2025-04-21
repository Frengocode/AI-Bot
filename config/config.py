from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    OPEN_AI_KEY: SecretStr
    BOT_TOKEN: SecretStr
    ASSISTANT_ID: SecretStr

    model_config = SettingsConfigDict(env_file=".env", allow="extra")


settings = Settings()
