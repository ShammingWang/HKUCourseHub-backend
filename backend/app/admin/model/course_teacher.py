from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from backend.common.model import Base, id_key

class CourseTeacher(Base):
    """课程教师表"""
    __tablename__ = 'course_teachers'

    id: Mapped[id_key] = mapped_column(init=False)
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id'), comment='课程ID')
    teacher_name: Mapped[str] = mapped_column(String(100), comment='教师姓名') 