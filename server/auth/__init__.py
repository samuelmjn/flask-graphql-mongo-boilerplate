import jwt
import bcrypt
from datetime import datetime, timedelta
from constants import CONSTANTS
from typing import Dict

WEB_TOKEN_SECRET_KEY = CONSTANTS.get("WEB_TOKEN_SECRET_KEY")


def encode_token(profile: Dict[str, str]) -> str:
    """
    Encodes profile data into a web token
    :param profile:
    :return:
    """
    return jwt.encode({
        "username": profile["username"],
        "exp": datetime.utcnow() + timedelta(hours=1)},
        WEB_TOKEN_SECRET_KEY,
        algorithm="HS256").decode("utf-8")


def decode_token(token: str) -> Dict[str, str]:
    """
    Decodes a web token and checks
    :param token: the token to decode
    :return:
    """
    try:
        decoded = jwt.decode(token, WEB_TOKEN_SECRET_KEY, algorithm="HS256")
        if (datetime.utcnow() - decoded["exp"]).total_seconds() >= 1:
            raise Exception('Token expired. Please login again.')
        return decoded
    except Exception:
        raise Exception('Failed to decode token')


def encrypt_password(password: str) -> str:
    """
    Encryption on a password
    :param password: the password to encrypt
    :return: the hashed password
    """
    return bcrypt.hashpw(password.encode("utf8"),
                         bcrypt.gensalt()).decode("utf8")


def decrypt_password(password: str, hashed_password: str) -> bool:
    """
    Checks if the entered hashed password matches the hashed password in
    database
    :param password: the inputted password
    :param hashed_password: the password hashed in database
    :return: whether or not their hashes match
    """
    return bcrypt.checkpw(password.encode("utf8"),
                          hashed_password.encode("utf8"))
