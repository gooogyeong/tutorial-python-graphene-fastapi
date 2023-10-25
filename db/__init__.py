from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from graphene import relay
import os

Base = declarative_base()

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_str = "sqlite:///" + os.path.join(BASE_DIR, "tutorial-python-graphene-fastapi.db")

engine = create_engine(connection_str, echo=True)  # create db in project folder
session = scoped_session(sessionmaker(bind=engine))
Base.query = session.query_property()

class PersonModel(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)