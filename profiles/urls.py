from django.conf.urls import url
from django.urls import include
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from profiles.views import SectionsViewSet, SubscriptionsViewSet, UsersItemViewSet

sections_router = DefaultRouter()
sections_router.register(r'', SectionsViewSet, basename='section')

subscription_router = DefaultRouter()
subscription_router.register(r'', SubscriptionsViewSet, base_name='lists')

users_router = DefaultRouter()
users_router.register(r'', UsersItemViewSet, base_name='lists')

urlpatterns = [
    re_path(r'sections/', include(sections_router.urls)),
    re_path(r'subscription/', include(subscription_router.urls)),
    re_path(r'users/', include(users_router.urls)),
]