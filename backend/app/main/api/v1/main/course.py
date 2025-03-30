from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response, Path
# from sqlalchemy.orm import Session
from backend.app.main.model.courses import Course
from backend.app.main.schema.course import GetCourseDetail, GetCourseDetailWithRelation
from backend.app.main.schema.course_schedule import CreateCourseSchedule, UpdateCourseSchedule
from backend.app.main.schema.course_teacher import CreateCourseTeacher, UpdateCourseTeacher
from backend.app.main.service.course_service import course_service
from backend.common.exception import errors
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



@router.get(
    "/courses/me",
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

@router.get(
    "/course/{course_id}",
    summary="获取课程详细信息",
    description="根据课程ID获取课程详细信息",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def get_course_with_relation(
    course_id: Annotated[int, Path(..., title="课程ID", description="课程的唯一标识符")]
) -> ResponseSchemaModel[GetCourseDetailWithRelation]:
    """
    根据课程ID获取课程详细信息

    :param db: 数据库会话
    :param course_id: 课程ID
    :return: 课程详细信息
    """
    course = await course_service.get_course_with_relation_by_id(course_id=course_id)
    if not course:
        raise errors.NotFoundError(msg="id为{}的课程不存在".format(course_id))
    return response_base.success(data=course)

@router.post(
    "/course/teacher",
    summary="添加课程教师",
    description="添加课程教师接口",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def add_course_teacher(
    obj: CreateCourseTeacher,
) -> ResponseSchemaModel[None]:
    """
    添加课程教师
    :param course_id: 课程ID
    :param teacher_id: 教师ID
    :return: None
    """
    await course_service.add_course_teacher(obj=obj)
    return response_base.success()


@router.put(
    "/course/teacher",
    summary="修改课程教师",
    description="修改课程教师接口",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def update_course_teacher(
    obj: UpdateCourseTeacher,
) -> ResponseSchemaModel[None]:
    """
    修改课程教师
    :param id: 课程教师关系ID
    :param course_id: 课程ID
    :param teacher_id: 教师ID
    :return: None
    """
    await course_service.update_course_teacher(obj=obj)
    return response_base.success()

@router.delete(
    "/course/teacher",
    summary="删除课程教师",
    description="删除课程教师接口",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def delete_course_teacher(
    id: int,
) -> ResponseSchemaModel[None]:
    """
    删除课程教师
    :param id: 课程教师关系ID
    :return: None
    """
    await course_service.delete_course_teacher(id=id)
    return response_base.success()



@router.post(
    "/course/schedule",
    summary="添加课程安排",
    description="添加课程安排接口",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def add_course_schedule(
    obj: CreateCourseSchedule,
) -> ResponseSchemaModel[None]:
    """
    添加课程安排
    :param course_id: 课程ID
    :param schedule_time: 安排时间
    :param location: 上课地点
    :return: None
    """
    await course_service.add_course_schedule(obj=obj)
    return response_base.success()


@router.put(
    "/course/schedule",
    summary="修改课程安排",
    description="修改课程安排接口",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def update_course_schedule(
    obj: UpdateCourseSchedule,
) -> ResponseSchemaModel[None]:
    """
    修改课程安排
    :param id: 安排ID
    :param schedule_date: 上课日期
    :param day_of_week: 星期几
    :param start_time: 开始时间
    :param end_time: 结束时间
    :param location: 上课地点
    :return: None
    """
    await course_service.update_course_schedule(obj=obj)
    return response_base.success()

@router.delete(
    "/course/schedule",
    summary="删除课程安排",
    description="删除课程安排接口",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def delete_course_schedule(
    id: int,
) -> ResponseSchemaModel[None]:
    """
    删除课程安排
    :param id: 课程安排ID
    :return: None
    """
    await course_service.delete_course_schedule(id=id)
    return response_base.success()


