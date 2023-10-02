from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from main.models import Drinks, BeverageType

# Create your views here.

@api_view(['GET', 'POST'])
def drinks(request):
    if request.method == "GET":
        list_of_drinks = Drinks.objects.all().values()
        return Response(list_of_drinks)
    elif request.method == "POST":
        beverage_type = BeverageType(id=request.data["beverage_type"])
        Drinks.objects.create(name = request.data["name"], degree = request.data["degree"], description = request.data["description"], image = request.data["image"], beverage_type = beverage_type)
        return Response(status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'DELETE'])
def drink(request, num):
    if request.method == 'GET':
        return Response(Drinks.objects.filter(id=num).values())
    elif request.method == 'DELETE':
        Drinks(id=num).delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
