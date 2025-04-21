from sqlalchemy_crud_plus import CRUDPlus


from backend.app.main.model.forum_replies import ForumReply


class CRUDUser(CRUDPlus[ForumReply]):
    pass

forum_reply_dao: CRUDUser = CRUDUser(ForumReply)
