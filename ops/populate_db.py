"""

"""
from server.db.managers.aircraft_manager import AircraftManager
from server.db.managers.user_manager import UserManager
from server.db.models.user import User, UserType
from server.db.managers.aircraft_manager import AircraftManager
from server.db.managers.maintenance_manager import MaintenanceManager
from server.db.models.aircraft import AircraftHealth


def populate_db():
    u1 = UserManager.add('Operator User', 'operator@zips.com', UserType.HUMAN)
    u2 = UserManager.add('Automated User', 'automator@zips.com', UserType.AUTOMATED)

    a1 = AircraftManager.add('Zip 21', AircraftHealth.GOOD)
    a2 = AircraftManager.add('Zip 44', AircraftHealth.GOOD)
    a3 = AircraftManager.add('Zip 66', AircraftHealth.GOOD)

    MaintenanceManager.add(u2.id, a1.id, 'Tail assembly loose', blocked=False)
    MaintenanceManager.add(u2.id, a2.id, 'Left tail outboard servo needs to be checked', blocked=True)
    MaintenanceManager.add(u2.id, a2.id, 'Broken left wing tip on recovery', blocked=True)

    print 'Database Populated'


if __name__ == '__main__':
    populate_db()
