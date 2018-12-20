"""
common stuffs among model classes
"""

from ._base_ import DeclarativeBase #model base class

#table column type
from sqlalchemy import Column, UniqueConstraint, ForeignKey
from sqlalchemy import String, Integer, Boolean, SmallInteger, BigInteger, DateTime, Date, Float

#crud command
from sqlalchemy import select, update, insert, delete

#json column
from sqlalchemy.ext.mutable              import MutableDict
from sqlalchemy.dialects.postgresql.json import JSONB

#hybrid property
from sqlalchemy.ext.hybrid import hybrid_property
