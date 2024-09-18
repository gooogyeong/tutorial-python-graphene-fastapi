from graphene import ObjectType, String, Field, Schema, Mutation, relay, List, InputObjectType, Float, ID
from db import RectangleModel, session
from graphene_sqlalchemy import SQLAlchemyObjectType

class RectangleSchema(SQLAlchemyObjectType):
    class Meta:
        model = RectangleModel

class Query(ObjectType):
    node = relay.Node.Field()

    rectangles=List(RectangleSchema)

    rectangle=Field(RectangleSchema)

    def resolve_rectangles(root, info, **args):
        query = RectangleSchema.get_query(info)

        return query.all()

class RectangleInput(InputObjectType):
    width = Float()
    height = Float()
    x = Float()
    y = Float()
    color = String()

class AddRectangle(Mutation):
    class Arguments:
        width = Float()
        height = Float()
        x = Float()
        y = Float()
        color = String()

    id  = ID()
    width = Float()
    height = Float()
    x = Float()
    y = Float()
    color = String()
    
    def mutate(self, info, x, y, width, height, color):
        new_rectangle = RectangleModel(x=x, y=y, width=width, height=height, color=color)

        session.add(new_rectangle)
        session.commit()

        return AddRectangle(id=new_rectangle.id, width=new_rectangle.width, height=new_rectangle.height, x=new_rectangle.x, y=new_rectangle.y, color=new_rectangle.color)
    
class DeleteRectangles(Mutation):
    class Arguments:
        ids = List(ID)

    Output = List(ID)

    def mutate(self, info, ids):
        rectangles_to_delete = session.query(RectangleModel).filter(RectangleModel.id.in_(ids)).all()

        if not rectangles_to_delete:
            raise Exception("No rectangles found for the given IDs.")
        
        for rectangle in rectangles_to_delete:
            session.delete(rectangle)
        session.commit()

        return ids

    
class Mutation(ObjectType):
    add_rectangle = AddRectangle.Field()
    delete_rectangles = DeleteRectangles.Field()
    
schema=Schema(query=Query, mutation=Mutation)

# query_string="""
#     {
#         allPeople {
#             edges {
#                 node {
#                     email 
#                     lastName   
#                 }
#             }
#         }
#     }
# """

# query_string="""
#     mutation {
#         addRectangle(x: 10, y: 10, width: 10.0, height: 10.0, color: "red") {
#             id
#             width
#             height
#             x
#             y
#             color
#         }
#     }
# # """

query_string="""
    mutation {
        deleteRectangles(ids: ["21"])
    }
# """



result = schema.execute(query_string, context_value={'session': session})
# print(result) # ExecutionResult(data={'allPeople': {'edges': [{'node': {'email': 'db@gmail.com', 'lastName': 'master'}}]}}, errors=None)
print('=== print something ===')
# print(result) # {'allPeople': {'edges': [{'node': {'email': 'db@gmail', 'lastName': 'master'}}]}}
print(result) # ExecutionResult(data={'rectangles': {'edges': []}}, errors=None)

# FastAPI: exposes what we get from console to frontend