from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int = Field(default=None)
    company_name: str = Field(default="")
    company_details: str = Field(default="")

class UserSchema(BaseModel):
    firstname: str = Field(...)
    lastname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)