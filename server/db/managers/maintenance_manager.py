from server.db.database import db_session
from server.db.models.aircraft import Aircraft, AircraftHealth
from server.db.models.maintenance import Maintenance
from server.db.models.user import User
from server.db.managers import get_timebased_uuid
from server.db.managers.aircraft_manager import AircraftManager
from datetime import datetime
from sqlalchemy.orm import aliased
from sqlalchemy.sql.functions import count

class MaintenanceManager(object):

    @staticmethod
    def add(user_id, aircraft_id, description, blocked=True):
        if user_id is None or aircraft_id is None or description is None:
            raise ValueError('user_id, aircraft_id, or description must be specified correctly')

        # Add Maintenance Record
        new_item = Maintenance(description=description,
                               created=datetime.utcnow(),
                               created_by_id=user_id,
                               aircraft_id=aircraft_id,
                               completed=False,
                               blocked=blocked)
        new_item.id = get_timebased_uuid()

        aircraft = AircraftManager.get(aircraft_id)
        if aircraft.health != AircraftHealth.BLOCKING:
            aircraft.health = AircraftHealth.BLOCKING if blocked else AircraftHealth.NON_BLOCKING

        db_session.add(new_item)
        db_session.commit()
        return new_item

    @staticmethod
    def get(id):
        return Maintenance.query.get(id)

    @staticmethod
    def all():
        return Maintenance.query.all()

    @staticmethod
    def completed(id):
        maintenance = MaintenanceManager.get(id)
        maintenance.completed = True
        db_session.commit()
        return maintenance.aircraft_id, MaintenanceManager.aircraft_health(maintenance.aircraft_id)

    @staticmethod
    def history(aircraft_id):
        created_by_user = aliased(User)
        fixed_by_user = aliased(User)
        query = db_session.query(Aircraft.id.label('aircraft_id'),
                                 Aircraft.name.label('aircraft_name'),
                                 Maintenance.id.label('maintenance_id'),
                                 Maintenance.description,
                                 Maintenance.created,
                                 created_by_user.name.label('created_by_name'),
                                 Maintenance.fixed,
                                 fixed_by_user.name.label('fixed_by_name'),
                                 Maintenance.blocked,
                                 Maintenance.completed)
        query = query.join(Maintenance)
        query = query.join(created_by_user, created_by_user.id == Maintenance.created_by_id)
        query = query.outerjoin(fixed_by_user, Maintenance.fixed_by_id == fixed_by_user.id)
        query = query.filter(Aircraft.id == aircraft_id)
        query = query.order_by(Maintenance.created.desc())
        return query.all(), MaintenanceManager.history_to_dict

    @staticmethod
    def aircraft_health(aircraft_id):
        query1 = db_session.query(count(Maintenance.id))
        query1 = query1.filter(Maintenance.aircraft_id == aircraft_id,
                               Maintenance.completed == False)
        total_maintenance = query1.scalar()

        query2 = db_session.query(count(Maintenance.id))
        query2 = query2.filter(Maintenance.aircraft_id == aircraft_id,
                               Maintenance.completed == False,
                               Maintenance.blocked == True)
        total_blocking_maintenance = query2.scalar()

        if total_maintenance == 0:
            return AircraftHealth.GOOD
        elif total_blocking_maintenance == 0:
            return AircraftHealth.NON_BLOCKING
        elif total_blocking_maintenance > 0:
            return AircraftHealth.BLOCKING

    @staticmethod
    def history_to_dict(i):
        return {'aircraft_id': i.aircraft_id,
                'aircraft_name': i.aircraft_name,
                'maintenance_id': i.maintenance_id,
                'description': i.description,
                'created': i.created.isoformat() if i.created is not None else None,
                'created_by': i.created_by_name,
                'fixed': i.fixed.isoformat() if i.fixed is not None else None,
                'fixed_by': i.fixed_by_name,
                'blocked': i.blocked,
                'completed': i.completed}
