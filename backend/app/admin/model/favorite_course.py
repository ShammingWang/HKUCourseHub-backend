from datetime import datetime
from sqlalchemy import ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from backend.common.model import Base, id_key

class FavoriteCourse(Base):
    """课程收藏表"""
    __tablename__ = 'favorite_courses'

    id: Mapped[id_key] = mapped_column(init=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), comment='用户ID')
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id'), comment='课程ID')
    added_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp(), comment='添加时间') 