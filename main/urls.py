from django.contrib import admin
from django.urls import path
from main.views import drinks, drink

urlpatterns = [
    path('drinks/', drinks),
    path('drinks/<int:num>', drink),
]
