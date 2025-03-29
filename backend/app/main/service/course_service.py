#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import Select

from backend.app.main.crud.crud_course import course_dao
from backend.app.main.crud.crud_user_course import user_course_dao

from backend.app.main.schema.course import GetCourseDetailWithRelation
from backend.common.exception.errors import NotFoundError
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
                raise NotFoundError
            await db.refresh(course, ['course_schedules'])
            await db.refresh(course, ['course_teachers'])
            return GetCourseDetailWithRelation.model_validate(course)
        
course_service: CourseService = CourseService()
