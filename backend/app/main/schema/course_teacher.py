from backend.common.schema import SchemaBase
from pydantic import ConfigDict
from typing import Optional

class TeacherCourseSchemaBase(SchemaBase):
    id: int
    course_id: int
    teacher_name: str

class GetTeacherCourseDetail(SchemaBase):
    """获取教师课程详情"""
    pass
    model_config = ConfigDict(from_attributes=True)
    id: int
    teacher_name: str
