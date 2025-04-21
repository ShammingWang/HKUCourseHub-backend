from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response, Path
# from sqlalchemy.orm import Session
from backend.app.main.schema.form import GetForumDetail, CreateForumParam
from backend.app.main.schema.forum_reply import CreateForumReplyParam, GetForumReplyDetail
from backend.app.main.service.forum_service import forum_service
from backend.common.response.response_schema import ResponseSchemaModel, response_base
from backend.common.security.jwt import DependsJwtAuth



router = APIRouter()

@router.get(
    "/forum/{courde_id}",
    summary="查询课程论坛列表",
    description="查询课程论坛列表",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def get_forums_by_course_id(
    request: Request,
    courde_id: int = Path(..., title="课程ID", description="课程ID"),
    # response: Response
) -> ResponseSchemaModel[List[GetForumDetail]]:
    # user_id = request.user.id
    forums = await forum_service.get_forums_by_course_id(course_id=courde_id)
    return response_base.success(data=forums)


@router.post(
    "/forum",
    summary="新增课程论坛",
    description="新增课程论坛",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def add_forum_by_course_id(
    request: Request,
    obj: CreateForumParam,
    # courde_id: int = Path(..., title="课程ID", description="课程ID"),
    # response: Response
) -> ResponseSchemaModel[None]:
    user_id = request.user.id
    await forum_service.add_forum_by_course_id(obj=obj, user_id=user_id)
    return response_base.success(data=None)

@router.delete(
    "/forum/{forum_id}",
    summary="删除课程论坛",
    description="根据论坛ID删除课程论坛",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def delete_forum_by_id(
    request: Request,
    forum_id: int = Path(..., title="论坛ID", description="课程论坛的唯一ID")
) -> ResponseSchemaModel[None]:
    user_id = request.user.id
    await forum_service.delete_forum_by_id(forum_id=forum_id, user_id=user_id)
    return response_base.success(data=None)



@router.get(
    "/forum/reply/{forum_id}",
    summary="根据论坛ID查询论坛回复",
    description="根据论坛ID查询论坛回复",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def get_replies_by_forum_id(
    request: Request,
    response: Response,
    forum_id: int = Path(..., title="论坛ID", description="课程论坛的唯一ID"),
) -> ResponseSchemaModel[List[GetForumReplyDetail]]:
    # user_id = request.user.id
    replies = await forum_service.get_replies_by_forum_id(forum_id=forum_id)
    return response_base.success(data=replies)


@router.post(
    "/forum/reply",
    summary="新增论坛回复",
    description="新增论坛回复",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def add_reply_by_forum_id(
    request: Request,
    obj: CreateForumReplyParam,
    response: Response
) -> ResponseSchemaModel[None]:
    user_id = request.user.id
    await forum_service.add_reply_by_forum_id(obj=obj, user_id=user_id)
    return response_base.success(data=None)


@router.delete(
    "/forum/reply/{reply_id}",
    summary="根据回复ID删除课程论坛回复",
    description="根据回复ID删除课程论坛回复",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def delete_reply_by_id(
    request: Request,
    response: Response,
    reply_id: int = Path(..., title="回复ID", description="论坛回复的唯一ID"),
) -> ResponseSchemaModel[None]:
    user_id = request.user.id  # 获取当前登录用户ID
    await forum_service.delete_reply_by_id(reply_id=reply_id, user_id=user_id)
    return response_base.success(data=None)
