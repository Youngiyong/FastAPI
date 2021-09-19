from typing import Optional

from pydantic import BaseModel


class BlogBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    price: Optional[float]


class BlogCreate(BlogBase):
    name: str
    price: float


class BlogUpdate(BlogBase):
    id: int
    pass


class BlogResponse(BlogBase):
    class Config:
        orm_mode = True
