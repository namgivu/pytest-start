import datetime

from ._imports_       import *
from model._base_     import BaseModel
from service.postgres import PostgresSvc


class User(DeclarativeBase, BaseModel):
    __tablename__ = 'users'

    id         = Column(Integer, primary_key=True, autoincrement=True)
    email      = Column(String)
    dob        = Column(Date)
    created_at = Column(DateTime, default=datetime.datetime.now())

    #region json column
    extra_info  = Column(JSONB, default={})
    custom_cols = Column(MutableDict.as_mutable(JSONB), default={})
    '''
    NOTE
    Why we use Column(MutableDict.as_mutable(JSONB) but not plain `Column(JSONB)?
    --> Simply that JSONB cannot record updates while MutableDict.as_mutable(JSONB) can
    '''
    #endregion


    @staticmethod
    def create(fields:dict):
        u = User(**fields)
        return PostgresSvc.insert(u)
