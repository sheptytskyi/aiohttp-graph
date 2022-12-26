from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models import Base

engine = create_engine(
    'postgresql://postgres:root@localhost/aiohttp-graph',
    echo=True
)

Session = scoped_session(sessionmaker(bind=engine))
session = Session()

Base.query = Session.query_property()


def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
