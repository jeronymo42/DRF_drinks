from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from main.models import Drinks, BeverageType

# Create your views here.

@api_view(['GET', 'POST'])
def index(request):
    if request.method == "GET":
        list_of_drinks = Drinks.objects.all().values_list()
        return Response(list_of_drinks)
    elif request.method == "POST":
        beverage_type = BeverageType(id=request.data["beverage_type"])
        Drinks.objects.create(name = request.data["name"], degree = request.data["degree"], description = request.data["description"], image = request.data["image"], beverage_type = beverage_type)
        return Response({'answer':'Success!'})