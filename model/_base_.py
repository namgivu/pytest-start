from sqlalchemy.ext.declarative import declarative_base


class BaseModel(object):

    @classmethod
    def get_columns(cls):
        return cls.metadata.tables[cls.__tablename__].columns.keys()


    def to_dict(self):
        """
        convert *model_obj.column* to *dict['column']*
        """
        d = {}

        #region extract db columns to dict
        columns = self._sa_class_manager.mapper.mapped_table.columns
        for c in columns:
            d[c.name] = getattr(self, c.name)

        #alternative implementation
        #return {c.key: getattr(self, c.key)
        #    for c in inspect(self).mapper.column_attrs}

        pass
        #endregion extract db columns

        return d


    def __repr__(self):
        from pprint import pformat
        return pformat(self.to_dict())


    @classmethod
    def find_all(cls):
        from service.postgres import PostgresSvc # import locally here to dodge circular reference
        with PostgresSvc.get_session() as session:
            rows = session.query(cls).all()
            return rows


DeclarativeBase = declarative_base(cls=BaseModel)
