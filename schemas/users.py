from datetime import date
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr
from enum import Enum


class UserBase(BaseModel):
    id          : Optional[str] = None
    username    : Optional[str] = None
    password    : Optional[str] = None
    email       : Optional[str] = None
    first_name  : Optional[str] = None
    last_name   : Optional[str] = None
    gender      : Optional[str] = None
    create_at   : Optional[str] = None
    status      : Optional[str] = None


class UserShow(BaseModel):
    username    :str
    first_name  :str
    last_name   :str
    gender      :str
    status      :str
    
    class Config():
        orm_mode = True


class UserCreate(BaseModel):
    username    :str      = Field(..., example = "Doston")
    password    :str      = Field(..., example = "123")
    email       :EmailStr = Field(..., example = "example@gmail.com")
    first_name  :str      = Field(..., example = "Doston")
    last_name   :str      = Field(..., example = "Imomaliyev")
    gender      :str      = Field(..., example = "M")
    
    class Config():
        orm_mode = True


class UserUpdate(BaseModel):
    email       :EmailStr = Field(..., example = "example@gmail.com")
    first_name  :str      = Field(..., example = "Doston")
    last_name   :str      = Field(..., example = "Imomaliyev")
    gender      :str      = Field(..., example = "M")
    status      :str      = Field(..., example = "1")
    
    class Config():
        orm_mode = True
    
    
class UserDelete(BaseModel):
    id          : str = Field(..., example = "Enter your id")
    
    class Config():
        orm_mode = True