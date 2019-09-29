import uuid
from faker import Faker
from auth import encrypt_password
from constants import CONFIGS
from pymongo import MongoClient

conn = MongoClient(CONFIGS.get("MONGO_URL"), retryWrites=False)

profile_collections = conn[CONFIGS.get("MONGO_DB")].profiles


def mock(count: int) -> str:
    """
     Pre-populates the Mongo graphql with mock data
    :param: count the amount of fake people to generate
    :returns: an indicator that the operation has been completed
    :rtype: str
    """
    # populate data
    for i in range(count):
        fake = Faker().profile(fields=None, sex=None)
        profile_collections.insert_one({
            'email': fake["mail"],
            'password': encrypt_password('password'),
            "name": fake["name"],
            "username": fake["username"],
            "is_check": {
                "status": False,
                "id": uuid.uuid1()
            },
        })

        print("Created: {0}".format(fake["username"]))

    return "Finished populating DB"


def drop() -> str:
    """
    :returns: an indicator that the operation has been completed
    :rtype: str
    """
    db_to_drop = CONFIGS.get("MONGO_DB")
    conn.drop_database(db_to_drop)
    return "{0} has been dropped.".format(db_to_drop)
