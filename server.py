import asyncio

import graphene
# from graphene_file_upload.scalars import Upload

from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from fastapi import FastAPI
from schema import schema

app=FastAPI()

# app.add_route('/graphql', GraphQLApp(schema=schema))

# @app.get("/")
# async def index():
#     return {"message": "Hello World"}

app = Starlette()
# schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)

app.mount("/", GraphQLApp(schema=schema, on_get=make_graphiql_handler()))  # Graphiql IDE

# @app.get("/")
# async def index():
#     return {"message": "Hello World"}

# app.mount("/", GraphQLApp(schema, on_get=make_playground_handler()))  # Playground IDE
# app.mount("/", GraphQLApp(schema)) # no IDE

