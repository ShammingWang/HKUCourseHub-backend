from sqlalchemy import String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.common.model import Base, id_key
from backend.utils.timezone import timezone
from datetime import datetime



class Course(Base):
    """课程表"""

    __tablename__ = 'courses'

    id: Mapped[id_key] = mapped_column(init=False)
    course_code: Mapped[str] = mapped_column(String(50), nullable=False, comment='课程代码')
    course_name: Mapped[str] = mapped_column(String(100), nullable=False, comment='课程名称')
    course_description: Mapped[str | None] = mapped_column(Text, comment='课程描述')
    semester: Mapped[str] = mapped_column(String(20), nullable=False, comment='学期')
    created_by: Mapped[int | None] = mapped_column(ForeignKey('users.id', ondelete='SET NULL'), comment='创建者')
    # created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=timezone.now, comment='创建时间')

    # 课程与用户一对一
    creator: Mapped['User'] = relationship(back_populates='courses')  # noqa: F821
    # 课程与教师一对多
    course_teachers: Mapped[list['CourseTeacher']] = relationship(back_populates='course', cascade='all, delete-orphan')  # noqa: F821
    # 课程与时间表一对多
    course_schedules: Mapped[list['CourseSchedule']] = relationship(back_populates='course', cascade='all, delete-orphan')  # noqa: F821
    # 课程与选课多对多
    user_courses: Mapped[list['UserCourse']] = relationship(back_populates='course', cascade='all, delete-orphan')  # noqa: F821
    # 课程与收藏多对多
    favorite_courses: Mapped[list['FavoriteCourse']] = relationship(back_populates='course', cascade='all, delete-orphan')  # noqa: F821
    # 课程与论坛一对多
    course_forums: Mapped[list['CourseForum']] = relationship(back_populates='course', cascade='all, delete-orphan')  # noqa: F821
