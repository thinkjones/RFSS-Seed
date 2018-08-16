"""

"""
import sys

from server.db.managers.maintenance_manager import MaintenanceManager


def query_maintenance():
    print 'History for {u}'.format(u=sys.argv[1])
    history, to_dict = MaintenanceManager.history(sys.argv[1])
    print [to_dict(h) for h in history]


if __name__ == '__main__':
    query_maintenance()
