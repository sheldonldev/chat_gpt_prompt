from os import environ
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Config:
    EMAILE = environ.get("CHATBOT_EMAIL")
    PASSWORD = environ.get("CHATBOT_PASSWORD")
    PROXY = environ.get("PROXY")
    ACCESS_TOKEN_PATH = Path(__file__).parent.joinpath("access_token")
