
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session, sessionmaker

import sqlalchemy.orm.session

import models
import database
import schemas
import crud
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users")
def create_user(request: schemas.UserBase, db: Session = Depends(get_db)):
    user = crud.find_user_by_email(db, email=request.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already exist")

    return crud.create_user(db=db, request=request)


@app.get("/users/{user_id}", response_model=schemas.UserBase)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.find_user_by_id(db, id=user_id)

    if user is None:
        raise HTTPException(status_code=400, detail="Id is not exist")

    return user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):

    user = crud.delete_user(db, id=user_id)

    if user is None:
        raise HTTPException(status_code=400, detail="Id is not exist")

    else:
        return user


@app.put("/users/{user_id}")
def update_user(user_id: int, request: schemas.UserUpdate, db: Session = Depends(get_db)):
    print(request)
    return crud.update_user(db, user_id, request)

