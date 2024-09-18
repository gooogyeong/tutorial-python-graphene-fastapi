from starlette.applications import Starlette
from starlette.routing import Route
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schema import schema
from starlette.responses import PlainTextResponse, JSONResponse

async def index(request):
    return JSONResponse({"message": "Hello, world"})

routes = [
    Route('/', index),
]

origins = [
    "http://localhost:3000",
]

app = Starlette(routes=routes)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/graphql", GraphQLApp(schema=schema, on_get=make_graphiql_handler()))  # Graphiql IDE

