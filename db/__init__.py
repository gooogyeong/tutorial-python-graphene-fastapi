from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from graphene import relay
import os

Base = declarative_base()

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_str = "sqlite:///" + os.path.join(BASE_DIR, "tutorial-python-graphene-fastapi.db")

engine = create_engine(connection_str)  # create db in project folder

SessionLocal = sessionmaker(bind=engine) # scoped_session(sessionmaker(bind=engine))
session = scoped_session(SessionLocal)

Base.query = session.query_property()

class RectangleModel(Base):
    __tablename__ = 'rectangle'
    id = Column(Integer, primary_key=True)
    width = Column(Float)
    height = Column(Float)
    x = Column(Float)
    y = Column(Float)
    color = Column(String)

Base.metadata.create_all(engine)