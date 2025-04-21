#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import Select
from typing import List
from backend.app.main.crud.crud_forum import course_forum_dao
from backend.app.main.crud.crud_course import course_dao
from backend.app.main.schema.form import GetForumDetail, CreateForumParam, CreateForum
from backend.common.exception import errors

from backend.database.db import async_db_session


class ForumService:
    @staticmethod
    async def get_forums_by_course_id(*, course_id: int) -> List[GetForumDetail]:
        async with async_db_session() as db:
            # 先查询课程是否存在
            course = await course_dao.select_model(db, pk=course_id)
            if not course:
                raise errors.RequestError()
            
            forums = await course_forum_dao.select_models(db, course_id=course_id)
            for forum in forums:
                await db.refresh(forum, ['creator'])
            return [GetForumDetail.model_validate(forum) for forum in forums]

    @staticmethod
    async def add_forum_by_course_id(*, obj: CreateForumParam, user_id: int):
        course_id = obj.course_id

        async with async_db_session() as db:
            # 先查询课程是否存在
            course = await course_dao.select_model(db, pk=course_id)
            if not course:
                raise errors.RequestError()

            await course_forum_dao.create_model(
                db,
                CreateForum(
                    **obj.model_dump(),  
                    created_by=user_id,  
                ),
                commit=True  # 关键点
            )

    @staticmethod
    async def delete_forum_by_id(forum_id: int, user_id: int):
        async with async_db_session() as db:
            obj = await course_forum_dao.select_model(db, pk=forum_id)
            if obj is None:
                raise errors.NotFoundError(msg="未找到该课程论坛")
            if obj.created_by != user_id:
                raise errors.ForbiddenError(msg="你无权删除他人的帖子")
            await course_forum_dao.delete_model(db, pk=forum_id, commit=True)

forum_service: ForumService = ForumService()
