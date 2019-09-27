import bcrypt
from faker import Faker
from constants import CONFIGS
from mongoengine import connect
from model.profile_model import ProfileModel

connect(CONFIGS.get("MONGO_DB"), host=CONFIGS.get("MONGO_URL"), alias='default')
salt = bcrypt.gensalt()


def mock(count: int) -> None:
    """
    Prepopulates the Mongo graphql with mock data
    @:param count the amount of fake people to generate
    """
    # populate data
    for i in range(count):
        fake = Faker().profile(fields=None, sex=None)
        ProfileModel(name=fake["name"], username=fake["username"],
                     email=fake["mail"],
                     password=bcrypt.hashpw('fake pass'.encode('utf-8'),
                                            salt).decode(
                         "utf-8")).save()

    print("Finished populating DB")
