#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_crud_plus import CRUDPlus

from backend.app.main.model.course_schedules import CourseSchedule
from backend.app.main.schema.course_schedule import CreateCourseSchedule


class CRUDCourseSchedule(CRUDPlus[CourseSchedule]):
    async def get(self, db: AsyncSession, course_schedule_id: int) -> CourseSchedule | None:
        """
        获取课程安排记录
        """
        return await self.select_model(db, course_schedule_id)

    async def add_course_schedule(self, db: AsyncSession, obj: CreateCourseSchedule) -> CourseSchedule | None:
        obj_dump = obj.model_dump()
        course_schedule = self.model(**obj_dump)
        db.add(course_schedule)
        # await db.flush()  # 如果你需要获取新插入记录的 ID，可以取消注释
        # return course_schedule


course_schedule_dao: CRUDCourseSchedule = CRUDCourseSchedule(CourseSchedule)
