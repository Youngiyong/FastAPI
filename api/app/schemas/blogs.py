from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BlogBase(BaseModel):
    id: Optional[int]
    member_id: Optional[int]
    name: Optional[str]
    blog_url: Optional[str]
    blog_icon: Optional[str]
    blog_favicon: Optional[str]
    created_at: Optional[datetime]


class BlogCreate(BaseModel):
    member_id: Optional[int]
    name: Optional[str]
    blog_url: Optional[str]
    blog_icon: Optional[str]
    blog_favicon: Optional[str]


class BlogUpdate(BaseModel):
    name: Optional[str]
    blog_url: Optional[str]
    blog_icon: Optional[str]
    blog_favicon: Optional[str]


class BlogResponse(BlogBase):
    class Config:
        orm_mode = True
