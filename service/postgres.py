from sqlalchemy     import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib     import contextmanager


#region connection as session
port = '54322'
host = 'localhost'
user = 'postgres'
pswd = 'postgres'
db   = 'test'

connection_string = f'postgresql://{user}:{pswd}@{host}:{port}/{db}'

engine  = create_engine(connection_string)
Session = sessionmaker(bind=engine)
#endregion


class PostgresSvc: # aka. Postgres Service

    @classmethod
    @contextmanager # this helps to get around the error 'AttributeError: __exit__' #TODO why is that?
    def get_session(cls):
        """
        IMPORTANT NOTE
        we are creating a python generator ref. https://stackoverflow.com/a/231855/248616, NOT a normal method
        *yield* is used in place of *return* #TODO master this point, what the h*** is this ^^?
        """
        session = Session(expire_on_commit=False)
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
    def run_sql(cls, sql):
        """ref. https://stackoverflow.com/a/17987782/248616"""
        from sqlalchemy import text
        return engine.execute(text(sql))
