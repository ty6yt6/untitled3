from django.shortcuts import render
from django import http

def register(request):
    return http.HttpResponse("你看我像不像注册")
# Create your views here.

def tupi(request):
    return http.HttpResponse("wuliao")