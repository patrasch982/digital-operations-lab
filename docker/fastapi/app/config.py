import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "Digital Operations Lab API")
    APP_VERSION = os.getenv("APP_VERSION", "0.0.0")
    APP_ENV = os.getenv("APP_ENV", "development")
    HOST_NAME = os.getenv("HOST_NAME", "unknown")


settings = Settings()
