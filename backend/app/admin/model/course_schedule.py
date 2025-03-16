from sqlalchemy import Enum, Time, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from backend.common.model import Base, id_key

class CourseSchedule(Base):
    """课程时间安排表"""
    __tablename__ = 'course_schedules'

    id: Mapped[id_key] = mapped_column(init=False)
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id'), comment='课程ID')
    day_of_week: Mapped[str] = mapped_column(Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'), comment='星期几')
    start_time: Mapped[time] = mapped_column(Time, comment='开始时间')
    end_time: Mapped[time] = mapped_column(Time, comment='结束时间')
    location: Mapped[str] = mapped_column(String(255), comment='上课地点') 