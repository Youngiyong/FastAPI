
from typing import Optional

from pydantic import BaseModel


class PostBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    price: Optional[float]


class PostCreate(PostBase):
    name: str
    price: float


class PostUpdate(PostBase):
    id: int
    pass


class PostResponse(PostBase):
    class Config:
        orm_mode = True
