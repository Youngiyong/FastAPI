from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserId(BaseModel):
    id: str


class UserBase(BaseModel):
    email: str
    hashed_password: str


class UserCreate(UserBase):
    email: str
    hashed_password: str


class UserUpdate(BaseModel):
    email: str
    password: str
    is_active: bool


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True