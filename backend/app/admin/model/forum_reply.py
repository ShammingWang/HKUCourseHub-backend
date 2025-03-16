from datetime import datetime
from sqlalchemy import Text, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from backend.common.model import Base, id_key

class ForumReply(Base):
    """讨论回复表"""
    __tablename__ = 'forum_replies'

    id: Mapped[id_key] = mapped_column(init=False)
    forum_id: Mapped[int] = mapped_column(ForeignKey('course_forums.id'), comment='讨论ID')
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), comment='用户ID')
    content: Mapped[str] = mapped_column(Text, comment='内容')
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp(), comment='创建时间') 