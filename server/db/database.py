from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData


engine = create_engine('sqlite:///zipstatus.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()



def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import server.db.models.user
    import server.db.models.aircraft
    import server.db.models.maintenance
    Base.metadata.create_all(bind=engine)


def drop_tables():
    init_db()
    Base.metadata.drop_all(bind=engine)
