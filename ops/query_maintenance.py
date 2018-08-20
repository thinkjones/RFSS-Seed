"""

"""
import sys

from server.db.managers.maintenance_manager import MaintenanceManager


def query_maintenance():
    aircraft_id = sys.argv[1]
    print 'History for Aircraft {u}'.format(u=aircraft_id)
    history, to_dict = MaintenanceManager.history(aircraft_id)
    print [to_dict(h) for h in history]

    health = MaintenanceManager.aircraft_health(aircraft_id)
    print 'Health: {h}'.format(h=health)

if __name__ == '__main__':
    query_maintenance()
