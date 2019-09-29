from auth import encode_token
from graphene import ObjectType, String, Boolean


class ProfileSchema(ObjectType):
    """
    Models a profile schema
    """
    _id = String(required=True)
    username = String(required=True)
    name = String()
    email = String()
    is_verified = Boolean(required=True)
    token = String()

    def resolve_is_verified(self, info):
        return self["is_verified"]["status"]

    def resolve_token(self, info):
        print("resolve_token ->", self["username"])
        return encode_token({"username": self["username"]})
