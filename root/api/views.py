import random

from django.contrib.auth.models import Group, User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import Category, Ingredient
from .schema import schema
from .serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def test_subscription(request) -> HttpResponse:
    """Test the subscription part of the graphQL API

    Args:
        request (HttpRequest): standard request

    Returns:
        [type]: [description]
    """
    del request
    ingredient_ = Ingredient.objects.create(name=str(random.random()),
                                            category=Category.objects.first())
    schema.MySubscription.broadcast(group="group42",
                                    payload=ingredient_)
    return HttpResponse()


def graphql_example(request: HttpRequest) -> HttpResponse:
    """Load the graphql example page
    """
    return render(request, template_name="api/graphQL_example.html")
