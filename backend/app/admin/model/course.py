from datetime import datetime
from sqlalchemy import ForeignKey, String, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.common.model import Base, id_key

class Course(Base):
    """课程表"""
    __tablename__ = 'courses'

    id: Mapped[id_key] = mapped_column(init=False)
    course_code: Mapped[str] = mapped_column(String(50), comment='课程代码')
    course_name: Mapped[str] = mapped_column(String(100), comment='课程名称')
    course_description: Mapped[str | None] = mapped_column(Text, comment='课程描述')
    semester: Mapped[str] = mapped_column(String(20), comment='学期')
    created_by: Mapped[int | None] = mapped_column(ForeignKey('users.id'), comment='创建者')
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp(), comment='创建时间')
