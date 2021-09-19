from typing import Optional

from pydantic import BaseModel


class MemberBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    price: Optional[float]


class MemberCreate(MemberBase):
    name: str
    price: float


class MemberUpdate(MemberBase):
    id: int
    pass


class MemberResponse(MemberBase):
    class Config:
        orm_mode = True
