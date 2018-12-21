from sqlalchemy     import create_engine, text
from sqlalchemy.orm import sessionmaker
from contextlib     import contextmanager
import sys

from model._base_     import DeclarativeBase
from service.parallel import get_current_process_thread_id
from config           import port, host, user, pswd, db


class PostgresSvc: # aka. Postgres Service

    @classmethod
    def make_session(cls, user, pswd, host, port, db):
        connection_string = f'postgresql://{user}:{pswd}@{host}:{port}/{db}'
        engine            = create_engine(connection_string)
        Session           = sessionmaker(bind=engine)
        return Session, engine, connection_string


    @classmethod
    @contextmanager # this helps to get around the error 'AttributeError: __exit__' #TODO why is that?
    def get_session(cls):
        """
        IMPORTANT NOTE
        we are creating a python generator ref. https://stackoverflow.com/a/231855/248616, NOT a normal method
        *yield* is used in place of *return* #TODO master this point, what the h*** is this ^^?
        """

        global user, pswd, host, port, db
        global Session, engine, connection_string

        Session2, engine2, connection_string2 = None,None,None
        if sys._called_from_test: # we're in testing, connection to be as test method's config if any
            test_id      = sys.require_isolated_db.get(get_current_process_thread_id())
            session_data = sys.test_sessions.get(test_id)
            if session_data:
                Session2, engine2, connection_string2 = session_data
                print(f'Loaded isolated session for test_id={test_id}')

        if Session2: session = Session2(expire_on_commit=False) # load :Session2 as test's :require_isolated_db session
        else:        session = Session(expire_on_commit=False)  # load :Session as common :test db
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()


    @classmethod
    def insert(cls, model_instance):
        with cls.get_session() as session:
            session.add(model_instance)
            session.commit()
            session.refresh(model_instance)
            return model_instance


    @classmethod
    def update(cls, model_instance):
        """
        In sqlalchemy, update+insert are same when saving to db
        """
        with cls.get_session() as session:
            session.add(model_instance)
            session.commit()
            session.refresh(model_instance)
            return model_instance


    @classmethod
    def run_sql(cls, sql, engine_obj=None):
        """ref. https://stackoverflow.com/a/17987782/248616"""
        if engine_obj is None: engine_obj=engine
        return engine_obj.execute(text(sql))


    @classmethod
    def create_all_postgres_tables(cls, engine_obj=None):
        if engine_obj is None: engine_obj=engine
        DeclarativeBase.metadata.create_all(engine_obj)


    #region db crud
    @classmethod
    def create_db(cls, db_name):
        from sqlalchemy import create_engine
        from sqlalchemy_utils import database_exists, create_database

        eg = create_engine(f'postgresql://{user}:{pswd}@{host}:{port}/{db_name}') # eg aka. engine
        if not database_exists(eg.url): create_database(eg.url) # ref. https://stackoverflow.com/a/30971098/248616
        print(f'Created db {db_name}')


    @classmethod
    def drop_db(cls, db_name):
        from sqlalchemy import create_engine
        from sqlalchemy_utils import database_exists, drop_database

        eg = create_engine(f'postgresql://{user}:{pswd}@{host}:{port}/{db_name}') # eg aka. engine
        if database_exists(eg.url): drop_database(eg.url) # ref. https://stackoverflow.com/a/30971098/248616
        print(f'Dropped db {db_name}')


    @classmethod
    def drop_all_postgres_tables(cls):
        from model._base_ import DeclarativeBase
        tables = ','.join(table.name for table in reversed(DeclarativeBase.metadata.sorted_tables))
        with PostgresSvc.get_session() as session:
            session.execute(f'DROP TABLE if exists {tables} CASCADE;')
    #endregion db crud


Session, engine, connection_string = PostgresSvc.make_session(user, pswd, host, port, db)
