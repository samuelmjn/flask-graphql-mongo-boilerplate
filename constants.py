import os
from dotenv import load_dotenv

load_dotenv()

CONFIGS = {
    "PORT": os.environ.get("PORT", 9000),
    "HTTP_STATUS": {
        "404_NOT_FOUND": 404,
    },
    "MONGO_URL": os.environ.get("MONGO_URL"),
    "MONGO_DB": os.getenv("MONGO_DB"),
    # make sure to change the web
    # token secret key from "secret" to something else
    "WEB_TOKEN_SECRET_KEY": os.getenv("WEB_TOKEN_SECRET_KEY"),
    # WEB_TOKEN_ACCESS_TOKEN_EXPIRES is meant to be in seconds
    "WEB_TOKEN_ACCESS_TOKEN_EXPIRES": os.getenv(
        "WEB_TOKEN_ACCESS_TOKEN_EXPIRES")
}
