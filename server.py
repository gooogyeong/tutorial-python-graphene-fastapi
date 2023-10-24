from starlette.applications import Starlette
from starlette.routing import Route
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from fastapi import FastAPI
from schema import schema
from starlette.responses import PlainTextResponse

def homepage(request):
    return PlainTextResponse('Hello, world!')

routes = [
    Route('/', homepage),
]

app = Starlette(routes=routes)

app.mount("/graphql", GraphQLApp(schema=schema, on_get=make_graphiql_handler()))  # Graphiql IDE

