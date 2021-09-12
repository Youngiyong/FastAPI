from sqlalchemy.orm import Session
import models, schemas
import database


def create_user(db: Session, request: schemas.UserCreate):
    fake_hashed_password = request.hashed_password + "notreallyhashed"
    db_user = models.User(email=request.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


def update_user(db: Session, user_id: int, request: schemas.UserUpdate):
    print(user_id)
    print(request)
    user = db.query(models.User).filter_by(id=user_id).first()
    print(user)
    if user:
        user.email = request.email
        user.hashed_password = request.password
        db.add(user)
        db.commit()


def delete_user(db: Session, id: int):
    user = db.query(models.User).filter_by(id=id).first()

    if user:
        user.is_active = False
        db.add(user)
        db.commit()

    return user


def find_user_by_email(db: Session, email: str):
    user = db.query(models.User).filter_by(email=email).first()
    return user


def find_user_by_id(db: Session, id: str):
    user = db.query(models.User).filter_by(id=id).first()
    res = {"id": user.id, "hashed_password": user.hashed_password, "email": user.email, "is_active": user.is_active }
    return res


def find_all_user(db: Session):
    users = db.query(models.User).all()

    return users
