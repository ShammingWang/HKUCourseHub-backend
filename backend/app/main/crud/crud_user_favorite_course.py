#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import bcrypt

from sqlalchemy import and_, desc, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import noload, selectinload
from sqlalchemy import Select
from sqlalchemy_crud_plus import CRUDPlus


from backend.app.main.model.courses import Course
from backend.app.main.model.favorite_courses import FavoriteCourse


class CRUDUserFavoriteCourse(CRUDPlus[FavoriteCourse]):
    pass
    # async def get_list_by_user_id(self, db: AsyncSession, user_id: int) -> list[UserCourse] | None:
    #     """
    #     获取课程

    #     :param db:
    #     :param course_id:
    #     :return:
    #     """
    #     return await self.select_models(db, user_id=user_id)

user_favorite_course_dao: CRUDUserFavoriteCourse = CRUDUserFavoriteCourse(FavoriteCourse)
