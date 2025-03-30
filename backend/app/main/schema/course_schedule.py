from pydantic import ConfigDict
from backend.common.schema import SchemaBase
from datetime import date


class CourseScheduleSchemaBase(SchemaBase):
    id: int
    course_id: int
    schedule_date: date
    day_of_week: str
    start_time: str
    end_time: str
    location: str

class GetCourseScheduleDetail(SchemaBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    # course_id: int  # 不需要返回课程ID
    schedule_date: date
    day_of_week: str
    start_time: str
    end_time: str
    location: str
