from sqlalchemy import TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.common.model import Base, id_key
from backend.utils.timezone import timezone
from datetime import datetime


class UserCourse(Base):
    """用户选课表"""

    __tablename__ = 'user_courses'

    id: Mapped[id_key] = mapped_column(init=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False, comment='用户ID')
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id', ondelete='CASCADE'), nullable=False, comment='课程ID')

    # 选课与用户多对一
    user: Mapped['User'] = relationship(back_populates='user_courses')  # noqa: F821
    # 选课与课程多对一
    course: Mapped['Course'] = relationship(back_populates='user_courses')  # noqa: F821
    
    # added_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=timezone.now, comment='添加时间')