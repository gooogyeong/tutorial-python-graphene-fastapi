from graphene import ObjectType, String, Int, Field, Schema, Mutation, relay
from db import PersonModel, session
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

class PersonSchema(SQLAlchemyObjectType):
    class Meta:
        model = PersonModel
        interfaces = (relay.Node, )

class Query(ObjectType):
    node = relay.Node.Field()
    allPeople = SQLAlchemyConnectionField(PersonSchema.connection)
    person=Field(PersonSchema, id=Int())

    def resolve_all_people(root, info):
        query = PersonModel.get_query(info)
        return query.all()
    
    def resolve_person(root, info, id):
        person = session.query(PersonModel).get(id)
        return person
    
class CreatePerson(Mutation):
    class Arguments:
        email = String()
        first_name = String()
        last_name = String()
        age = Int()

    person = Field(lambda: PersonSchema)
    
    def mutate(self, info, email, first_name, last_name, age):
        person = PersonModel(email=email, first_name=first_name, last_name=last_name, age=age)
        session.add(person)
        session.commit()

        return CreatePerson(person=person)
    
class Mutation(ObjectType):
    create_person = CreatePerson.Field()
    
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

# result = schema.execute(query_string, context_value={'session': session})
# print(result) # ExecutionResult(data={'allPeople': {'edges': [{'node': {'email': 'db@gmail.com', 'lastName': 'master'}}]}}, errors=None)

# FastAPI: exposes what we get from console to frontend