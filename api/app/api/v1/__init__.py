from fastapi import APIRouter

from app.api.v1 import users, blogs, post, qnas, notices, auth, images

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(images.router, prefix="/images", tags=["images"])
api_router.include_router(blogs.router, prefix="/blogs", tags=["blogs"])
api_router.include_router(post.router, prefix="/posts", tags=["posts"])
api_router.include_router(qnas.router, prefix="/qnas", tags=["qnas"])
api_router.include_router(notices.router, prefix="/notices", tags=["notices"])
