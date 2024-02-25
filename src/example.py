
from ariadne.asgi import GraphQL
from ariadne import MutationType, gql, QueryType, make_executable_schema
from ariadne.explorer import ExplorerGraphiQL

# Define type definitions (schema) using SDL
type_defs = gql(
   """
   type Query {
       places: [Place]
   }

   type Mutation {
       edit_place(name: String!): Response
   }

   type Place {
       name: String!
       description: String!
       country: String!
       }
    
    type Response {
        content: String!
    }
   """
)

# Initialize query

query = QueryType()

mutation = MutationType()

# Define resolvers
@query.field("places")
def places(*_):
   return [
       {"name": "Paris", "description": "The city of lights", "country": "France"},
       {"name": "Rome", "description": "The city of pizza", "country": "Italy"},
       {
           "name": "London",
           "description": "The city of big buildings",
           "country": "United Kingdom",
       },
       {"name": "asdfasdfasdf", "description": "The city of pizza", "country": "Italy"}
   ]

@mutation.field("edit_place")
def edit_name(obj, infom, name):
    return {"content": name}

# Create executable schema
schema = make_executable_schema(type_defs, query, mutation)

# Create ASGI application
app = GraphQL(schema)
