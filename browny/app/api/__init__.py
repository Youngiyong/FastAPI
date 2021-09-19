from fastapi import APIRouter

from app.api.v1 import users, blogs, posts, qnas, notices

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(blogs.router, prefix="/blogs", tags=["blogs"])
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(qnas.router, prefix="/qnas", tags=["qnas"])
api_router.include_router(notices.router, prefix="/notices", tags=["notices"])