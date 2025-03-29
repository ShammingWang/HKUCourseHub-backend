#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

from fastapi import Request
from sqlalchemy import Select


from backend.app.main.schema.user import GetUserInfoDetail, RegisterUserParam
from backend.app.main.crud.crud_user import user_dao

from backend.common.exception import errors
from backend.common.security.jwt import get_hash_password, get_token, jwt_decode, password_verify, superuser_verify
from backend.core.conf import settings
from backend.database.db import async_db_session
from backend.database.redis import redis_client


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

user_service: UserService = UserService()