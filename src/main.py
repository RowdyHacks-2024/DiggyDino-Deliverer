from os import getenv
from .api import app

from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType

if __name__=='__main__':
    DEBUG = getenv('DEBUG')

    assert DEBUG is not None

    DEBUG = DEBUG.lower() == 'true'
    app.run( debug = DEBUG )

query = ObjectType("Query")

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)
