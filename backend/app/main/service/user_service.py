#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

from fastapi import Request
from sqlalchemy import Select


from backend.app.main.schema.user import GetUserInfoDetail, RegisterUserParam
from backend.app.main.crud.crud_user import user_dao
from backend.app.main.crud.crud_user_course import user_course_dao
from backend.app.main.crud.crud_course import course_dao


from backend.app.main.schema.user_course import CreateUserCourse
from backend.common.exception import errors
from backend.database.db import async_db_session


class UserService:
    @staticmethod
    async def register(*, obj: RegisterUserParam) -> None:
        async with async_db_session.begin() as db:
            if not obj.password:
                raise errors.ForbiddenError(msg='密码为空')
            username = await user_dao.get_by_username(db, obj.username)
            if username:
                raise errors.ForbiddenError(msg='用户已注册')
            # obj.nickname = obj.nickname if obj.nickname else f'#{random.randrange(10000, 88888)}'
            # nickname = await user_dao.get_by_nickname(db, obj.nickname)
            # if nickname:
            #     raise errors.ForbiddenError(msg='昵称已注册')
            email = await user_dao.check_email(db, obj.email)
            if email:
                raise errors.ForbiddenError(msg='邮箱已注册')
            await user_dao.create(db, obj)
    @staticmethod
    async def get_user_by_id(*, id: int) -> GetUserInfoDetail:
        async with async_db_session.begin() as db:
            user = await user_dao.get(db, id)
            if not user:
                raise errors.NotFoundError(msg='id为{}的用户不存在'.format(id))
            return GetUserInfoDetail.model_validate(user)

    @staticmethod
    async def add_user_course(user_id: int, course_id: int) -> None:
        async with async_db_session.begin() as db:
            # 检查课程是否存在
            course = await course_dao.select_model(db, course_id)
            if not course:
                raise errors.NotFoundError(msg='id为{}的课程不存在'.format(course_id))
            user_course = await user_course_dao.select_model_by_column(
                session=db,
                user_id=user_id,
                course_id=course_id
            )
            if user_course:
                raise errors.ForbiddenError(msg='用户已选这门课')
            
            await user_course_dao.create_model(
                session=db,
                obj=CreateUserCourse(
                    user_id=user_id,
                    course_id=course_id
                )
            )

    @staticmethod
    async def delete_user_course_by_course_id(user_id: int, course_id: int) -> None:
        async with async_db_session.begin() as db:
            # 检查课程是否存在
            course = await course_dao.select_model(db, course_id)
            if not course:
                raise errors.NotFoundError(msg='id为{}的课程不存在'.format(course_id))

            # 查找用户选课记录
            user_course = await user_course_dao.select_model_by_column(
                session=db,
                user_id=user_id,
                course_id=course_id
            )
            if not user_course:
                raise errors.NotFoundError(msg='用户未选这门课')

            # 删除用户选课记录
            await user_course_dao.delete_model(
                session=db,
                pk=user_course.id
            )


user_service: UserService = UserService()