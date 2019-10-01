from flask_script import Manager
from __init__ import app
from utils.model import mock, drop

manager = Manager(app)


@manager.command
def drop_database():
    """ Drops the database specified in the configuration file. """
    return drop()


@manager.option("-c", "--count", help="The amount of fake accounts to create")
def populate_with_mock_data(count: int) -> str:
    """Creates the db tables."""
    if count:
        print("Preparing to create", count, "fake accounts")
        return mock(int(count))
    else:
        return mock(1)


if __name__ == "__main__":
    manager.run()
