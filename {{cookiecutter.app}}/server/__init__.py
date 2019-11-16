import logging

from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flask_graphql import GraphQLView

from constants import CONSTANTS
from server.resolvers.auth import authentication_schema

logging.basicConfig(
    level=CONSTANTS.get("LOG_LEVEL"),
    format="%(asctime)s %(levelname)s: %(message)s " "[in %(pathname)s:%("
           "lineno)d]",
    datefmt="%Y%m%d-%H:%M%p",
)

app = Flask(__name__)
CORS(app)
app.debug = CONSTANTS.get("DEBUG")

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=authentication_schema,
                                  graphiql=True)
)


@app.route("/")
def main():
    return "GraphQL server is listening on /graphql"


# error handler
@app.errorhandler(404)
def page_not_found(error):
    print(error)
    response = jsonify({'error': 'Page not found'})
    return make_response(response, CONSTANTS['HTTP_STATUS']['404_NOT_FOUND'])
