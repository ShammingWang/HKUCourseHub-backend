#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import bcrypt

from sqlalchemy import and_, desc, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import noload, selectinload
from sqlalchemy.sql import Select
from sqlalchemy_crud_plus import CRUDPlus

from backend.app.main.model import User
from backend.app.main.schema.user import RegisterUserParam

from backend.common.security.jwt import get_hash_password
from backend.utils.timezone import timezone

class CRUDUser(CRUDPlus[User]):
    async def get(self, db: AsyncSession, user_id: int) -> User | None:
        """
        获取用户

        :param db:
        :param user_id:
        :return:
        """
        return await self.select_model(db, user_id)

    async def get_by_username(self, db: AsyncSession, username: str) -> User | None:
        """
        通过 username 获取用户

        :param db:
        :param username:
        :return:
        """
        return await self.select_model_by_column(db, username=username)

    async def check_email(self, db: AsyncSession, email: str) -> User | None:
        """
        检查邮箱是否存在

        :param db:
        :param email:
        :return:
        """
        return await self.select_model_by_column(db, email=email)


    async def create(self, db: AsyncSession, obj: RegisterUserParam, *, social: bool = False) -> None:
        """
        创建用户

        :param db:
        :param obj:
        :param social: 社交用户，适配 oauth 2.0
        :return:
        """
        # if not social:
        #     salt = bcrypt.gensalt()
        #     obj.password = get_hash_password(obj.password, salt)
        #     dict_obj = obj.model_dump()
        #     dict_obj.update({'is_staff': True, 'salt': salt})
        # else:
        #     dict_obj = obj.model_dump()
        #     dict_obj.update({'is_staff': True, 'salt': None})
        # new_user = self.model(**dict_obj)
        salt = bcrypt.gensalt()
        # 这里进行hash撒盐加密
        obj.password = get_hash_password(obj.password, salt)
        dict_obj = obj.model_dump()
        dict_obj.update({'salt': salt})
        new_user = self.model(**dict_obj)
        db.add(new_user)


user_dao: CRUDUser = CRUDUser(User)