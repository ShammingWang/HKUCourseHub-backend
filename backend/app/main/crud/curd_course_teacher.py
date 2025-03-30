#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import bcrypt

from sqlalchemy import and_, desc, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import noload, selectinload
from sqlalchemy import Select
from sqlalchemy_crud_plus import CRUDPlus


from backend.app.main.model.course_teachers import CourseTeacher
from backend.app.main.model.courses import Course
from backend.app.main.model.user_courses import UserCourse
from backend.app.main.schema.course_teacher import CreateTeacherCourse
from backend.common.security.jwt import get_hash_password
from backend.utils.timezone import timezone


class CRUDUser(CRUDPlus[CourseTeacher]):
    async def get(self, db: AsyncSession, course_teacher_id: int) -> CourseTeacher | None:
        """
        获取课程教师关系
        """
        return await self.select_model(db, course_teacher_id)
    

    async def add_course_teacher(self, db: AsyncSession, obj: CreateTeacherCourse) -> CourseTeacher | None:
        obj_dump = obj.model_dump()
        course_teacher = self.model(**obj_dump)
        db.add(course_teacher)
        # await db.flush()  # 获取 ID 必须 flush 一下
        # return course_teacher

course_teacher_dao: CRUDUser = CRUDUser(CourseTeacher)
