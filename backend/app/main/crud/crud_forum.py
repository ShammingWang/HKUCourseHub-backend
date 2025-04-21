from sqlalchemy_crud_plus import CRUDPlus


from backend.app.main.model.course_forums import CourseForum


class CRUDUser(CRUDPlus[CourseForum]):
    pass

course_forum_dao: CRUDUser = CRUDUser(CourseForum)
