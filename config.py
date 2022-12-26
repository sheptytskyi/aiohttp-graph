import os

from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

load_dotenv('.env')

DATABASE_URL = f'''postgresql+asyncpg://{os.environ['DB_USER']}:{os.environ['DB_PASS']}
                    @{os.environ['DB_HOST']}/{os.environ['DB_NAME']}'''


def _async_db_uri(uri: str) -> str:
    if 'asyncpg' not in uri:
        uri = uri.split(':', 1)[0] + '+asyncpg' + ':' + uri.split(':', 1)[1]

    return uri


engine = create_async_engine(_async_db_uri(DATABASE_URL), future=True, echo=True)
CustomAsyncSession = scoped_session(
    sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
)
async_session = CustomAsyncSession()
Base = declarative_base()
