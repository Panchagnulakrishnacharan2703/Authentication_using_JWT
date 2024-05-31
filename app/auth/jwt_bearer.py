from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer

from .jwt_handler import decodeJWT

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials = await super(JWTBearer, self).__call__(request)
        if not credentials:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
        if credentials.scheme.lower() != "bearer":
            raise HTTPException(status_code=403, detail="Invalid authentication.")
        if not self.verify_jwt(credentials.credentials):
            raise HTTPException(status_code=403, detail="Invalid token or expired token.")
        return credentials.credentials

    def verify_jwt(self, jwtoken: str) -> bool:
        try:
            decodeJWT(jwtoken)
            return True
        except:
            return False