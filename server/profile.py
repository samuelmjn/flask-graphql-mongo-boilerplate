from server.auth import encode_token
from graphene import ObjectType, String, Boolean


class ProfileSchema(ObjectType):
    """
    Profile Schema defining the types and relationship between Fields in your
    API.
    """
    _id = String(required=True)
    username = String(required=True)
    name = String()
    email = String()
    is_verified = Boolean(required=True)
    token = String()

    def resolve_is_verified(self, info):
        print(info)
        return self["is_verified"]["status"]

    def resolve_token(self, info):
        print(info)
        return encode_token({"username": self["username"]})
