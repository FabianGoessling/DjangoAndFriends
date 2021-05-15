from .schema import schema
import random
from .models import Category, Ingredient
from django.contrib.auth.models import User, Group
from django.http.request import HttpRequest
from rest_framework import permissions
from rest_framework import viewsets

from .serializers import UserSerializer, GroupSerializer
from django.shortcuts import render

from django.http.response import HttpResponse


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


def graphiql(request):
    """Trivial view to serve the `graphiql.html` file."""
    return render(request, 'api/graphiql.html')


def test_subscription(request) -> HttpRequest:
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
