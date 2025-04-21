from datetime import datetime
from pydantic import ConfigDict
from backend.common.schema import SchemaBase
from backend.app.main.schema.user import GetUserInfoDetail

class ForumSchemaBase(SchemaBase):
    """课程论坛基础数据模型"""
    id: int
    course_id: int
    title: str
    content: str
    created_by: int
    # updated_at: str
    

class GetForumDetail(ForumSchemaBase):
    model_config = ConfigDict(from_attributes=True)
    creator: GetUserInfoDetail  # 额外返回创建者User的信息
