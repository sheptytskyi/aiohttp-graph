from aiohttp import web
from aiohttp_graphql import GraphQLView

from db import init_db
from schema import schema

app = web.Application()
GraphQLView.attach(app, schema=schema, graphiql=True)


if __name__ == '__main__':
    # init_db()
    web.run_app(app)
