import jwt
import bcrypt
from datetime import datetime, timedelta
from constants import CONFIGS
from typing import Dict

WEB_TOKEN_SECRET_KEY = CONFIGS.get("WEB_TOKEN_SECRET_KEY")


def encode_token(profile: Dict[str, str]) -> str:
    return jwt.encode({
        "username": profile["username"],
        "exp": datetime.utcnow() + timedelta(hours=1)},
        WEB_TOKEN_SECRET_KEY,
        algorithm="HS256").decode("utf-8")


def decode_token(token):
    try:
        return jwt.decode(token, WEB_TOKEN_SECRET_KEY, algorithm="HS256")
    except Exception as exception:
        print(exception)
        return {}


def encrypt_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf8"),
                         bcrypt.gensalt()).decode("utf8")


def decrypt_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode("utf8"),
                          hashed_password.encode("utf8"))
