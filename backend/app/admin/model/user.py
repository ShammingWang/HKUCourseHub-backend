from datetime import datetime
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from backend.common.model import Base, id_key

class User(Base):
    """用户表"""
    __tablename__ = 'users'

    id: Mapped[id_key] = mapped_column(init=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, comment='用户名')
    email: Mapped[str] = mapped_column(String(100), unique=True, comment='邮箱')
    password_hash: Mapped[str] = mapped_column(String(255), comment='密码哈希')
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp(), comment='创建时间') 
