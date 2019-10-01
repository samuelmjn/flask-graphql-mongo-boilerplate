import logging
from constants import CONFIGS
from flask import Flask, jsonify, make_response
from flask_graphql import GraphQLView
from flask_cors import CORS
from resolvers import global_schema

logging.basicConfig(
    level=CONFIGS.get("LOG_LEVEL"),
    format="%(asctime)s %(levelname)s: %(message)s " "[in %(pathname)s:%("
           "lineno)d]",
    datefmt="%Y%m%d-%H:%M%p",
)

app = Flask(__name__)
CORS(app)
app.debug = CONFIGS.get("DEBUG")

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=global_schema,
                                  graphiql=True)
)


@app.route("/")
def main():
    return "GraphQL server is listening on /graphql"

# error handler
@app.errorhandler(404)
def page_not_found(error):
    json_response = jsonify({'error': 'Page not found'})
    return make_response(json_response, CONFIGS['HTTP_STATUS']['404_NOT_FOUND'])
