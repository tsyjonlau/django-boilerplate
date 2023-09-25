from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

# Create your views here.
class MainView(APIView):
    serializer_class = ReactSerializer
  
    def get(self, request):
        detail = []
        return Response(detail)
  
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)