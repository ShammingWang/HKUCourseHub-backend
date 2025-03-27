#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import Select

from backend.app.main.crud.crud_course import course_dao

class CourseService:

    @staticmethod
    async def get_select(*, course_code: str, course_name: str, semester: str) -> Select:
        return await course_dao.get_list(course_code=course_code, course_name=course_name, semester=semester)
    
course_service: CourseService = CourseService()
