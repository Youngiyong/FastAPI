from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api.deps import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.BlogResponse])
def get_multi_blogs(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    find all blogs.
    """
    blog = crud.blog.get_multi(db, skip=skip, limit=limit)
    return blog


@router.get("/{id}", response_model=schemas.BlogResponse)
def get_blog(id: int, db: Session = Depends(get_db)) -> Any:
    """
    find blog
    """
    blog = crud.blog.get(db, id=id)

    if not blog:
        raise HTTPException(status_code=404, detail="blog not found")

    return blog


@router.post("", response_model=schemas.BlogResponse)
def create_blog(*, db: Session = Depends(get_db), blog_in: schemas.BlogCreate) -> Any:
    """
    Create new Blog.
    """
    blog = crud.blog.create(db, obj_in=blog_in)
    return blog


@router.put("/{id}", response_model=schemas.BlogResponse)
def update_blog(*, db: Session = Depends(get_db), id: int, blog_in: schemas.BlogUpdate) -> Any:
    """
    Update Blog.
    """
    blog = crud.blog.get(db, id=id)

    if not blog:
        raise HTTPException(status_code=404, detail="blog not found")

    if blog_in is None:
        raise HTTPException(status_code=400, detail="Bad Request Error")

    blog = crud.blog.update(db=db, db_obj=blog, obj_in=blog_in)
    return blog

@router.delete("/{id}")
def delete_blog(*, db: Session = Depends(get_db), id: int) -> Any:
    """
    Delete Blog.
    """
    blog = crud.blog.get(db, id=id)

    if not blog:
        raise HTTPException(status_code=404, detail="blog not found")

    return crud.blog.delete(db=db, db_obj=blog)
