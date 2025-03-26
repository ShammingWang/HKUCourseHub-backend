#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter, Request, Response, Depends
from starlette.background import BackgroundTasks
from fastapi_limiter.depends import RateLimiter

from backend.app.main.schema.user import AuthSchemaParam
from backend.app.main.schema.user import RegisterUserParam
from backend.app.main.service.user_service import user_service

from backend.common.response.response_schema import ResponseSchemaModel, response_base

router = APIRouter()


@router.post(
    '/register',
    summary='用户注册',
    description='用户注册接口',
    dependencies=[Depends(RateLimiter(times=5, minutes=1))],
)
async def user_register(
    request: Request, response: Response, obj: RegisterUserParam, background_tasks: BackgroundTasks
) -> ResponseSchemaModel[object]:
    # data = await auth_service.register(request=request, response=response, obj=obj, background_tasks=background_tasks)
    await user_service.register(obj=obj)
    return response_base.success()
