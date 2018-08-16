from sqlalchemy import Column, Integer, String

from server.db.database import Base


class UserType(object):
    HUMAN = 'human'
    AUTOMATED = 'automated'


class User(Base):
    """ Books in a library """
    __tablename__ = 'user'
    id = Column(String(25), primary_key=True)
    name = Column(String(50))
    email = Column(String(100))
    type = Column(String(10))

    def __repr__(self):
        return '<User %r>' % (self.name)
