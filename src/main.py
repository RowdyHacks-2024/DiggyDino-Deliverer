from os import getenv
from .api import app, db, models, resolvers

from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType

if __name__=='__main__':
    DEBUG = getenv('DEBUG')

    assert DEBUG is not None

    DEBUG = DEBUG.lower() == 'true'
    app.run( debug = DEBUG )

with app.app_context():
    db.create_all()

query = ObjectType("Query")
query.set_field("user", resolvers.resolve_add_user)

type_defs = load_schema_from_path("schema.gql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)
