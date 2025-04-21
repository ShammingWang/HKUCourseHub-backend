from typing import List
from fastapi import APIRouter, Request, Response
from backend.common.response.response_schema import ResponseSchemaModel, response_base
from backend.common.security.jwt import DependsJwtAuth
from backend.app.main.schema.user_course import UserCourseSchemaBase
from backend.app.main.schema.favorite_course import UserFavoriteCourseSchemaBase
from backend.app.main.crud.crud_user_course import user_course_dao
from backend.app.main.crud.crud_user_favorite_course import user_favorite_course_dao
from backend.database.db import async_db_session


router = APIRouter()

@router.get(
    "/sys/all_user_course",
    summary="查询系统所有用户选课表",
    description="查询系统所有用户选课表",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def get_all_user_coourse(
    request: Request,
    response: Response,
) -> ResponseSchemaModel[List[UserCourseSchemaBase]]:
    async with async_db_session() as db:
        user_course_list = await user_course_dao.select_models(db)
        # print(user_course_list[0])
        # user_course_0 = UserCourseSchemaBase.model_validate(user_course_list[0])
        return response_base.success(
            data=[UserCourseSchemaBase.model_validate(user_course) for user_course in user_course_list])


@router.get(
    "/sys/all_user_favorite_course",
    summary="查询系统所有用户收藏课表",
    description="查询系统所有用户收藏课表",
    dependencies=[
        DependsJwtAuth,  # 需要jwt认证
    ]
)
async def get_all_user_favorite_course(
    request: Request,
    response: Response,
) -> ResponseSchemaModel[List[UserFavoriteCourseSchemaBase]]:
    async with async_db_session() as db:
        user_favorite_course_list = await user_favorite_course_dao.select_models(db)
        return response_base.success(
            data=[UserFavoriteCourseSchemaBase.model_validate(user_favorite_course) for user_favorite_course in user_favorite_course_list])
