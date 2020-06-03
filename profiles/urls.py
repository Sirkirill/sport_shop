from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from profiles.views import TeamViewSet

sections_router = DefaultRouter()
sections_router.register(r'', TeamViewSet, basename='teams')


urlpatterns = sections_router.urls