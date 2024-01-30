from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def creat_movies(request):
    Response({}, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_movies(request, id):
    pass

@api_view(["POST"])
def create_ratings(request):
    pass