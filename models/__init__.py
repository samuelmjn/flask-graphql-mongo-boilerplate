import bcrypt
from faker import Faker
from constants import CONFIGS
from mongoengine import connect
from models.profile_model import ProfileModel

db = connect(CONFIGS.get("MONGO_DB"), host=CONFIGS.get("MONGO_URL"),
             alias='default')


def mock(count: int) -> str:
    """
     Prepopulates the Mongo graphql with mock data
    :param: count the amount of fake people to generate
    :returns: an indicator that the operation has been completed
    :rtype: str
    """
    # populate data
    for i in range(count):
        fake = Faker().profile(fields=None, sex=None)
        ProfileModel(name=fake["name"], username=fake["username"],
                     email=fake["mail"],
                     password=bcrypt.hashpw('fake pass'.encode('utf-8'),
                                            bcrypt.gensalt()).decode(
                         "utf-8")).save()
        print("Created: {0}".format(fake["username"]))

    return "Finished populating DB"


def drop() -> str:
    """
    :returns: an indicator that the operation has been completed
    :rtype: str
    """
    db_to_drop = CONFIGS.get("MONGO_DB")
    db.drop_database(db_to_drop)
    return "{0} has been dropped.".format(db_to_drop)
