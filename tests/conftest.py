import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from graphene.test import Client
from schema import schema
from db import Base

@pytest.fixture(scope="function")
def session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)  # Create all tables
    Session = scoped_session(sessionmaker(bind=engine))
    session = Session()

    yield session

    session.close()
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def client(session):
    client = Client(schema)
    
    return client, {"session": session}
