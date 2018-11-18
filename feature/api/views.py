from django.shortcuts import render
from rest_framework import viewsets
from core.models import FeatureRequest
from api.serializers import FeatureRequestSerializer



class FeatureRequestViewset(viewsets.ModelViewSet):
    queryset = FeatureRequest.objects.all()
    serializer_class = FeatureRequestSerializer
