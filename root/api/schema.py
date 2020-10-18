import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType


class UserG(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    users = graphene.List(UserG)

    def resolve_users(self, info): # noqa
        return User.objects.all()


schema = graphene.Schema(query=Query)
