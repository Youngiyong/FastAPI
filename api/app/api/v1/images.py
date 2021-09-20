from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status, File, Form, UploadFile
from sqlalchemy.orm import Session
from app import schemas
from app.common.helper import make_image_file_path, s3_upload
router = APIRouter()


@router.post("")
async def upload_images(file: UploadFile = File(...), upload_path: str = Form(...)):
    """
    upload_s3_images
    """

    # max_size = 5 * 1024000 * 104
    image_path = make_image_file_path(upload_path, file)

    upload = s3_upload(file, image_path.get("full_path"))
    print(upload)
    if not upload:
        raise HTTPException(status_code=400, detail="bad request error")

    return image_path
