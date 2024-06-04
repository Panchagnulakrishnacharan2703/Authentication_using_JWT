import time
import jwt
from decouple import config

JWT_secret = "dcc152f43c9cf01acec4"
JWT_algorithm = "HS256"

def signJWT(USERID: str) -> str:
    """
    The signJWT function takes a USERID as an argument and returns a JWT token.
    The payload of the JWT contains the USERID and an expiry time, which is set to 10 minutes from when it was created.
    
    :param USERID: str: Specify the user id that will be used to generate a jwt
    :return: A jwt token
    """
    payload = {
        "USERID": USERID,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_secret, algorithm=JWT_algorithm)
    return token


def decodeJWT(token: str) -> dict:
    """
    The decodeJWT function takes a JWT token as an argument and returns the decoded payload.
    If the token is invalid, it will return an empty dictionary.
    
    :param token: str: Pass in the token to be decoded
    :return: A dictionary with the following keys:
    """
    try:
        decode_token = jwt.decode(token, JWT_secret, algorithm=JWT_algorithm)
        return decode_token
    except:
        return { }