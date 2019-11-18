"""Top-level package for {{ cookiecutter.app_name }}."""

__author__ = """{{ cookiecutter.author }}"""
__version__ = '{{ cookiecutter.version }}'

import logging
{% if cookiecutter.sentry_sdk == "yes" %}import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration{% endif %}
{% if cookiecutter.log_to_file == "yes" %}from logging.handlers import RotatingFileHandler{% endif %}
from flask.logging import default_handler
from flask import Flask, jsonify, make_response, current_app
from flask_cors import CORS
from flask_graphql import GraphQLView
from {{cookiecutter.app_name}}.constants import CONSTANTS
from {{cookiecutter.app_name}}.resolvers.auth import authentication_schema


def _log_exception(exception):
    """
    Log an exception to Flask's logger.
    ----------
    exception : Exception
        The exception to log.
    """

    current_app.logger.exception(exception)
    {% if cookiecutter.sentry_sdk == "yes" %}
    sentry_sdk.capture_exception(exception)
    {% endif %}

class LoggingMiddleware:
    def on_error(self, error):
        _log_exception(error)
        raise error

    def resolve(self, next, root, info, **args):
        return next(root, info, **args).catch(self.on_error)


app = Flask(__name__)
CORS(app)
{% if cookiecutter.log_to_file == "yes" %}
log_file_path = CONSTANTS.get("LOG_FILE_PATH")
rfh = RotatingFileHandler(log_file_path, maxBytes=CONSTANTS.get("LOG_MAX_BYTES"),
                          backupCount=CONSTANTS.get("BACKUP_COUNT"))
rfh.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
app.logger.addHandler(rfh)
{% else %}
app.logger.addHandler(default_handler)
{% endif %}

{% if cookiecutter.sentry_sdk == "yes" %}# Setting up sentry sdk
sentry_dsn = CONSTANTS.get('SENTRY_DSN')
if not sentry_dsn:
    app.logger.info('No value is defined for SENTRY_DSN. Have you defined an '
                    'environment variable with this name?')
sentry_sdk.init(
    dsn=sentry_dsn,
    integrations=[FlaskIntegration()]
)
{% endif %}
app.debug = CONSTANTS.get("DEBUG")

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=authentication_schema,
                                  middleware=[LoggingMiddleware()], graphiql=True))

@app.route("/")
def main():
    return "GraphQL server is listening on /graphql"

# error handlers
@app.errorhandler(404)
def page_not_found(error):
    _log_exception(error)
    response = jsonify({'error': 'Page not found'})
    return make_response(response, CONSTANTS['HTTP_STATUS']['404_NOT_FOUND'])


@app.errorhandler(500)
def internal_server_error(error):
    _log_exception(error)
    response = jsonify({'error': 'Internal server error'})
    return make_response(response, CONSTANTS['HTTP_STATUS']['500_INTERNAL_ERROR'])


@app.errorhandler(Exception)
def exception_raised(error):
    _log_exception(error)
    response = jsonify({'error': 'Internal server error'})
    return make_response(response, CONSTANTS['HTTP_STATUS']['500_INTERNAL_ERROR'])


def create_app() -> Flask:
    return app
