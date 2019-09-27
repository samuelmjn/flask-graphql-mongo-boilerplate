import bcrypt
from constants import CONFIGS
from mongoengine import connect
from models import Profile

connect(CONFIGS.get("MONGO_DB"), host=CONFIGS.get("MONGO_URL"), alias='default')


def mock() -> None:
    """
    Prepopulates the Mongo database with mock data
    """
    # populate data

    roy = Profile()
    roy.name = 'Roy'
    roy.email = 'roy.hibbert@mock.com'
    roy.password = \
        bcrypt.hashpw('roy.hibbert'.encode('utf-8'), bcrypt.gensalt()).decode(
            "utf-8")
    roy.save()

    tracy = Profile()
    tracy.name = 'Tracy'
    tracy.email = 'tracy.morgan@mock.com'
    tracy.password = bcrypt.hashpw('tracy.morgan'.encode('utf-8'),
                                   bcrypt.gensalt()).decode("utf-8")
    tracy.save()

    print("Finished populating DB")


if __name__ == "__main__":
    mock()
