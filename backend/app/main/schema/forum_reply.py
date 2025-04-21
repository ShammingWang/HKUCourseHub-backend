from datetime import datetime
from pydantic import ConfigDict
from backend.common.schema import SchemaBase
from backend.app.main.schema.user import GetUserInfoDetail


class ForumReplySchemaBase(SchemaBase):
    """课程论坛回复基础数据模型"""
    id: int
    forum_id: int
    user_id: int
    content: str
    created_time: datetime

class GetForumReplyDetail(ForumReplySchemaBase):
    model_config = ConfigDict(from_attributes=True)
    user: GetUserInfoDetail  # 额外返回创建者User的信息

class CreateForumReplyParam(SchemaBase):
    """创建课程论坛回复参数"""
    forum_id: int
    content: str

class CreateForumReply(CreateForumReplyParam):
    """创建课程论坛回复参数"""
    user_id: int
