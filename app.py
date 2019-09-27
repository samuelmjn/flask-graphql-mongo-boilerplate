from flask import Flask
from flask_graphql import GraphQLView
from database import mock
from global_schema import global_schema

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=global_schema, graphiql=True)
)

if __name__ == '__main__':
    mock(2)
    app.run()
