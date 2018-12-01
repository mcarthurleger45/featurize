from django.shortcuts import render
from rest_framework import viewsets
from core.models import FeatureRequest
from api.serializers import FeatureRequestSerializer, UserSerializer, UserSerializerWithToken
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action

class FeatureRequestViewset(viewsets.ModelViewSet):
    queryset = FeatureRequest.objects.all()
    serializer_class = FeatureRequestSerializer
        

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def user(self, request):
        query = self.queryset.filter(user__id=pk)
        serializer = self.get_serializer(query, many=True)
        return Response(serializer.data)

