from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.common.model import Base, id_key

class CourseTeacher(Base):
    """课程教师表"""

    __tablename__ = 'course_teachers'

    id: Mapped[id_key] = mapped_column(init=False)
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id', ondelete='CASCADE'), nullable=False, comment='课程ID')
    teacher_name: Mapped[str] = mapped_column(String(100), nullable=False, comment='教师名称')

    # 教师与课程多对一
    course: Mapped['Course'] = relationship(back_populates='course_teachers', init=False)  # noqa: F821
