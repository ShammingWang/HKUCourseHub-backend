from pydantic import ConfigDict, Field, field_validator
from backend.common.schema import SchemaBase
from datetime import date, time
from enum import Enum

class CourseScheduleSchemaBase(SchemaBase):
    id: int
    course_id: int
    schedule_date: date
    day_of_week: str
    start_time: time
    end_time: time
    location: str

class GetCourseScheduleDetail(SchemaBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    # course_id: int  # 不需要返回课程ID
    schedule_date: date
    day_of_week: str
    start_time: time
    end_time: time
    location: str


class DayOfWeekEnum(str, Enum):
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"
    sunday = "Sunday"

class CreateCourseSchedule(SchemaBase):
    course_id: int = Field(..., description="课程ID")
    schedule_date: date = Field(..., description="上课日期")
    day_of_week: DayOfWeekEnum = Field(..., description="星期几")
    start_time: time = Field(..., description="开始时间")
    end_time: time = Field(..., description="结束时间")
    location: str = Field(..., description="上课地点")

    @field_validator("end_time")
    @classmethod
    def check_time_range(cls, end_time: time, info):
        start_time = info.data.get("start_time")
        if start_time and end_time <= start_time:
            raise ValueError("结束时间必须晚于开始时间")
        return end_time

class UpdateCourseSchedule(SchemaBase):
    id: int = Field(..., description="课程安排ID")
    # course_id: int = Field(..., description="课程ID")  # 不能更新课程ID
    schedule_date: date = Field(..., description="上课日期")
    day_of_week: DayOfWeekEnum = Field(..., description="星期几")
    start_time: time = Field(..., description="开始时间")
    end_time: time = Field(..., description="结束时间")
    location: str = Field(..., description="上课地点")

    @field_validator("end_time")
    @classmethod
    def check_time_range(cls, end_time: time, info):
        start_time = info.data.get("start_time")
        if start_time and end_time <= start_time:
            raise ValueError("结束时间必须晚于开始时间")
        return end_time