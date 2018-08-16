"""

"""
import sys

from server.db.managers.maintenance_manager import MaintenanceManager
from server.db.managers.aircraft_manager import AircraftManager


def query_maintenance():
    print 'Maintenance is completed for {u}'.format(u=sys.argv[1])
    aircraft_id, health = MaintenanceManager.completed(sys.argv[1])
    AircraftManager.set_health(aircraft_id, health)
    print 'Aircraft Health is now "{r}"'.format(r=health)

if __name__ == '__main__':
    query_maintenance()
