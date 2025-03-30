#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import Select

from backend.app.main.crud.crud_course import course_dao
from backend.app.main.crud.crud_user_course import user_course_dao

from backend.app.main.schema.course import GetCourseDetailWithRelation
from backend.app.main.schema.course_schedule import CreateCourseSchedule, UpdateCourseSchedule
from backend.app.main.schema.course_teacher import CreateCourseTeacher, UpdateCourseTeacher
from backend.app.main.crud.curd_course_teacher import course_teacher_dao
from backend.app.main.crud.crud_course_schedule import course_schedule_dao

from backend.common.exception import errors
from backend.database.db import async_db_session


class CourseService:

    @staticmethod
    async def get_select(*, course_code: str, course_name: str, semester: str) -> Select:
        return await course_dao.get_list(course_code=course_code, course_name=course_name, semester=semester)
    
    @staticmethod
    async def get_current_user_courses(*, user_id: int) -> list[GetCourseDetailWithRelation]:
        async with async_db_session.begin() as db:
            user_course_list = await user_course_dao.get_list_by_user_id(db, user_id=user_id)
            # course_list = []
            # for user_course in user_course_list:
            #     await db.refresh(user_course, ['course'])
            #     await db.refresh(user_course.course, ['course_schedules'])
            #     course_list.append(GetCourseDetailWithRelation.model_validate(user_course.course))
            # 这里可以使用上面的代码来获取课程列表
            # course_id_list = [user_course.course_id for user_course in user_course_list]
            # course_list = []
            # for course_id in course_id_list:
            #     course = await course_dao.get(db, course_id)
            #     if course is not None:
            #         await db.refresh(course, ['course_schedules'])
            #         await db.refresh(course, ['course_teachers'])
            #         course_list.append(GetCourseDetailWithRelation.model_validate(course))
            # return course_list
            # 也可以使用下面的代码来获取课程列表
            return [await CourseService.get_course_with_relation_by_id(course_id=user_course.course_id) 
                    for user_course in user_course_list]

    @staticmethod
    async def get_course_with_relation_by_id(*, course_id: int) -> GetCourseDetailWithRelation:
        async with async_db_session.begin() as db:
            course = await course_dao.get(db, course_id)
            if course is None:
                raise errors.NotFoundError(msg='id为{}的课程不存在'.format(course_id))
            await db.refresh(course, ['course_schedules'])
            await db.refresh(course, ['course_teachers'])
            return GetCourseDetailWithRelation.model_validate(course)
    
    @staticmethod
    async def add_course_teacher(*, obj: CreateCourseTeacher) -> None:
        async with async_db_session.begin() as db:
            # 先判断课程是否存在
            course = await course_dao.get(db, obj.course_id)
            if course is None:
                raise errors.NotFoundError(msg='id为{}的课程不存在'.format(obj.course_id))
            await course_teacher_dao.add_course_teacher(db, obj)

    @staticmethod
    async def update_course_teacher(*, obj: UpdateCourseTeacher) -> None:
        async with async_db_session.begin() as db:
            # 先判断课程教师关系是否存在
            course_teacher = await course_teacher_dao.get(db, obj.id)
            if course_teacher is None:
                raise errors.NotFoundError(msg='id为{}的课程教师关系不存在'.format(obj.id))
            
            # # 检查课程是否存在
            # course = await course_dao.get(db, obj.course_id)
            # if course is None:
            #     raise errors.NotFoundError(msg='id为{}的课程不存在'.format(obj.course_id))

            # 调用 DAO 的 update_model 方法（按主键更新）
            await course_teacher_dao.update_model(
                session=db,
                pk=obj.id,
                obj=obj
            )

    @staticmethod
    async def add_course_schedule(*, obj: CreateCourseSchedule) -> None:
        async with async_db_session.begin() as db:
            # 先判断课程是否存在
            course = await course_dao.get(db, obj.course_id)
            if course is None:
                raise errors.NotFoundError(msg='id为{}的课程不存在'.format(obj.course_id))
            await course_schedule_dao.add_course_schedule(db, obj)

    @staticmethod
    async def update_course_schedule(*, obj: UpdateCourseSchedule) -> None:
        async with async_db_session.begin() as db:
            # 先判断课程安排是否存在
            course_schedule = await course_schedule_dao.get(db, obj.id)
            if course_schedule is None:
                raise errors.NotFoundError(msg='id为{}的课程安排不存在'.format(obj.id))
            
            # # 检查课程是否存在（如有需要可取消注释）
            # course = await course_dao.get(db, obj.course_id)
            # if course is None:
            #     raise errors.NotFoundError(msg='id为{}的课程不存在'.format(obj.course_id))

            # 调用 DAO 的 update_model 方法（按主键更新）
            await course_schedule_dao.update_model(
                session=db,
                pk=obj.id,
                obj=obj
            )


course_service: CourseService = CourseService()
