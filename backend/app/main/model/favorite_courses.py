from sqlalchemy import TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.common.model import Base, id_key
from backend.utils.timezone import timezone
from datetime import datetime


class FavoriteCourse(Base):
    """用户收藏课程表"""

    __tablename__ = 'favorite_courses'

    id: Mapped[id_key] = mapped_column(init=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False, comment='用户ID')
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id', ondelete='CASCADE'), nullable=False, comment='课程ID')
    # added_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=timezone.now, comment='添加时间')

    # 收藏与用户多对一
    user: Mapped['User'] = relationship(back_populates='favorite_courses', init=False)  # noqa: F821
    # 收藏与课程多对一
    course: Mapped['Course'] = relationship(back_populates='favorite_courses', init=False)  # noqa: F821
