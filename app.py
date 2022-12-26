from aiohttp import web
from aiohttp_graphql import GraphQLView
from graphql.execution.executors.asyncio import AsyncioExecutor

from config import engine, Base
from schema import schema


async def db_init(app: web.Application) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def init() -> web.Application:
    app = web.Application()
    app.on_startup.append(db_init)

    GraphQLView.attach(app, schema=schema, graphiql=True, executor=AsyncioExecutor())

    return app


if __name__ == '__main__':
    web.run_app(init())
