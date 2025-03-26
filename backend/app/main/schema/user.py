#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Any

from pydantic import ConfigDict, EmailStr, Field, HttpUrl, model_validator
from typing_extensions import Self

from backend.app.admin.schema.dept import GetDeptDetail
from backend.app.admin.schema.role import GetRoleWithRelationDetail
from backend.common.enums import StatusType
from backend.common.schema import CustomPhoneNumber, SchemaBase


class AuthSchemaBase(SchemaBase):
    username: str
    password: str | None


class AuthSchemaParam(AuthSchemaBase):  # the same as AuthSchemaBase
    pass


class UserInfoSchemaBase(SchemaBase):
    username: str
    email: EmailStr | None = None

class GetUserInfoWithRelationDetail(UserInfoSchemaBase):
    model_config = ConfigDict(from_attributes=True)
