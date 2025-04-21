#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import Select
from typing import List
from backend.app.main.crud.crud_forum import course_forum_dao
from backend.app.main.schema.form import GetForumDetail

from backend.database.db import async_db_session


class ForumService:
    @staticmethod
    async def get_forums_by_course_id(*, course_id: int) -> List[GetForumDetail]:
        async with async_db_session() as db:
            forums = await course_forum_dao.select_models(db, course_id=course_id)
            for forum in forums:
                await db.refresh(forum, ['creator'])
            return [GetForumDetail.model_validate(forum) for forum in forums]


forum_service: ForumService = ForumService()
