from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String, select
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, scoped_session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_scoped_session

DATABASE_URL = 'postgresql+asyncpg://postgres:root@localhost/aiohttp-graph'

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
CustomAsyncSession = scoped_session(
    sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
)
async_session = CustomAsyncSession()
Base = declarative_base()



class Hall(Base):
    __tablename__ = 'halls'

    id = Column(Integer, primary_key=True)
    city = Column(String, nullable=False)
    street = Column(String, nullable=False)

    def __str__(self):
        return f'Hall in city {self.city} on street {self.street}'


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __str__(self):
        return f'User: {self.name}'


class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)

    hall_id = Column(Integer, ForeignKey('halls.id'), nullable=False)
    hall = relationship('Hall',
                        backref='hall',
                        foreign_keys=[hall_id])
    coach_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    coach = relationship('User', backref='coach', foreign_keys=[coach_id])

    def __str__(self):
        return f'Lesson in {self.hall} with coach {self.coach}'
