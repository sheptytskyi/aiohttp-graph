from aiohttp import web
from aiohttp_graphql import GraphQLView
from graphql.execution.executors.asyncio import AsyncioExecutor

from app.database import db
from app.schema import schema


async def init() -> web.Application:
    app = web.Application()
    db.init()
    app.on_startup.append(db.create_all)
    app.on_shutdown.append(db.dispose)

    GraphQLView.attach(app, schema=schema, graphiql=True, executor=AsyncioExecutor())

    return app


if __name__ == '__main__':
    web.run_app(init())
