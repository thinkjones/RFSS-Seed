from server.db.database import db_session
from server.db.models.aircraft import Aircraft, AircraftHealth
from server.db.managers import get_timebased_uuid


class AircraftManager(object):

    @staticmethod
    def add(name, health):
        if name is None or health not in [AircraftHealth.GOOD, AircraftHealth.BLOCKING, AircraftHealth.NON_BLOCKING]:
            raise ValueError('Name or Health must be specified correctly')

        new_item = Aircraft(name=name, health=health)
        new_item.id = get_timebased_uuid()
        db_session.add(new_item)
        db_session.commit()
        return new_item

    @staticmethod
    def get(id):
        return Aircraft.query.get(id)

    @staticmethod
    def all():
        return Aircraft.query.all()

    @staticmethod
    def set_health(id, health):
        aircraft = AircraftManager.get(id)
        aircraft.health = health
        db_session.commit()
        return AircraftManager.get(id)
