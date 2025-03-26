from sqlalchemy import String, Enum, Time, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.common.model import Base, id_key
from datetime import time, date


class CourseSchedule(Base):
    """课程时间表"""

    __tablename__ = 'course_schedules'

    id: Mapped[id_key] = mapped_column(init=False)
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id', ondelete='CASCADE'), nullable=False, comment='课程ID')
    schedule_date: Mapped[date] = mapped_column(Date, nullable=False, comment='日期')
    day_of_week: Mapped[str] = mapped_column(Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'), nullable=False, comment='星期几')
    start_time: Mapped[time] = mapped_column(nullable=False, comment='开始时间')
    end_time: Mapped[time] = mapped_column(nullable=False, comment='结束时间')
    location: Mapped[str] = mapped_column(String(255), nullable=False, comment='上课地点')

    # 时间表与课程多对一
    course: Mapped['Course'] = relationship(back_populates='course_schedules')  # noqa: F821
