from datetime import datetime
from sqlalchemy import String, TIMESTAMP, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.common.model import Base, id_key
from backend.utils.timezone import timezone

class User(Base):
    """用户表"""

    __tablename__ = 'users'

    id: Mapped[id_key] = mapped_column(init=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, comment='用户名')
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, comment='邮箱')
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False, comment='密码哈希')
    # created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=timezone.now, comment='创建时间')

    # 用户与课程一对多
    courses: Mapped[list['Course']] = relationship(back_populates='creator', cascade='all, delete-orphan')  # noqa: F821
    # 用户与选课多对多
    user_courses: Mapped[list['UserCourse']] = relationship(back_populates='user', cascade='all, delete-orphan')  # noqa: F821
    # 用户与收藏课程多对多
    favorite_courses: Mapped[list['FavoriteCourse']] = relationship(back_populates='user', cascade='all, delete-orphan')  # noqa: F821
    # 用户与论坛帖子一对多
    course_forums: Mapped[list['CourseForum']] = relationship(back_populates='creator', cascade='all, delete-orphan')  # noqa: F821
    # 用户与论坛回复一对多
    forum_replies: Mapped[list['ForumReply']] = relationship(back_populates='user', cascade='all, delete-orphan')  # noqa: F821
