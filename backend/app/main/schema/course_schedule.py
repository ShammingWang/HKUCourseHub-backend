from pydantic import ConfigDict
from backend.common.schema import SchemaBase
from datetime import date


class CourseScheduleSchemaBase(SchemaBase):
    id: int
    # course_id: int
    schedule_date: date
    day_of_week: str
    start_time: str
    end_time: str
    location: str

class GetCourseScheduleDetail(CourseScheduleSchemaBase):
    # 这个很重要 返回给前端的数据必须是padantic的模型 这里允许从sqlalchemy的模型中直接转换
    model_config = ConfigDict(from_attributes=True)
    pass
