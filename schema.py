from graphene import ObjectType, String, Int, Field, Schema, List, Mutation, relay
from db import PersonModel, session
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

"""
    class PersonType:
        email: str
        first_name: str
        last_name: str
        age: int
"""

from models import data

class PersonType(ObjectType):
    email = String() 
    first_name = String()
    last_name = String()
    age = Int()

    # def reolsve_email(self, info):
    #     return self.email

    # def resolve_fisrt_name(self, info):
    #     return self.first_name
    
    # def resolve_last_name(self, info):
    #     return self.last_name
    
    # def resolve_age(self, info):
    #     return self.age

class PersonSchema(SQLAlchemyObjectType):
    class Meta:
        model = PersonModel
        interfaces = (relay.Node, )

class Query(ObjectType):
    node = relay.Node.Field()
    # all_people=List(PersonType)
    allPeople = SQLAlchemyConnectionField(PersonSchema.connection)
    # person=Field(PersonType, key=Int())
    person=Field(PersonSchema, id=Int())

    def resolve_all_people(root, info):
        # return data.values()
        query = PersonModel.get_query(info)
        return query.all()
    
    def resolve_person(root, info, id):
        # TODO
        # return data[key]
        person = session.query(PersonModel).get(id)
        return person
    
class CreatePerson(Mutation):
    class Arguments:
        email = String()
        first_name = String()
        last_name = String()
        age = Int()

    # person = Field(lambda: PersonType)
    person = Field(lambda: PersonSchema)
    
    def mutate(self, info, email, first_name, last_name, age):
        # person = PersonType(email=email, first_name=first_name, last_name=last_name, age=age)
        # data[len(data)+1] = person
        
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
#             email 
#             lastName
#         }
#     }
# """

# print(schema.execute(query_string))
# executionResult(data={'allPeople': [{'email': 'johndoe@gmail.com', 'lastName': 'Doe'}, {'email': 'janedoe@gmail.com', 'lastName': 'Doe'}, {'email': 'johnsmith@gmail.com', 'lastName': 'Smith'}, {'email': 'jasonross@gmail.com', 'lastName': 'Ross'}]}, errors=None)

# FastAPI: exposes what we get from console to frontend

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