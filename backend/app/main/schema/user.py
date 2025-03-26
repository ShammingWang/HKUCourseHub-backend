#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Any

from pydantic import ConfigDict, EmailStr, Field, HttpUrl, model_validator
from typing_extensions import Self


from backend.common.enums import StatusType
from backend.common.schema import CustomPhoneNumber, SchemaBase


class AuthSchemaBase(SchemaBase):
    username: str
    password: str | None


class AuthSchemaParam(AuthSchemaBase):  # the same as AuthSchemaBase
    pass


class AuthLoginParam(AuthSchemaParam):  # the same as AuthSchemaParam
    pass


class RegisterUserParam(AuthSchemaBase):
    email: EmailStr = Field(examples=['user@example.com'])


class UserInfoSchemaBase(SchemaBase):
    username: str
    email: EmailStr | None = None

class GetUserInfoDetail(UserInfoSchemaBase):
    # 这个很重要 返回给前端的数据必须是padantic的模型 这里允许从sqlalchemy的模型中直接转换
    model_config = ConfigDict(from_attributes=True)
    id: int

class GetUserInfoWithRelationDetail(UserInfoSchemaBase):
    model_config = ConfigDict(from_attributes=True)
