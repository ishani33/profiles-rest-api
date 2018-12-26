"""a view is basically the application logic behind our API, it's the code that runs when user visits our API endpoint"""
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response #Response object is the standard response object that we return from our APIView

# Create your views here.

class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function(get,post,put,patch,delete)',
            'It is similar to traditional django view',
            'Gives most control over logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})
