from os import environ

from dotenv import load_dotenv

load_dotenv()


class Config:
    CHATBOT_CONFIG = {
        # "access_token": environ.get("CHATBOT_ACCESS_TOKEN"),
        "email": environ.get("CHATBOT_EMAIL"),
        "password": environ.get("CHATBOT_PASSWORD"),
    }
