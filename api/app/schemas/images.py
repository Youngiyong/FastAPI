from typing import Optional

from pydantic import BaseModel


class ImageCreate(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        schema_extra = [{
            "example": {
                "file": "multipart-form"
            }
        }]


class ImageResponse(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        schema_extra = [{
            "example": {
                "image" : "https://s3.aws.com/members/example.png",
            }
        }]

