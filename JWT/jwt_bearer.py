from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from log.log_helper import logger
from .jwt_handler import decodeJWT

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True) :
        """
        The __init__ function is called when the class is instantiated.
        It allows the class to initialize its attributes.
        
        
        :param self: Represent the instance of the class
        :param auto_error: bool: Determine whether to raise an exception or not
        :return: A new instance of the jwtbearer class
        """
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) :
        """
        The __call__ function is the function that will be called when a user
        attempts to access an endpoint. It takes in a request object and returns
        either credentials or raises an exception.
        
        :param self: Access the class attributes
        :param request: Request: Get the authorization header from the request
        :return: The credentials
        """
        credentials = await super(JWTBearer, self).__call__(request)
        if not credentials:
            logger.error('Invalid authorization code.')
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
        if credentials.scheme.lower() != "bearer":
            logger.error('Invalid authentication')
            raise HTTPException(status_code=403, detail="Invalid authentication.")
        if not self.verify_jwt(credentials.credentials):
            logger.error('Invalid token or expired token.')
            raise HTTPException(status_code=403, detail="Invalid token or expired token.")
        logger.info('JWT authenticated.')
        return credentials.credentials


    def verify_jwt(self, jwtoken: str) :#-> bool:
        """
        The verify_jwt function takes a JWT token as an argument and returns True if the token is valid, False otherwise.
        
        
        :param self: Represent the instance of a class
        :param jwtoken: str: Pass in the jwtoken to be decoded
        :return: A boolean value, true or false
        """
        try:
            decodeJWT(jwtoken)
            return True
        except:
            return False