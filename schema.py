from graphene import ObjectType, String, Int, Field, Schema, List

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

class Query(ObjectType):
    all_people=List(PersonType)
    person=Field(PersonType, key=Int())

    def resolve_all_people(root, info):
        return data.values()
    
    def resolve_person(root, info, key):
        return data[key]
    
schema=Schema(query=Query)

# query_string="{allPeople{email lastName}}"

# print(schema.execute(query_string))
# executionResult(data={'allPeople': [{'email': 'johndoe@gmail.com', 'lastName': 'Doe'}, {'email': 'janedoe@gmail.com', 'lastName': 'Doe'}, {'email': 'johnsmith@gmail.com', 'lastName': 'Smith'}, {'email': 'jasonross@gmail.com', 'lastName': 'Ross'}]}, errors=None)

# FastAPI: exposes what we get from console to frontend