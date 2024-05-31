import time
import jwt
from decouple import config

JWT_secret = config("secret")
JWT_algorithm = config("algorithm")

def signJWT(USERID: str) -> str:
    payload = {
        "USERID": USERID,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_secret, algorithm=JWT_algorithm)
    return token

def decodeJWT(token: str) -> dict:
    try:
        decode_token = jwt.decode(token, JWT_secret, algorithm=JWT_algorithm)
        return decode_token
    except:
        return { }