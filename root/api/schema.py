import channels_graphql_ws
import graphene
from graphene import ObjectType, relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField  # noqa

from .models import Category, Ingredient

# Graphene will automatically map the Category model's fields onto the
# CategoryNode. This is configured in the CategoryNode's Meta class 
# (as you can see below)


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (relay.Node, )


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        # Allow for some more advanced filtering here
        fields = ("name",)


class MySubscription(channels_graphql_ws.Subscription):
    ingredient = graphene.Field(IngredientNode)

    @staticmethod
    def subscribe(root, info):
        return ["group42"]

    @staticmethod
    def publish(payload, info):
        return MySubscription(ingredient=payload)


class Query(ObjectType):
    last_ingredient = graphene.Field(IngredientNode)

    @staticmethod
    def resolve_last_ingredient(parent, info):
        return Ingredient.objects.last()


class Subscription(ObjectType):
    test_subscription = MySubscription.Field()


schema = graphene.Schema(
    query=Query,
    subscription=Subscription,
)


class MyGraphqlWsConsumer(channels_graphql_ws.GraphqlWsConsumer):
    """Channels WebSocket consumer which provides GraphQL API."""
    schema = schema

    # Uncomment to send keepalive message every 42 seconds.
    # send_keepalive_every = 42

    # Uncomment to process requests sequentially (useful for tests).
    # strict_ordering = True

    async def on_connect(self, payload):
        """New client connection handler."""
        # You can `raise` from here to reject the connection.
        print("New client connected!")
