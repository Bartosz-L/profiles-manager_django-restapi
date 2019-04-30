from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from . import serializers
from . import models
from . import permissions


# Create your views here.


# test api view
class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'dummy'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        return Response({'method': "delete"})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'users actions (list-create, retrieve, update, partial_update',
        ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.object.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
