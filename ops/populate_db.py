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

    aircraft_names = ['Zip 21', 'Zip 44', 'Zip 66']
    aircraft = []
    for a in aircraft_names:
        item = AircraftManager.add(a, AircraftHealth.GOOD)
        print '{a} id is {id}'.format(a=a, id=item.id)
        aircraft.append(item)

    MaintenanceManager.add(u2.id, aircraft[0].id, 'Tail assembly loose', blocked=False)
    MaintenanceManager.add(u2.id, aircraft[1].id, 'Left tail outboard servo needs to be checked', blocked=True)
    MaintenanceManager.add(u2.id, aircraft[1].id, 'Broken left wing tip on recovery', blocked=True)

    print 'Database Populated'


if __name__ == '__main__':
    populate_db()
