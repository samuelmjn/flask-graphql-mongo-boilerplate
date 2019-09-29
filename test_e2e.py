# test_e2e.py
import requests
import urllib.parse
from random import choice
import string
from constants import CONFIGS
from models import profile_collections

# Please make sure to start the server before starting the e2e test suite
url = CONFIGS.get("APP_URL")


def test_root_endpoint():
    """
    / endpoint (GET)
    Fetches root route
    """
    req = requests.get("{}/".format(url))
    assert req.status_code == 200, "failed get request"
    print(req.content)
    assert req.content.decode(
        "utf-8") == "GraphQL server is listening on /graphql"


def test_registration():
    """
    /graphql endpoint (GET)
    Registers a test account
    """
    query = """
    {
      register(email: "test@test.com", password: "password", username: "test", name: "test") {
        email
        token
      }
    }
    """
    req = requests.get("{}/graphql?query={}".format(url,
                                                    urllib.parse.quote(query)))
    assert req.status_code == 200


def test_profile_exists():
    """
    /graphql endpoint (GET)
    Tries to re-register the same account
    """
    query = """
    {
      register(email: "test@test.com", password: "password", username: "test", name: "test") {
        email
        token
      }
    }
    """
    req = requests.get("{}/graphql?query={}".format(url,
                                                    urllib.parse.quote(query)))

    assert len(req.json()["errors"]) == 1
    assert req.json()["errors"][0][
               "message"] == "Profile with that username currently exists in the system."


def test_login():
    """
    /graphql endpoint (GET)
    Login's to created account
    """
    query = """
    {
      login(username: "test", password: "password") {
        email
        token
      } 
    }
    """
    req = requests.get("{}/graphql?query={}".format(url,
                                                    urllib.parse.quote(query)))
    assert req.status_code == 200


def test_profile():
    """
    /graphql endpoint (GET)
    Token authentication to fetch profile data
    """
    query_profile = """
       {
         login(username: "test", password: "password") {
           email
           token
         } 
       }
   """
    req = requests.get("{}/graphql?query={}".format(
        url, urllib.parse.quote(query_profile)))

    token = req.json()['data']['login']['token']

    query = "{profile(token: \"" + token + "\") { email name username " \
                                           "isVerified }} "
    req = requests.get("{}/graphql?query={}".format(url,
                                                    urllib.parse.quote(query)))
    assert req.status_code == 200


def test_login_wrong_password():
    """
    /graphql endpoint (GET)
    Tries to login with false credentials
    """
    query = """
    {
      login(username: "test", password: "wrong") {
        email
        token
      } 
    }
    """
    r = requests.get("{}/graphql?query={}".format(url,
                                                  urllib.parse.quote(query)))

    assert len(r.json()['errors']) == 1
    assert r.json()['errors'][0][
               'message'] == "The password is incorrect. Please try again."


def test_long_no_profile():
    """
    /graphql endpoint (GET)
    Deletes and tries to fetch deleted account
    """
    profile_collections.delete_one({"username": "test"})
    query = """
    {
      login(username: "test", password: "I don't exist") {
        email
        token
      } 
    }
    """
    req = requests.get("{}/graphql?query={}".format(url,
                                                    urllib.parse.quote(query)))

    assert len(req.json()['errors']) == 1
    assert req.json()['errors'][0][
               'message'] == "The profile by the username test, was not found in the system."


def test_user_wrong_token():
    def random(len=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(choice(letters) for _ in range(len))

    query = "{profile(token: \"" + random(
        50) + "\") { email name username isVerified }}"
    r = requests.get("{}/graphql?query={}".format(url,
                                                  urllib.parse.quote(query)))
    assert len(r.json()['errors']) == 1
    assert r.json()['errors'][0]['message'] == "Token is invalid."
