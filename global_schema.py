import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models.profile_model import ProfileModel


class ProfileSchema(MongoengineObjectType):
    """
    A Profile Schema defining the types and relationship between fields in ProfileModel
    """

    class Meta:
        """
        Meta class to set different options
        """
        model = ProfileModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    """
    Defines the query types
    """
    node = Node.Field()
    profile = graphene.Field(ProfileSchema)
    every_profile = MongoengineConnectionField(ProfileSchema)


global_schema = graphene.Schema(query=Query,
                                types=[ProfileSchema])
