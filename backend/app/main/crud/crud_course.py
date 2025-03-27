#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import bcrypt

from sqlalchemy import and_, desc, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import noload, selectinload
from sqlalchemy import Select
from sqlalchemy_crud_plus import CRUDPlus


from backend.app.main.model.courses import Course
from backend.common.security.jwt import get_hash_password
from backend.utils.timezone import timezone

class CRUDUser(CRUDPlus[Course]):
    async def get(self, db: AsyncSession, course_id: int) -> Course | None:
        """
        获取课程

        :param db:
        :param course_id:
        :return:
        """
        return await self.select_model(db, course_id)
    
    async def get_list(self, course_code: str | None = None, 
                       course_name: str | None = None, 
                       semester: str | None = None) -> Select:
        """
        获取课程列表"
        """
        filters = {}
        if course_code is not None:
            filters.update(course_code__like=f'%{course_code}%')
        if course_name is not None:
            filters.update(course_name__like=f'%{course_name}%')
        if semester is not None:
            filters.update(semester=semester)
        return await self.select_order('course_code', 'asc', **filters)
    
course_dao: CRUDUser = CRUDUser(Course)
