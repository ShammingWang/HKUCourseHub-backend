from backend.app.main.api.v1.main.course import router as course_router
from backend.app.main.api.v1.main.user import router as user_router
from backend.app.main.api.v1.main.forum import router as forum_router
from fastapi import APIRouter

router = APIRouter(prefix='/main')

router.include_router(course_router, tags=["课程类API"])
router.include_router(user_router, tags=["用户类API"])
router.include_router(forum_router, tags=["论坛类API"])
