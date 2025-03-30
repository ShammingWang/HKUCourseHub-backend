#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Any, List, Optional

from pydantic import ConfigDict, EmailStr, Field, HttpUrl, model_validator
from typing_extensions import Self


from backend.app.main.schema.course_schedule import GetCourseScheduleDetail
from backend.app.main.schema.course_teacher import GetCourseTeacherDetail
from backend.common.enums import StatusType
from backend.common.schema import SchemaBase

class CourseSchemaBase(SchemaBase):
    id: int = Field(None, title='课程ID')
    course_code: Optional[str] = Field(None, title='课程代码', max_length=50)
    course_name: Optional[str] = Field(None, title='课程名称', max_length=100)
    course_description: Optional[str] = Field(None, title='课程描述')
    semester: Optional[str] = Field(None, title='学期', max_length=20)
    created_by: Optional[int] = Field(None, title='创建者')

class GetCourseDetail(CourseSchemaBase):
    # 这个很重要 返回给前端的数据必须是padantic的模型 这里允许从sqlalchemy的模型中直接转换
    model_config = ConfigDict(from_attributes=True)
    pass

class GetCourseDetailWithRelation(GetCourseDetail):
    model_config = ConfigDict(from_attributes=True)
    # creator: Optional['UserSchema'] = None
    course_teachers: Optional[list[GetCourseTeacherDetail]] = None
    course_schedules: Optional[list[GetCourseScheduleDetail]] = None
    # user_courses: Optional[List['UserCourseSchema']] = None
    # favorite_courses: Optional[List['FavoriteCourseSchema']] = None
    # course_forums: Optional[List['CourseForumSchema']] = None
