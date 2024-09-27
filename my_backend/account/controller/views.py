from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.serilaizers import AccountSerializer

class AccountView(viewsets.ViewSet):
    pass

