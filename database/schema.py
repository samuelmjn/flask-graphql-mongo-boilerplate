import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType, MongoengineConnectionField
from models import (Profile as ProfileModel)


class ProfileSchema:
    class Meta:
        model = ProfileModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    """
    Defines the query types
    """
    node = Node.Field()
    every_profile = MongoengineConnectionField(ProfileSchema)


schema = graphene.Schema(query=graphene.ObjectType(Query),
                         types=[ProfileSchema])
