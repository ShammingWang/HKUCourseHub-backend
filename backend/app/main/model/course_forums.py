from sqlalchemy import String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.common.model import Base, id_key
from backend.utils.timezone import timezone
from datetime import datetime


class CourseForum(Base):
    """课程论坛表"""

    __tablename__ = 'course_forums'

    id: Mapped[id_key] = mapped_column(init=False)
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id', ondelete='CASCADE'), nullable=False, comment='课程ID')
    title: Mapped[str] = mapped_column(String(255), nullable=False, comment='标题')
    content: Mapped[str] = mapped_column(Text, nullable=False, comment='内容')
    created_by: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False, comment='创建者')
    # created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=timezone.now, comment='创建时间')

    # 论坛与课程多对一
    course: Mapped['Course'] = relationship(back_populates='course_forums', init=False)  # noqa: F821
    # 论坛与用户多对一
    creator: Mapped['User'] = relationship(back_populates='course_forums', init=False)  # noqa: F821
    # 论坛与回复一对多
    forum_replies: Mapped[list['ForumReply']] = relationship(back_populates='forum', cascade='all, delete-orphan', init=False)  # noqa: F821
