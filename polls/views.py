from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello from the server poll app")


def new(request):
    return HttpResponse("This is the new page")