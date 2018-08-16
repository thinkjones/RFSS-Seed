from sqlalchemy import Column, Integer, String
from server.db.database import Base


class AircraftHealth(object):
    GOOD = 'good'                           # No Maintenance Outstanding
    NON_BLOCKING = 'non_blocking'           # No Blocking Maintenance Outstanding
    BLOCKING = 'blocking'                   # Blocking Maintenance Outstanding


class Aircraft(Base):
    """ Books in a library """
    __tablename__ = 'aircraft'
    id = Column(String(25), primary_key=True)
    name = Column(String(50), unique=True)
    health = Column(String(20))

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'health': self.health
        }

    def __repr__(self):
        return '<Aircraft %r>' % (self.name)
