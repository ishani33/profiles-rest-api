"""a view is basically the application logic behind our API, it's the code that runs when user visits our API endpoint"""
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response #Response object is the standard response object that we return from our APIView
from rest_framework import status
from . import serializers


# Create your views here.

class HelloApiView(APIView):
    """test api view"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function(get,post,put,patch,delete)',
            'It is similar to traditional django view',
            'Gives most control over logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})


    def post(self, request):
        """Create a Hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Handles updating an object"""

        return Response({'method':'put'})


    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""

        return Response({'method':'patch'})


    def delete(self, request, pk=None):
        """Deletes an object"""

        return Response({'method':'patch'})
