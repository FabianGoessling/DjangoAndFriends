from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('REST/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('test_subscription/', views.test_subscription),
    path('graphql_example', views.graphql_example)
]
