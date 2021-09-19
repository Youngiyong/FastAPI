
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func, Text
from sqlalchemy.orm import relationship

from app.database.base_class import Base


class Members(Base):
    # __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50), nullable=False)
    email = Column(String(length=50), nullable=False)
    sex = Column(String(length=1), nullable=True)
    password = Column(String(length=100), nullable=True)
    phone = Column(String(length=100), nullable=False)
    profile = Column(Text, nullable=True)
    profile_image = Column(String(length=255), nullable=True)
    grade = Column(String(length=10), nullable=True, default="user")
    join_type = Column(String(length=30), nullable=True)
    join_token = Column(String(length=255), nullable=True)
    pw_chage_date = Column(DateTime, nullable=True, default=func.utc_timestamp())
    created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    # blogs = relationship("Blogs", back_populates="member")


class MemberFollows(Base):
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey("members.id"))
    follow_id = Column(Integer, ForeignKey("members.id"))
    memo = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())