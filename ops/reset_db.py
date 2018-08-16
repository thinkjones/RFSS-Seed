"""

"""
from server.db.database import drop_tables, init_db
from ops.populate_db import populate_db


def reset_db():
    drop_tables()
    init_db()
    populate_db()
    print 'Database reset and populated with demo data'


if __name__ == '__main__':
    reset_db()
