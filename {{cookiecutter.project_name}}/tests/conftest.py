import pytest
from {{cookiecutter.app_name}} import create_app


@pytest.fixture()
def app():
    """
    Fixture for creating the Flask app.

    Yields
    ------
    Flask app :
        The created Flask app.
    """
    yield create_app()


@pytest.fixture()
def graphql(client):
    """
       Fixture for making GraphQL queries.
       This fixture yields a function facilitating making GraphQL queries.
    """

    def graphql_query(query):
        # send the GraphQL to the server.
        res = client.post('/graphql', json=query)

        # return the server response
        return res

    yield graphql_query
