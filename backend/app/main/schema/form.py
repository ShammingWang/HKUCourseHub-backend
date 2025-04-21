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
    created_time: datetime
    
class CreateForumParam(SchemaBase):
    """创建课程论坛数据模型"""
    # id: int  数据库自增主键
    course_id: int
    title: str
    content: str
    # created_by: int
    
class CreateForum(CreateForumParam):
    created_by: int
