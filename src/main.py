from os import getenv
from api import app, db, resolvers
from api.models import *
from ariadne.explorer import ExplorerApollo
from ariadne import graphql_sync
from flask import request, jsonify


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

query.set_field("get_user", resolvers.resolve_get_user)
query.set_field("get_detector", resolvers.resolve_get_detector)
query.set_field("get_prediction", resolvers.resolve_get_prediction)
query.set_field("get_sample", resolvers.resolve_get_sample)


mutation = ObjectType("Mutation")

mutation.set_field("add_user", resolvers.resolve_add_user)
mutation.set_field("update_user", resolvers.resolve_update_user)
mutation.set_field("delete_user", resolvers.resolve_delete_user)

mutation.set_field("add_detector", resolvers.resolve_add_detector)
mutation.set_field("update_detector", resolvers.resolve_update_detector)
mutation.set_field("delete_detector", resolvers.resolve_delete_detector)

mutation.set_field("add_sample", resolvers.resolve_add_sample)
mutation.set_field("update_sample", resolvers.resolve_update_sample)
mutation.set_field("delete_sample", resolvers.resolve_delete_sample)

mutation.set_field("add_prediction", resolvers.resolve_add_prediction)
mutation.set_field("update_prediction", resolvers.resolve_update_prediction)
mutation.set_field("delete_prediction", resolvers.resolve_delete_prediction)

type_defs = load_schema_from_path("schema.gql")
schema = make_executable_schema(
    type_defs,
    query,
    mutation,
    snake_case_fallback_resolvers )


EXPLORER_HTML = ExplorerApollo().html(None)

@app.route("/", methods=["GET"])
def graphql_explore():
    return EXPLORER_HTML

@app.route("/", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value={"request": request},
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
