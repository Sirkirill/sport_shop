from allauth.account.models import EmailConfirmationHMAC
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from profiles.models import Section, User, Subscription
from profiles.serializers import SectionSerializer, UserDetailsSerializer, SubscriptionSerializer


def confirm_email(request, key):
    email_confirmation = EmailConfirmationHMAC.from_key(key)
    if email_confirmation:
        email_confirmation.confirm(request)
    return HttpResponseRedirect(reverse_lazy('api'))


class SectionsViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage sections
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class UsersItemViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    pass


class SubscriptionsViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    pass
