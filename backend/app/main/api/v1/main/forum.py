from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response, Path
# from sqlalchemy.orm import Session
from backend.app.main.schema.form import GetForumDetail

from backend.app.main.service.forum_service import forum_service
from backend.app.main.service.user_service import user_service
from backend.app.main.service.course_service import course_service
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

