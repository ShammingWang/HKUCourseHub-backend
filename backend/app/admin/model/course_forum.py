from datetime import datetime
from sqlalchemy import String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from backend.common.model import Base, id_key

class CourseForum(Base):
    """课程讨论表"""
    __tablename__ = 'course_forums'

    id: Mapped[id_key] = mapped_column(init=False)
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id'), comment='课程ID')
    title: Mapped[str] = mapped_column(String(255), comment='标题')
    content: Mapped[str] = mapped_column(Text, comment='内容')
    created_by: Mapped[int] = mapped_column(ForeignKey('users.id'), comment='创建者')
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp(), comment='创建时间') 