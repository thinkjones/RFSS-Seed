from server.db.database import db_session
from server.db.models.user import User, UserType
from server.db.managers import get_timebased_uuid


class UserManager(object):

    @staticmethod
    def add(name, email, userType):
        if name is None or email is None or userType not in [UserType.HUMAN, UserType.AUTOMATED]:
            raise ValueError('Name, Email and UserType must be specified correctly')

        new_item = User(name=name, email=email, type=userType)
        new_item.id = get_timebased_uuid()
        db_session.add(new_item)
        db_session.commit()
        return new_item

    @staticmethod
    def all_real_users():
        return User.query.filter_by(type=UserType.HUMAN).all()

    @staticmethod
    def all():
        return User.query.all()
