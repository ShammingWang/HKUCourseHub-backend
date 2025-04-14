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

@router.get(
    "/user/courses",
    summary="获取当前用户课程列表",
    description="根据当前用户获取课程列表",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def get_courses_by_current_user(
    request: Request,
    response: Response,
) -> ResponseSchemaModel[list[GetCourseDetailWithRelation]]:
    user_id = request.user.id  # 由jwt认证提供的用户ID
    courses = await course_service.get_current_user_courses(user_id=user_id)
    return response_base.success(data=courses)


@router.post(
    "/user/course/{course_id}",
    summary="用户请求选课",
    description="用户请求选课接口“",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def add_user_course(
    request: Request,
    course_id: int = Path(..., title="课程ID", description="用户想要选课的课程ID"),
) -> ResponseSchemaModel[None]:
    user_id = request.user.id
    await user_service.add_user_course(user_id=user_id, course_id=course_id)
    return response_base.success(data=None)

@router.delete(
    "/user/course/{course_id}",
    summary="用户请求删除选课",
    description="用户请求删除选课接口“",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def delete_user_course(
    request: Request,
    course_id: int = Path(..., title="课程ID", description="课程ID"),
) -> ResponseSchemaModel[None]:
    user_id = request.user.id
    await user_service.delete_user_course_by_course_id(user_id=user_id, course_id=course_id)
    return response_base.success(data=None)



@router.get(
    "/user/favorite",
    summary="获取当前用户收藏的课程列表",
    description="获取当前用户收藏的课程列表",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def get_favorite_courses_by_current_user(
    request: Request,
    response: Response,
) -> ResponseSchemaModel[list[GetCourseDetailWithRelation]]:
    user_id = request.user.id  # 由jwt认证提供的用户ID
    courses = await course_service.get_current_user_favorite_courses(user_id=user_id)
    return response_base.success(data=courses)

@router.post(
    "/user/favorite/{course_id}",
    summary="添加当前用户收藏的课程",
    description="添加当前用户收藏的课程",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def add_favorite_courses_by_current_user(
    request: Request,
    course_id: int = Path(..., title="课程ID", description="用户想收藏的课程ID"),
) -> ResponseSchemaModel[None]:
    user_id = request.user.id  # 由jwt认证提供的用户ID
    await course_service.add_user_favorite_course(user_id=user_id, course_id=course_id)
    return response_base.success(data=None)

@router.delete(
    "/user/favorite/{course_id}",
    summary="删除当前用户收藏的课程",
    description="删除当前用户收藏的课程",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def delete_favorite_courses_by_current_user(
    request: Request,
    course_id: int = Path(..., title="课程ID", description="用户想收藏的课程ID"),
) -> ResponseSchemaModel[None]:
    user_id = request.user.id
    # 由jwt认证提供的用户ID
    await course_service.delete_user_favorite_course(user_id=user_id, course_id=course_id)
    return response_base.success(data=None)

