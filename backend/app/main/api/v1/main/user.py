from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response, Path
# from sqlalchemy.orm import Session
from backend.app.main.model.courses import Course
from backend.app.main.schema.course import GetCourseDetail, GetCourseDetailWithRelation
from backend.app.main.schema.user import GetUserInfoDetail
from backend.app.main.service.user_service import user_service
from backend.app.main.service.course_service import course_service
from backend.common.exception.errors import NotFoundError
from backend.common.pagination import DependsPagination, PageData, paging_data
from backend.common.response.response_schema import ResponseModel, ResponseSchemaModel, response_base
from backend.common.security.jwt import DependsJwtAuth
from backend.database.db import CurrentSession
from sqlalchemy.orm import selectinload


router = APIRouter()

@router.get(
    "/user/me",
    summary="获取当前用户信息",
    description="获取当前用户信息接口",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def get_current_user(
    request: Request,
    response: Response,
) -> ResponseSchemaModel[GetUserInfoDetail]:
    user_id = request.user.id
    user = await user_service.get_user_by_id(id=user_id)
    return response_base.success(data=user)
