from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    price: Optional[float]


class UserCreate(UserBase):
    name: str
    price: float


class UserUpdate(UserBase):
    id: int
    pass


class UserResponse(UserBase):
    class Config:
        orm_mode = True
