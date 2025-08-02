from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
from app.utils.logging import logger

# Explicitly load the .env file from the project root
# Adjust the path if necessary; here we assume you're running from the root.
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))


# Define the settings class using Pydantic
class Settings(BaseSettings):
    # --- General environment variables ---
    SECRET_KEY: str
    ALGORITHM: str

    # --- OpenAI-related environment variables ---
    OPENAI_API_KEY: str
    class Config:
        env_file = ".env.development"  # This is relative to the working directory


# Initialize settings
settings = Settings()

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM