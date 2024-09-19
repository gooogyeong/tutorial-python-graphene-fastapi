from starlette.applications import Starlette
from starlette.routing import Route
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse, JSONResponse

from db import SessionLocal
from schema import schema

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

async def get_context_value(request: Request):
    session = SessionLocal()
    try:
        # Pass the session in the context
        return {"session": session}
    finally:
        session.close()

app.mount("/graphql", GraphQLApp(schema=schema, on_get=make_graphiql_handler(), context_value=get_context_value))  # Graphiql IDE

