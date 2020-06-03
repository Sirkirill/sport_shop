from allauth.account.models import EmailConfirmationHMAC
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from profiles.models import Section
from profiles.serializers import SectionSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage teams
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
