from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response
# from sqlalchemy.orm import Session
from backend.app.main.model.courses import Course
from backend.app.main.schema.course import GetCourseDetail
from backend.app.main.service.course_service import course_service
from backend.common.pagination import DependsPagination, PageData, paging_data
from backend.common.response.response_schema import ResponseModel, ResponseSchemaModel, response_base
from backend.common.security.jwt import DependsJwtAuth
from backend.database.db import CurrentSession
from sqlalchemy.orm import selectinload

router = APIRouter()

@router.get(
    "/courses",
    summary="获取课程列表",
    description="获取课程列表接口",
    dependencies=[
        DependsJwtAuth, # 需要jwt认证
        DependsPagination, # 需要分页
    ]  
)
async def get_courses(
    db: CurrentSession,  # 依赖注入当前数据库会话
    course_code: Annotated[str | None, Query()] = None,
    course_name: Annotated[str | None, Query()] = None,
    semester: Annotated[str | None, Query()] = None,
) -> ResponseSchemaModel[PageData[GetCourseDetail]]:
    course_select = await course_service.get_select(course_code=course_code, course_name=course_name, semester=semester)
    page_data = await paging_data(db, course_select, schema_model=GetCourseDetail)
    return response_base.success(data=page_data)

