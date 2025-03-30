#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Any

from pydantic import ConfigDict, EmailStr, Field, HttpUrl, field_validator, model_validator
from typing_extensions import Self


from backend.app.main.schema.course import GetCourseDetail
from backend.common.enums import StatusType
from backend.common.schema import CustomPhoneNumber, SchemaBase


class AuthSchemaBase(SchemaBase):
    username: str
    password: str | None

    @field_validator("username", mode="before")
    @classmethod
    def strip_username(cls, v: str) -> str:
        return v.strip()

    @field_validator("password", mode="before")
    @classmethod
    def strip_password(cls, v: str | None) -> str | None:
        return v.strip() if isinstance(v, str) else v

class AuthSchemaParam(AuthSchemaBase):  # the same as AuthSchemaBase
    pass


class AuthLoginParam(AuthSchemaParam):  # the same as AuthSchemaParam
    pass


class RegisterUserParam(AuthSchemaBase):
    email: EmailStr = Field(examples=['user@example.com'])


class UserInfoSchemaBase(SchemaBase):
    id: int
    username: str
    email: EmailStr | None = None

    @field_validator("username", mode="before")
    @classmethod
    def strip_username(cls, v: str) -> str:
        return v.strip()

    @field_validator("email", mode="before")
    @classmethod
    def strip_email(cls, v: str | None) -> str | None:
        return v.strip() if isinstance(v, str) else v

class GetUserInfoDetail(UserInfoSchemaBase):
    # 这个很重要 返回给前端的数据必须是padantic的模型 这里允许从sqlalchemy的模型中直接转换
    model_config = ConfigDict(from_attributes=True)

class GetUserInfoDetailWithRelation(UserInfoSchemaBase):
    model_config = ConfigDict(from_attributes=True)
    # courses: list[GetCourseDetail]
