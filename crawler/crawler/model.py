from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from . import settings

Base = declarative_base()


def db_connect():
    connect = URL.create(**settings.DATABASE)
    return create_engine(connect)


def create_table(engine):
    Base.metadata.create_all(engine)


class ScrapyData(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    url = Column('url', String)
