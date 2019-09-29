import logging
from constants import CONFIGS
from flask import Flask
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
    return "GraphQL Server is listening on /graphql"
