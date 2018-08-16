from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from server.db.database import Base
from sqlalchemy.orm import relationship
from server.db.models.user import User


class Maintenance(Base):
    """ A reservation of a book in the library """
    __tablename__ = 'maintenance'
    id = Column(String(25), primary_key=True)
    description = Column(String(500))

    created = Column(DateTime, nullable=False)
    created_by_id = Column(String(25), ForeignKey('user.id'), nullable=False)
    created_by = relationship(User, foreign_keys='Maintenance.created_by_id', lazy="joined")

    fixed = Column(DateTime, nullable=True)
    fixed_by_id = Column(String(25), ForeignKey('user.id'), nullable=True)
    fixed_by = relationship(User, foreign_keys='Maintenance.fixed_by_id', lazy="joined")

    aircraft_id = Column(String(25), ForeignKey('aircraft.id'), nullable=False)
    aircraft = relationship("Aircraft")

    blocked = Column(Boolean, nullable=False, default=True)

    completed = Column(Boolean, nullable=False, default=True)

    def __repr__(self):
        return '<Maintenance %r>' % (self.description)
