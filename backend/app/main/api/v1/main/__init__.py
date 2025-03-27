from backend.app.main.api.v1.main.course import router as course_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(course_router, tags=["课程类API"], prefix="/main")

