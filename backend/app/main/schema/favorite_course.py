from backend.common.schema import SchemaBase
from pydantic import ConfigDict, Field
from typing import Optional


class UserFavoriteCourseSchemaBase(SchemaBase):
    id: int
    course_id: int
    user_id: int

class CreateUserFavoriteCourse(SchemaBase):
    course_id: int
    user_id: int
