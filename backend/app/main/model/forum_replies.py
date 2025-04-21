from sqlalchemy import Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.common.model import Base, id_key
from backend.utils.timezone import timezone
from datetime import datetime


class ForumReply(Base):
    """论坛回复表"""

    __tablename__ = 'forum_replies'

    id: Mapped[id_key] = mapped_column(init=False)
    forum_id: Mapped[int] = mapped_column(ForeignKey('course_forums.id', ondelete='CASCADE'), nullable=False, comment='论坛ID')
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False, comment='用户ID')
    content: Mapped[str] = mapped_column(Text, nullable=False, comment='回复内容')
    # created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=timezone.now, comment='创建时间')

    # 回复与论坛多对一
    forum: Mapped['CourseForum'] = relationship(back_populates='forum_replies', init=False)  # noqa: F821
    # 回复与用户多对一
    user: Mapped['User'] = relationship(back_populates='forum_replies', init=False)  # noqa: F821
