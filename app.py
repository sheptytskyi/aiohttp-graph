from aiohttp import web
from aiohttp_graphql import GraphQLView
from graphql.execution.executors.asyncio import AsyncioExecutor

from app.config import engine, Base
from app.schema import schema


async def db_init(app: web.Application) -> None:
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def close_db(app: web.Application) -> None:
    await engine.dispose()


async def init() -> web.Application:
    app = web.Application()
    app.on_startup.append(db_init)
    app.on_shutdown.append(close_db)

    GraphQLView.attach(app, schema=schema, graphiql=True, executor=AsyncioExecutor())

    return app


if __name__ == '__main__':
    web.run_app(init())
