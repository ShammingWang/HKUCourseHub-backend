from backend.common.schema import SchemaBase
from pydantic import ConfigDict, Field
from typing import Optional

class CourseTeacherSchemaBase(SchemaBase):
    id: int
    course_id: int
    teacher_name: str

class GetCourseTeacherDetail(SchemaBase):
    """获取教师课程详情"""
    pass
    model_config = ConfigDict(from_attributes=True)
    id: int
    # course_id: int  # 不需要返回课程ID
    teacher_name: str

class CreateCourseTeacher(SchemaBase):
    """创建教师课程"""
    course_id: int = Field(..., description="课程ID")
    teacher_name: str = Field(..., description="教师ID")

class UpdateCourseTeacher(SchemaBase):
    """更新教师课程"""
    id: int = Field(..., description="教师课程关系ID")
    teacher_name: str = Field(..., description="教师ID")
