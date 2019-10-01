import string
import pytest
from __init__ import app
from random import choice
from constants import CONFIGS
from utils.model import profile_collections

url = CONFIGS.get("APP_URL")
client = app.test_client()


def test_root_endpoint():
    """
    / endpoint (GET)
    Fetches root route
    """
    global client
    res = client.get("/")
    assert res.status_code == 200, "failed get resuest"
    assert res.data == b"GraphQL server is listening on /graphql"


def test_registration():
    """
    /graphql endpoint (GET)
    Registers a test account
    """
    global client
    query = {"query": """{
      register(email: "test@test.com", password: "password", username: "test", name: "test") {
        email
        token
      }
    }"""}
    res = client.post("{}/graphql".format(url), json=query)
    assert res.status_code == 200
    assert res.json["data"]


def test_profile_exists():
    """
    /graphql endpoint (GET)
    Tries to re-register the same account
    """
    global client
    query = {"query": """{
      register(email: "test@test.com", password: "password", username: "test", name: "test") {
        email
        token
      }
    }"""}
    res = client.post("{}/graphql".format(url), json=query)
    print(res.json)
    assert len(res.json["errors"]) == 1
    assert res.json["errors"][0][
               "message"] == "Profile with that username currently exists in the system."


def test_login():
    """
    /graphql endpoint (GET)
    Login's to created account
    """
    global client
    query = {"query": """
    {
      login(username: "test", password: "password") {
        email
        token
      }
    }
    """}
    res = client.post("{}/graphql".format(url), json=query)
    assert res.status_code == 200


def test_profile():
    """
    /graphql endpoint (GET)
    Token authentication to fetch profile data
    """
    global client
    query_profile = {"query": """
       {
         login(username: "test", password: "password") {
           email
           token
         }
       }
   """}
    res = client.post("{}/graphql".format(url), json=query_profile)
    token = res.json['data']['login']['token']
    query = {
        "query": "{profile(token: \"" + token + "\") { email name username " \
                                                "isVerified }}"}
    res = client.post("{}/graphql".format(url), json=query)
    assert res.status_code == 200


def test_login_wrong_password():
    """
    /graphql endpoint (GET)
    Tries to login with false credentials
    """
    global client
    query = {"query": """
      {
        login(username: "test", password: "wrong") {
          email
          token
        }
      }
      """}
    client.post("{}/graphql".format(url), json=query)
    with pytest.raises(Exception) as exception:
        assert exception == "The password is incorrect. Please try again."


def test_long_no_profile():
    """
    /graphql endpoint (GET)
    Deletes and tries to fetch deleted account
    """
    global client
    test_remove_created_account()
    query = {"query": """"
    {
      login(username: "test", password: "I don't exist") {
        email
        token
      }
    }
    """}
    client.post("{}/graphql".format(url), json=query)
    with pytest.raises(Exception) as exception:
        assert exception == "The profile by the username test, was not found in the system."


def test_user_wrong_token():
    """ Test trying to authenticate with an unsigned token """
    global client

    def random(len=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(choice(letters) for _ in range(len))

    query = {"query": "{profile(token: \"" + random(
        50) + "\") { email name username isVerified }}"}
    client.post("graphql".format(url), json=query)
    with pytest.raises(Exception) as exception:
        assert exception == "Token is invalid."


def test_remove_created_account():
    """ Drop the test profile from database """
    assert profile_collections.delete_one({"username": "test"})
